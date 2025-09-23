# Taxi Route Optimization with Reinforcement Learning

This project explores the application of reinforcement learning to solve the classic "Taxi-v3" problem from the `gymnasium` library. The goal is to train an intelligent agent capable of determining the optimal route to pick up a passenger and transport them to their destination within a simulated grid-based environment.

![Agent Behavior](taxi_agent_behavior.gif)

## Project Overview

The core of this project is to build and train a Q-learning agent. The agent learns a policy—a map of states to optimal actions—that maximizes its cumulative reward. This involves navigating a 5x5 grid, managing passenger pickups and drop-offs, and avoiding penalties for inefficient or illegal moves. The entire implementation and analysis are contained within the [taxi_route_optimization.ipynb](taxi_route_optimization.ipynb) notebook.

## The Environment: Taxi-v3

The `Taxi-v3` environment provides a discrete, simulated world with the following characteristics:

-   **State Space**: 500 distinct states, encoding the taxi's position, the passenger's location, and the destination.
-   **Action Space**: 6 discrete actions: `south`, `north`, `east`, `west`, `pickup`, and `dropoff`.
-   **Reward System**:
    -   `+20` for a successful passenger drop-off.
    -   `-1` for each step taken to encourage efficiency.
    -   `-10` for illegal `pickup` or `dropoff` actions.

## Methodology

The agent is trained using **Q-learning**, a model-free algorithm chosen for its effectiveness in environments with discrete state and action spaces. The core of Q-learning is the Bellman equation, which iteratively updates the Q-value for a given state-action pair:

$$Q(s, a) \leftarrow Q(s, a) + \alpha [R(s, a) + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$

#### Training Process

1.  **Q-Table Initialization**: A Q-table of size (500 states × 6 actions) is initialized with zeros.
2.  **Hyperparameter Tuning**: The learning process was guided by the following hyperparameters:
    *   **Learning Rate (`alpha`)**: 0.1
    *   **Discount Factor (`gamma`)**: 1.0
    *   **Epsilon (`epsilon`)**: Initial value of 1.0, decaying to a minimum of 0.01.
3.  **Training Loop**: The agent was trained over 2,000 episodes. In each episode, it used an **epsilon-greedy** strategy to balance exploration (taking random actions) and exploitation (choosing the best-known action from the Q-table).
4.  **Policy Extraction**: After training, the optimal policy is derived from the Q-table by selecting the action with the highest Q-value for each state.

## Results and Evaluation

The effectiveness of the Q-learning agent was evaluated by its performance during and after training.

-   **Learning Progression**: The agent demonstrated significant learning over the 2,000 training episodes. Initially, its performance was random, resulting in highly negative cumulative rewards. As training progressed, the agent's policy improved, leading to consistently positive rewards, indicating it had learned to efficiently pick up and drop off the passenger.
-   **Optimal Policy**: The final trained agent successfully navigates the environment, avoiding penalties and completing the task in an optimal number of steps. This is visualized in the `taxi_agent_behavior.gif`, which shows the agent executing a flawless run on a test episode.

## Conclusion and Future Work

This project successfully demonstrates the application of Q-learning to solve a route-optimization problem in a discrete environment. The agent learned a robust policy, proving its ability to navigate the state space efficiently.

Potential future work could involve:
-   Applying more advanced Reinforcement Learning algorithms, such as Deep Q-Networks (DQN), to tackle more complex, high-dimensional environments.
-   Experimenting with different hyperparameter values and reward structures to further optimize the agent's learning speed and final performance.

## File Structure

-   [taxi_route_optimization.ipynb](taxi_route_optimization.ipynb): The Jupyter Notebook containing all the code for environment setup, agent training, policy evaluation, and visualization.
-   `taxi_agent_behavior.gif`: The output GIF showing the agent's learned behavior.
-   `figures/city-1265055_1280.jpg`, `figures/Taxi_snap.png`, `figures/qlearning.png`: Image assets used within the notebook