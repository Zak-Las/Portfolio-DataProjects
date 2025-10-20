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
        transforms.RandomRotation(20),  # Reduced rotation to be more realistic for clothing
        transforms.RandomAutocontrast(),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)) # Normalize for better performance
    ])
    
    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])

    # Create separate datasets for training and validation with their respective transforms
    train_data = datasets.FashionMNIST(root='./data', train=True, download=True, transform=train_transform)
    val_data = datasets.FashionMNIST(root='./data', train=True, download=True, transform=test_transform)
    
    # The test data should use the test_transform
    test_data = datasets.FashionMNIST(root='./data', train=False, download=True, transform=test_transform)

    # Get indices for splitting the training data
    train_size = int(0.8 * len(train_data))
    val_size = len(train_data) - train_size
    
    # Use a generator for reproducibility of the split
    generator = torch.Generator().manual_seed(42)
    indices = torch.randperm(len(train_data), generator=generator).tolist()
    
    # Create subsets based on the indices
    train_subset = Subset(train_data, indices[:train_size])
    val_subset = Subset(val_data, indices[train_size:])

    print(f"Number of training examples: {len(train_subset)}")
    print(f"Number of validation examples: {len(val_subset)}")
    print(f"Number of testing examples: {len(test_data)}")

    # Create DataLoaders
    train_loader = DataLoader(train_subset, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_subset, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_data, batch_size=batch_size, shuffle=False)
    
    # Get classes from the original dataset object
    classes = train_data.classes
    
    return train_loader, val_loader, test_loader, classes
