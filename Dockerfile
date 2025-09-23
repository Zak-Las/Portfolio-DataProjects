# 1. Base Image: Pinning the version for reproducibility
# Using a specific version of the miniconda3 image ensures that the build is reproducible.
# The 'latest' tag can change, potentially breaking your build in the future.
FROM continuumio/miniconda3:4.12.0

# 2. Metadata: Add labels to describe the image
LABEL maintainer="Zak-Las"
LABEL description="A containerized environment for Zak's data science portfolio projects."

# 3. Environment Variables: Centralize configuration
# Using ARG and ENV makes the Dockerfile more readable and easier to maintain.
ARG CONDA_ENV_NAME=datascience_env
ENV CONDA_ENV_NAME=${CONDA_ENV_NAME}
ENV APP_HOME=/workspace
WORKDIR $APP_HOME

# 4. Caching Dependencies: Optimize build time
# Copy only the environment file first and install dependencies.
# This leverages Docker's layer caching. The dependencies will only be re-installed
# if the environment.yml file changes, not every time a project file is modified.
COPY environment.yml .
RUN conda env create -f environment.yml

# 5. Copy Project Files: Add project files after dependency installation
COPY . .

# 6. Activate Conda Environment: Make the environment's tools available on the PATH
# This makes it easy to run commands like 'python' or 'jupyter' directly.
ENV PATH /opt/conda/envs/${CONDA_ENV_NAME}/bin:$PATH

# 7. Expose Port: Document the port used by Jupyter
EXPOSE 8888

# 8. Default Command: Start Jupyter Lab for a better user experience
# Jupyter Lab provides a more modern and feature-rich interface than the classic notebook.
# The token is intentionally left blank for ease of access in a trusted environment.
# For a public-facing server, you would want to configure a token or password.
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]
