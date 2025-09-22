# Use Miniconda3 as the base image
FROM continuumio/miniconda3:latest

# Set working directory
WORKDIR /app

# Copy environment.yml
COPY environment.yml ./

# Create the conda environment
RUN conda env create -f environment.yml

# Make RUN commands use the new environment
SHELL ["/bin/bash", "-c"]

# Activate the environment by default
ENV PATH /opt/conda/envs/ZakLas/bin:$PATH

# Set the default command to start a bash shell
CMD ["bash"]
