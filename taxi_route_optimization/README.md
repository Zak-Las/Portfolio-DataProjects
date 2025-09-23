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

The agent is trained using **Q-learning**, a model-free algorithm chosen for its effectiveness in environments with discrete state and action spaces.

1.  **Q-Table Initialization**: A Q-table of size (number of states × number of actions) is initialized with zeros.
2.  **Training Loop**: The agent is trained over 2,000 episodes. In each episode, it uses an **epsilon-greedy** strategy to balance exploration (taking random actions) and exploitation (choosing the best-known action from the Q-table).
3.  **Q-Value Updates**: After each action, the Q-table is updated using the Bellman equation, which adjusts the value of the state-action pair based on the received reward and the maximum Q-value of the next state.
4.  **Policy Extraction**: After training, the optimal policy is derived from the Q-table by selecting the action with the highest Q-value for each state.

## How to Run

To replicate the project, follow these steps:

1.  **Install Dependencies**: Ensure you have Python and the required libraries installed.
    ```sh
    pip install numpy gymnasium imageio ipython
    ```
2.  **Run the Notebook**: Open and run the [taxi_route_optimization.ipynb](taxi_route_optimization.ipynb) notebook in a Jupyter environment. The notebook will execute the training, testing, and visualization steps.
3.  **View the Results**: The final output is `taxi_agent_behavior.gif`, which visualizes the trained agent's performance on a test episode.

## File Structure

-   [taxi_route_optimization.ipynb](taxi_route_optimization.ipynb): The Jupyter Notebook containing all the code for environment setup, agent training, policy evaluation, and visualization.
-   `taxi_agent_behavior.gif`: The output GIF showing the agent's learned behavior.
-   `figures/city-1265055_1280.jpg`, `figures/Taxi_snap.png`, `figures/qlearning.png`: Image assets used within the notebook