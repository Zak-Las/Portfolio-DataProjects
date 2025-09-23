# E-Commerce Clothing Classifier with PyTorch

## Project Overview
This project demonstrates the end-to-end development of a deep learning image classification model for an e-commerce clothing retailer. The goal is to automatically categorize product images into 10 distinct garment types, a critical task for streamlining product listing, improving customer search experience, and enhancing inventory management.

The project uses the **FashionMNIST** dataset as a proxy for real-world clothing images and leverages **PyTorch** to build, train, and evaluate a Convolutional Neural Network (CNN).

![Clothing Classification](figures/clothing_classification.png)

## Problem Statement
E-commerce platforms face significant challenges in organizing large and rapidly changing inventories. Manual categorization of product images is not only time-consuming and costly but also prone to human error, leading to a poor customer experience. This project addresses the need for a robust, automated solution for garment classification that can scale with a growing business.

## Data Exploration
The project begins with an exploratory data analysis (EDA) of the FashionMNIST dataset, which contains 70,000 grayscale images (60,000 for training, 10,000 for testing) of 10 clothing categories. The EDA confirms that the dataset is well-balanced across all classes, providing a solid foundation for training an unbiased model.

## Model Architecture
A custom Convolutional Neural Network (CNN) was designed and implemented in PyTorch. The final architecture consists of the following layers, chosen to effectively capture hierarchical features from the images:

1.  **Convolutional Layer 1**: 16 output channels, 3x3 kernel, ReLU activation.
2.  **Max Pooling Layer 1**: 2x2 kernel, stride of 2.
3.  **Convolutional Layer 2**: 32 output channels, 3x3 kernel, ReLU activation.
4.  **Max Pooling Layer 2**: 2x2 kernel, stride of 2.
5.  **Flatten Layer**: To transition from 2D feature maps to a 1D feature vector.
6.  **Fully Connected (Linear) Layer**: 1568 input features and 10 output units, corresponding to the 10 clothing classes.

## Training and Evaluation
The model was trained and evaluated using an iterative approach, demonstrating the impact of key deep learning techniques.

#### Training Configuration:
-   **Loss Function**: `CrossEntropyLoss`, as it is well-suited for multi-class classification problems.
-   **Optimizer**: `Adam` with a learning rate of `0.001`.
-   **Epochs**: The model was trained for **10 epochs**, which was found to provide a good balance between training time and performance improvement.

#### Evaluation Metrics:
The model's performance was assessed using three key metrics:
-   **Accuracy**: The overall percentage of correctly classified images.
-   **Precision**: The ability of the model to avoid false positives for each class.
-   **Recall**: The ability of the model to find all relevant instances of each class.

## Results and Performance
The iterative development process, which involved increasing the training epochs and deepening the network architecture, resulted in a high-performing final model.

**Final Model Performance:**
-   **Overall Accuracy**: [Insert Final Accuracy Here, e.g., 90.5%]

**Per-Class Performance:**

| Class         | Precision | Recall |
|---------------|-----------|--------|
| T-shirt/top   | [Value]   | [Value]|
| Trouser       | [Value]   | [Value]|
| Pullover      | [Value]   | [Value]|
| Dress         | [Value]   | [Value]|
| Coat          | [Value]   | [Value]|
| Sandal        | [Value]   | [Value]|
| Shirt         | [Value]   | [Value]|
| Sneaker       | [Value]   | [Value]|
| Bag           | [Value]   | [Value]|
| Ankle boot    | [Value]   | [Value]|

*(Note: Please run the final evaluation cell in the notebook to populate the table with the latest metrics.)*

## Setup and Usage
To replicate the project and experiment with the model:

1.  **Clone the repository.**
2.  **Environment**: This project is designed to run in the provided dev container, which includes all necessary dependencies like PyTorch and TorchMetrics.
3.  **Run the Notebook**: Open and execute the `ecommerce_clothing_classifier.ipynb` notebook in a Jupyter environment (like VS Code). The notebook will guide you through the data loading, model training, evaluation, and visualization steps.

## Key Skills Demonstrated
-   **Deep Learning**: Designing, building, and training a custom CNN from scratch using PyTorch.
-   **Model Optimization**: Iteratively improving model performance by adjusting architecture (deeper network) and training parameters (epochs).
-   **Data Science Workflow**: Conducting exploratory data analysis, preprocessing data, and performing rigorous model evaluation.
-   **Problem Solving**: Translating a real-world business need into a data science problem and delivering a robust, automated solution.
