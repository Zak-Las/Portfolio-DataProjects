import torch
import torch.nn as nn
import torch.optim as optim
from src.data_loader import get_data_loaders
from src.model import DeeperCNN
from src.train import train_and_validate, plot_history
from src.evaluate import evaluate_model

def main():
    # --- 1. Load Data ---
    train_loader, val_loader, test_loader, classes = get_data_loaders(batch_size=64)
    num_classes = len(classes)

    # --- 2. Initialize Model, Optimizer, and Loss Function ---
    model = DeeperCNN(num_classes=num_classes)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    # --- 3. Train and Validate the Model ---
    print("Training Deeper CNN...")
    history = train_and_validate(
        model=model,
        optimizer=optimizer,
        criterion=criterion,
        num_epochs=15,
        train_loader=train_loader,
        val_loader=val_loader,
        num_classes=num_classes
    )

    # --- 4. Plot Training History ---
    plot_history(history)

    # --- 5. Evaluate the Final Model ---
    print("\nEvaluating final model on the test set...")
    evaluate_model(model, test_loader, classes)

if __name__ == '__main__':
    main()
