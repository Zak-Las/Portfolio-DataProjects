# E-Commerce Clothing Classifier

## Project Overview
This project demonstrates the end-to-end development of an image classification model for an e-commerce clothing retailer. The goal is to automatically categorize product images into garment types (e.g., shirts, trousers, shoes) to streamline product listing, improve customer search experience, and enhance inventory management.

## Problem Statement
E-commerce platforms face challenges in organizing large inventories and ensuring customers can easily find products. Manual categorization is time-consuming and error-prone. Leveraging deep learning, this project builds a robust, automated solution for garment classification using the FashionMNIST dataset as a proxy for real-world clothing images.

## Approach
- **Data Loading & Exploration:** Utilized the FashionMNIST dataset, which contains 70,000 grayscale images of 10 clothing categories. Data was loaded and visualized to understand class balance and image characteristics.
- **Model Architecture:** Developed a custom Convolutional Neural Network (CNN) in PyTorch. The architecture was iteratively improved by:
  - Starting with a simple CNN
  - Increasing training epochs for better learning
  - Deepening the network with additional convolutional and pooling layers for richer feature extraction
- **Training & Evaluation:**
  - Trained the model using cross-entropy loss and Adam optimizer
  - Evaluated performance using accuracy, precision, and recall metrics (overall and per class)
  - Documented the impact of each improvement step

## Results
- Training for more epochs and using a deeper CNN both led to significant improvements in accuracy and class-wise metrics.
- The final model achieved strong performance, demonstrating the effectiveness of iterative model development and tuning.

## Key Skills Demonstrated
- Deep learning model design and optimization (PyTorch)
- Data preprocessing and augmentation
- Model evaluation and interpretation
- Experiment tracking and documentation
- Communication of technical results for business impact

## How to Use
1. Clone the repository and install dependencies (see requirements in the notebook).
2. Run `main.ipynb` step by step to reproduce the results and experiment with further improvements.

## Portfolio Value
This project showcases my ability to:
- Tackle real-world business problems with deep learning
- Build, tune, and interpret neural networks
- Communicate results clearly to both technical and non-technical stakeholders

---
*For questions or collaboration, feel free to reach out!*
