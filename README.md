# Data Science Project Portfolio

This repository showcases my skills in using Python, SQL, PyTorch, and scikit-learn.

## Projects

Here's a summary of the projects you'll find in this repository, with machine learning projects listed first to highlight my skills in this area:

-   **[E-Commerce Clothing Classifier (PyTorch)](./ecommerce_clothing_classifier/)**: Built a CNN from scratch to classify garment images, achieving over 90% accuracy on the test set.
    -   *Tech: PyTorch, scikit-learn*

-   **[Insurance Claim Prediction (Regression Modeling)](./insurance_claim_prediction/)**: Compared regression models to predict insurance claims, demonstrating proficiency in both statistical and machine learning approaches.
    -   *Tech: statsmodels, scikit-learn*

-   **[World Life Expectancy (PostgreSQL)](./world_life_expectancy_sql/)**: Performed data cleaning and exploratory analysis on a global life expectancy dataset.
    -   *Tech: PostgreSQL*

-   **[Automated Data Cleaning (MySQL)](./automated_data_cleaning_sql/)**: Developed an automated data cleaning pipeline using advanced database features.
    -   *Tech: MySQL, Stored Procedures, Triggers, Events*

## Getting Started

This entire portfolio is containerized, allowing for a fully reproducible environment. You can explore the projects using either VS Code Dev Containers (recommended for the best experience) or by manually creating a Conda enviroment.

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
1.  Clone this repository to your local machine and navigate into the directory:
    ```bash
    git clone https://github.com/Zak-Las/Portfolio-DataProjects.git
    cd Portfolio-DataProjects
    ```
2.  Create and activate the Conda environment using the `environment.yml` file:
    ```bash
    conda env create -f environment.yml
    conda activate Zak-Las
    ```
3. Once the environment is active, you can run any of the notebooks or scripts.