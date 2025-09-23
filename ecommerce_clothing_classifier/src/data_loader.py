import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split

def get_data_loaders(batch_size=64):
    """
    Prepares and returns the training, validation, and test DataLoaders for the FashionMNIST dataset.
    """
    # Define a transform to normalize the data
    transform = transforms.ToTensor()

    # Download and load the training data
    full_train_data = datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)

    # Split training data into training and validation sets
    train_size = int(0.8 * len(full_train_data))
    val_size = len(full_train_data) - train_size
    train_data, val_data = random_split(full_train_data, [train_size, val_size])

    # Download and load the test data
    test_data = datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)

    print(f"Number of training examples: {len(train_data)}")
    print(f"Number of validation examples: {len(val_data)}")
    print(f"Number of testing examples: {len(test_data)}")

    # Create DataLoaders
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
    
    return train_loader, val_loader, test_loader, full_train_data.classes
