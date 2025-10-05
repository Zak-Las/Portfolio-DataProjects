import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split, Subset

def get_data_loaders(batch_size=64):
    """
    Prepares and returns the training, validation, and test DataLoaders for the FashionMNIST dataset.
    """
    # Define transforms for training (with augmentation) and for validation/testing (without)
    train_transform = transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ToTensor()
    ])
    
    test_transform = transforms.ToTensor()

    # Download and load the training data
    # We don't apply the transform immediately, as we need to split it first
    full_train_data = datasets.FashionMNIST(root='./data', train=True, download=True, transform=None)
    
    # The test data should use the test_transform
    test_data = datasets.FashionMNIST(root='./data', train=False, download=True, transform=test_transform)

    # Split training data into training and validation sets
    train_size = int(0.8 * len(full_train_data))
    val_size = len(full_train_data) - train_size
    # random_split returns Subset objects
    train_data, val_data = random_split(full_train_data, [train_size, val_size])

    # Apply the correct transforms to the training and validation subsets
    train_data.dataset.transform = train_transform
    val_data.dataset.transform = test_transform

    print(f"Number of training examples: {len(train_data)}")
    print(f"Number of validation examples: {len(val_data)}")
    print(f"Number of testing examples: {len(test_data)}")

    # Create DataLoaders
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
    
    return train_loader, val_loader, test_loader, full_train_data.classes
