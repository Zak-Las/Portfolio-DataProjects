import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import numpy as np
import random
from collections import deque, namedtuple

class ReplayBuffer:
    """A simple replay buffer to store and sample experiences."""
    def __init__(self, buffer_size, batch_size, seed):
        self.memory = deque(maxlen=buffer_size)
        self.batch_size = batch_size
        self.experience = namedtuple("Experience", field_names=["state", "action", "reward", "next_state", "done"])
        self.seed = random.seed(seed)

    def add(self, state, action, reward, next_state, done):
        e = self.experience(state, action, reward, next_state, done)
        self.memory.append(e)

    def sample(self):
        experiences = random.sample(self.memory, k=self.batch_size)
        
        # The states and next_states are now lists of dictionaries
        states = [e.state for e in experiences if e is not None]
        next_states = [e.next_state for e in experiences if e is not None]

        # Convert other fields to tensors as before
        actions = torch.from_numpy(np.vstack([e.action for e in experiences if e is not None])).long()
        rewards = torch.from_numpy(np.vstack([e.reward for e in experiences if e is not None])).float()
        dones = torch.from_numpy(np.vstack([e.done for e in experiences if e is not None]).astype(np.uint8)).float()

        return (states, actions, rewards, next_states, dones)

    def __len__(self):
        return len(self.memory)

class DQN(nn.Module):
    """
    A more advanced DQN that processes each taxi's state individually.
    This allows the network to directly associate a taxi's unique state 
    (its location relative to the request) with its Q-value.
    """
    def __init__(self, num_taxis, num_locations, embedding_dim=10):
        super(DQN, self).__init__()
        
        self.embedding_dim = embedding_dim
        
        # Embedding layers for categorical features
        self.loc_embedding = nn.Embedding(num_locations, embedding_dim)
        self.day_embedding = nn.Embedding(7, 3)
        self.hour_embedding = nn.Embedding(24, 5)
        
        # This sub-network processes the combined state for ONE taxi
        # Input: taxi_loc_emb + origin_loc_emb + dest_loc_emb + day_emb + hour_emb
        combined_size = embedding_dim + embedding_dim + embedding_dim + 3 + 5
        
        self.q_value_net = nn.Sequential(
            nn.Linear(combined_size, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 1) # Output a single Q-value for this taxi-request pair
        )

    def forward(self, state):
        # Embed shared request and time features once
        origin_loc = self.loc_embedding(state['request']['origin'].long()).squeeze(1)
        dest_loc = self.loc_embedding(state['request']['destination'].long()).squeeze(1)
        day = self.day_embedding(state['time']['day_of_week'].long()).squeeze(1)
        hour = self.hour_embedding(state['time']['hour_of_day'].long()).squeeze(1)
        
        # Get embeddings for all taxi locations
        # Shape: (batch_size, num_taxis, embedding_dim)
        taxis_locs = self.loc_embedding(state['taxis'].long())
        
        q_values = []
        # Iterate through each taxi to calculate its Q-value
        for i in range(taxis_locs.size(1)):
            # Get the location embedding for the i-th taxi
            # Shape: (batch_size, embedding_dim)
            taxi_loc = taxis_locs[:, i, :]
            
            # Concatenate this taxi's location with the shared request/time info
            combined_state = torch.cat([taxi_loc, origin_loc, dest_loc, day, hour], dim=1)
            
            # Calculate the Q-value for this specific taxi
            q_values.append(self.q_value_net(combined_state))
            
        # Stack the Q-values for all taxis into a single tensor
        # Shape: (batch_size, num_taxis)
        return torch.cat(q_values, dim=1)

class DQNAgent():
    """Interacts with and learns from the environment."""

    def __init__(self, num_taxis, num_locations, seed, initial_lr=5e-4):
        self.num_taxis = num_taxis
        self.qnetwork_local = DQN(num_taxis, num_locations)
        self.qnetwork_target = DQN(num_taxis, num_locations)
        self.optimizer = optim.Adam(self.qnetwork_local.parameters(), lr=initial_lr)
        
        # Add a learning rate scheduler
        # This will decrease the LR by a factor of 0.1 every 750 episodes
        self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, step_size=750, gamma=0.1)

        self.memory = ReplayBuffer(10000, 64, seed)
        self.t_step = 0
    
    def _state_to_tensor(self, states):
        """
        Converts a list of state dictionaries into a single batched tensor dictionary.
        This ensures consistent data shapes for both acting and learning.
        """
        # If a single state dict is passed, wrap it in a list
        if not isinstance(states, list):
            states = [states]

        taxis = torch.from_numpy(np.vstack([s['taxis'] for s in states])).long()
        origins = torch.from_numpy(np.vstack([s['request']['origin'] for s in states])).long()
        destinations = torch.from_numpy(np.vstack([s['request']['destination'] for s in states])).long()
        days = torch.from_numpy(np.vstack([s['time']['day_of_week'] for s in states])).long()
        hours = torch.from_numpy(np.vstack([s['time']['hour_of_day'] for s in states])).long()

        return {
            'taxis': taxis,
            'request': {'origin': origins, 'destination': destinations},
            'time': {'day_of_week': days, 'hour_of_day': hours}
        }

    def step(self, state, action, reward, next_state, done):
        self.memory.add(state, action, reward, next_state, done)
        
        self.t_step = (self.t_step + 1) % 4
        if self.t_step == 0:
            if len(self.memory) > self.memory.batch_size:
                experiences = self.memory.sample()
                self.learn(experiences, 0.99)

    def act(self, state, eps=0.):
        """Returns actions for given state as per current policy."""
        # Epsilon-greedy action selection
        if random.random() > eps:
            # Convert the single state into a batched tensor
            state_tensor = self._state_to_tensor(state)
            
            self.qnetwork_local.eval()
            with torch.no_grad():
                action_values = self.qnetwork_local(state_tensor)
            self.qnetwork_local.train()
            
            # Get the best action
            return np.argmax(action_values.cpu().data.numpy())
        else:
            # Get a random action
            return random.choice(np.arange(self.num_taxis))

    def learn(self, experiences, gamma):
        states, actions, rewards, next_states, dones = experiences

        # Use the helper to convert next_states dicts to tensors
        next_states_tensor = self._state_to_tensor(next_states)
        
        # Get max predicted Q values (for next states) from target model
        Q_targets_next = self.qnetwork_target(next_states_tensor).detach().max(1)[0].unsqueeze(1)
        
        # Compute Q targets for current states 
        Q_targets = rewards + (gamma * Q_targets_next * (1 - dones))

        # Use the helper to convert states dicts to tensors
        states_tensor = self._state_to_tensor(states)
        
        # Get expected Q values from local model
        Q_expected = self.qnetwork_local(states_tensor).gather(1, actions)

        # Compute loss
        loss = F.mse_loss(Q_expected, Q_targets)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Update target network
        self.soft_update(self.qnetwork_local, self.qnetwork_target, 1e-3)                     

    def soft_update(self, local_model, target_model, tau):
        for target_param, local_param in zip(target_model.parameters(), local_model.parameters()):
            target_param.data.copy_(tau*local_param.data + (1.0-tau)*target_param.data)
