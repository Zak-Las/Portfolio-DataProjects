# Portfolio - DataProjects
This repo will be used to host my data-related projects using SQL and Python:

- [movie industry - Python](https://github.com/Zak-Las/Portfolio-DataProjects/tree/main/movie%20industry%20-%20Python): Here I clean and perform an exploratory data analysis on a dataset of movies from imdb.
- [world life expectancy - PostgreSQL](https://github.com/Zak-Las/Portfolio-DataProjects/tree/main/world%20life%20expectancy%20-%20PostgreSQL): Here I clean and perform an exploratory data analysis on a dataset of the world life expectancy.
- [automated data cleaning - MySQL](https://github.com/Zak-Las/Portfolio-DataProjects/tree/main/automated%20data%20cleaning%20-%20MySQL): Here I use Stored Procedures, Triggers, and Events to automatically clean raw data.
- [regeression modeling of insurance claims - Python](https://github.com/Zak-Las/Portfolio-DataProjects/tree/main/predicting%20insurance%20claims%20-%20Regeression%20Modeling): Here I create a model using two different tools/packages (statsmodels + scikit-learn) to predict whether a customer will make a claim on their insurance during the policy period. 


# Installation

To set up the required Python environment for this project, follow these steps:

1. **Install [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)** if you don't already have it.

2. **Create a new conda environment from `environment.yml`:**
	```bash
	conda env create -f environment.yml
	conda activate ZakLas
	```


# Docker Option (Recommended for Reproducibility)

Alternatively, you can run this project in a Docker container using the provided `Dockerfile` and `environment.yml`.

1. **Build the Docker image:**
	```bash
	docker build -t zaklas-ds-project .
	```

2. **Run the container:**
	```bash
	docker run -it --rm zaklas-ds-project
	```

This will launch a shell inside the container with the full conda environment ready to use.