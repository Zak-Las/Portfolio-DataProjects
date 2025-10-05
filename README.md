# Data Science Project Portfolio

Welcome to my portfolio of data science projects. This repository showcases my skills in data cleaning, exploratory data analysis, machine learning, and data engineering using Python, SQL, and various data science libraries.

## Projects

Here's a summary of the projects you'll find in this repository, with machine learning projects listed first to highlight my skills in this area:

-   **[E-Commerce Clothing Classifier (PyTorch)](./ecommerce_clothing_classifier/)**: A deep learning project that builds a Convolutional Neural Network (CNN) from scratch to classify garment images from the FashionMNIST dataset.

-   **[Insurance Claim Prediction (Regression Modeling)](./insurance_claim_prediction/)**: A machine learning project where I build and compare regression models using `statsmodels` and `scikit-learn` to predict insurance claims.

-   **[Taxi Route Optimization (Reinforcement Learning)](./taxi_route_optimization/)**: A reinforcement learning project that trains an agent to solve the "Taxi-v3" problem from the `gymnasium` library. This project demonstrates the use of Q-learning to find an optimal route in a simulated environment.

-   **[Movie Industry Analysis (Python)](./movie_industry_analysis/)**: An in-depth exploratory data analysis of an IMDb movie dataset. This project involves data cleaning, visualization, and uncovering insights into the factors that drive movie success.

-   **[World Life Expectancy (PostgreSQL)](./world_life_expectancy_sql/)**: A SQL-based project focused on data cleaning and exploratory analysis of global life expectancy data.

-   **[Automated Data Cleaning (MySQL)](./automated_data_cleaning_sql/)**: Demonstrates the use of Stored Procedures, Triggers, and Events in MySQL to create an automated data cleaning pipeline for household income data.

## Getting Started

This entire portfolio is containerized, allowing for a fully reproducible environment. You can explore the projects using either VS Code Dev Containers (recommended for the best experience) or by manually building and running the Docker image.

---

### Option 1: Quick Start with VS Code & Dev Containers (Recommended)

This is the easiest and most integrated way to explore the projects.

**Prerequisites:**
- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code.

**Steps:**
1.  Clone this repository to your local machine.
2.  Open the cloned repository folder in VS Code.
3.  You will see a pop-up in the bottom-right corner asking to "Reopen in Container". Click it.
4.  VS Code will build the Docker container and configure the environment. This might take a few minutes on the first run.
5.  Once finished, you can directly open any of the `.ipynb` notebook files. VS Code will automatically use the Python environment from the container, and you can run the cells interactively within the editor.

---

### Option 2: Manual Setup with Conda

If you prefer not to use the VS Code Dev Container, you can still run the environment manually.

**Steps:**
1.  Clone this repository to your local machine.
    ```bash
    git clone https://github.com/Zak-Las/Portfolio-DataProjects.git
    cd Portfolio-DataProjects/ecommerce_clothing_classifier
    ```
2.  Open a terminal and navigate to the root directory of the repository.
3.  Create a virtual environment and install dependencies:
    ```bash
    conda env create -f environment.yml
    conda activate Zak-Las
    ```