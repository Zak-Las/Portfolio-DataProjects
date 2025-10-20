import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pandas as pd

class TaxiDispatchEnvV3(gym.Env):
    """
    The definitive taxi dispatch environment.

    This version incorporates a pre-computed travel matrix for realistic, time-aware
    cost calculations and uses a profit-maximizing reward function.

    State: A dictionary with 'taxis', 'request', and 'time'.
    - 'taxis': An array of current taxi LocationIDs.
    - 'request': A dictionary with 'origin' and 'destination' LocationIDs.
    - 'time': A dictionary with 'day_of_week' and 'hour_of_day'.

    Action: An integer representing the index of the taxi to dispatch.
    """
    def __init__(self, num_taxis, data_path, matrix_path, cost_per_mile=1.5, episode_length=50):
        super(TaxiDispatchEnvV3, self).__init__()

        self.num_taxis = num_taxis
        self.cost_per_mile = cost_per_mile
        self.episode_length = episode_length
        self.current_step = 0
        
        # Load trip data
        self.df = pd.read_parquet(data_path)
        self.df['tpep_pickup_datetime'] = pd.to_datetime(self.df['tpep_pickup_datetime'])
        self.df['day_of_week'] = self.df['tpep_pickup_datetime'].dt.dayofweek
        self.df['hour_of_day'] = self.df['tpep_pickup_datetime'].dt.hour
        
        # Load and index the travel matrix for fast lookups
        travel_matrix_df = pd.read_parquet(matrix_path)
        self.travel_matrix = travel_matrix_df.set_index(['PULocationID', 'DOLocationID', 'day_of_week', 'hour_of_day'])

        # Get unique locations for defining the space
        self.unique_locations = sorted(pd.concat([self.df['PULocationID'], self.df['DOLocationID']]).unique())
        self.location_map = {loc: i for i, loc in enumerate(self.unique_locations)}
        self.inverse_location_map = {i: loc for i, loc in enumerate(self.unique_locations)}
        num_locations = len(self.unique_locations)

        # Define spaces
        self.action_space = spaces.Discrete(num_taxis)
        
        self.observation_space = spaces.Dict({
            'taxis': spaces.MultiDiscrete([num_locations] * num_taxis),
            'request': spaces.Dict({
                'origin': spaces.Discrete(num_locations),
                'destination': spaces.Discrete(num_locations)
            }),
            'time': spaces.Dict({
                'day_of_week': spaces.Discrete(7),
                'hour_of_day': spaces.Discrete(24)
            })
        })

    def _get_observation(self):
        taxi_indices = [self.location_map[loc] for loc in self.taxi_locations]
        origin_index = self.location_map[self.current_trip['PULocationID']]
        dest_index = self.location_map[self.current_trip['DOLocationID']]

        return {
            'taxis': np.array(taxi_indices),
            'request': {'origin': origin_index, 'destination': dest_index},
            'time': {'day_of_week': self.current_trip['day_of_week'], 'hour_of_day': self.current_trip['hour_of_day']}
        }

    def _get_travel_cost(self, origin_id, dest_id, day, hour):
        """Looks up the travel distance from the pre-computed matrix."""
        try:
            # Look up the specific time
            cost = self.travel_matrix.loc[(origin_id, dest_id, day, hour)]
            return cost['mean_distance']
        except KeyError:
            # Fallback: if no data for this specific hour, try to get the average for the day
            try:
                cost = self.travel_matrix.loc[(origin_id, dest_id, day)].mean()
                return cost['mean_distance']
            except KeyError:
                # Fallback: if no data for this route at all, return a high penalty distance
                return 10.0 # High penalty for unknown routes

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_step = 0
        self.taxi_locations = np.random.choice(self.unique_locations, self.num_taxis)
        self.current_trip = self.df.sample(1, random_state=self.np_random).iloc[0]
        return self._get_observation(), {}

    def step(self, action):
        chosen_taxi_location_id = self.taxi_locations[action]
        
        # Get trip details from the current request
        pickup_location_id = self.current_trip['PULocationID']
        fare = self.current_trip['fare_amount']
        actual_trip_distance = self.current_trip['trip_distance']
        day = self.current_trip['day_of_week']
        hour = self.current_trip['hour_of_day']

        # Calculate deadhead distance using our travel matrix
        deadhead_distance = self._get_travel_cost(chosen_taxi_location_id, pickup_location_id, day, hour)
        
        # Calculate total cost
        total_distance = deadhead_distance + actual_trip_distance
        total_cost = total_distance * self.cost_per_mile
        
        # Calculate profit-based reward
        reward = fare - total_cost
        
        # Update the dispatched taxi's location to the dropoff of the completed trip
        self.taxi_locations[action] = self.current_trip['DOLocationID']
        
        # Get a new trip for the next state
        self.current_trip = self.df.sample(1, random_state=self.np_random).iloc[0]
        
        self.current_step += 1
        terminated = self.current_step >= self.episode_length
        
        return self._get_observation(), reward, terminated, False, {}

    def render(self, mode='human'):
        pass
