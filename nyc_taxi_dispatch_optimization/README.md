# NYC Taxi Dispatch Optimization: A Reinforcement Learning Approach

## 1. Project Goal

* **Objective:** State the primary business goal of this project. What key performance indicator (KPI) are you trying to optimize?
  * *Example: To develop a reinforcement learning agent that optimizes the dispatch of idle taxis in Manhattan to minimize passenger wait times and maximize driver utilization.*

* **Problem:** Briefly describe the real-world problem you are solving.
  * *Example: In a competitive ride-hailing market, inefficient dispatch leads to longer passenger wait times, lower driver earnings, and lost revenue. This project tackles this by creating an intelligent agent that learns optimal repositioning strategies for a fleet of taxis.*

* **Key Results:** Summarize your main finding in one or two sentences. This is your elevator pitch.
  * *Example: The trained DQN agent demonstrated a 25% reduction in average passenger wait time and a 15% increase in total trips completed compared to a baseline random-dispatch strategy in a simulated environment.*

## 2. Technical Overview

* **Methodology:** Briefly explain your approach.
  * *Example: This project uses a Deep Q-Network (DQN), a model-free reinforcement learning algorithm. An agent is trained in a custom-built simulation environment that models the dynamics of taxi supply and passenger demand across Manhattan's taxi zones.*

* **Data:** Describe the dataset(s) you used.
  * *Example: The simulation environment is built using the NYC TLC Trip Record Data. Specifically, the Yellow Taxi trip records for January 2022 were used to model passenger demand patterns and travel times between zones.*

* **Tech Stack:** List the key libraries and technologies.
  * **Languages:** Python
  * **Libraries:** Pandas, NumPy, Scikit-learn, PyTorch, Gym, Matplotlib, Seaborn

## 3. Project Structure

Describe the purpose of each key file and directory.

```
.
├── 01_data_exploration.ipynb       # Initial EDA on the NYC Taxi dataset
├── 02_simulation_environment.ipynb # Notebook for developing the custom Gym environment
├── 03_travel_matrix_creation.ipynb # Pre-calculating and saving the travel time matrix
├── 04_agent_training.ipynb         # Training the DQN agent and visualizing results
├── src/
│   ├── environment.py              # (Recommended) Python module for the Gym environment
│   └── agent.py                    # (Recommended) Python module for the DQN Agent
├── data/
│   └── yellow_tripdata_...parquet  # Raw data file
└── README.md                       # This file
```

## 4. Key Steps & Findings

### Step 1: Data Exploration & Feature Engineering
*   What were the key insights from your EDA?
*   How did you process the data to make it suitable for the simulation? (e.g., time binning, zone mapping)

### Step 2: Simulation Environment
*   How does your `Gym` environment work?
*   **State Space:** What information does the agent see at each step? (e.g., taxi locations, demand per zone, time of day)
*   **Action Space:** What can the agent do? (e.g., move an idle taxi from zone A to zone B)
*   **Reward Function:** How do you incentivize the desired behavior? (e.g., positive reward for successful pickups, negative reward for idle time)

### Step 3: Agent Training
*   Describe your agent's architecture (e.g., neural network layers).
*   Show the learning curve (e.g., plot of reward per episode). This is crucial evidence that your agent learned something.
*   What were the final hyperparameters for your model?

## 5. Results & Performance

*   **Performance Metrics:** How did you evaluate your agent's performance? (e.g., average wait time, total revenue, idle taxi ratio).
*   **Baseline Comparison:** How does your agent compare to a baseline strategy (e.g., random dispatch, or a simple heuristic)? A quantitative comparison here is essential.
*   **Visualizations:** Include key charts (e.g., agent's performance over time, heatmaps of agent's dispatch decisions).

## 6. How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone ...
    ```
2.  **Set up the environment:**
    ```bash
    conda env create -f environment.yml
    conda activate taxi-rl
    ```
3.  **Run the notebooks:**
    *   Execute the notebooks in order from `01` to `04`.
    *   Alternatively, explain how to run a single script if you refactor the code.
      ```bash
      python src/main.py --mode train
      ```

## 7. Future Work & Limitations

*   What are the limitations of your approach? (e.g., simulation doesn't account for traffic, uses historical data).
*   What are the next steps you would take to improve the project? (e.g., use a more advanced RL algorithm, incorporate real-time data, expand to other boroughs).
