
import pytest
import torch
from torch.utils.data import DataLoader
from ecommerce_clothing_classifier.src.data_loader import get_data_loaders

@pytest.fixture(scope="module")
def data_loaders():
    """
    Pytest fixture to provide data loaders for the tests.
    
    This fixture is scoped to the module, meaning it runs once per test file.
    It calls the get_data_loaders function to prepare the FashionMNIST dataset
    and returns the train, validation, and test loaders, along with class names.
    """
    return get_data_loaders(batch_size=32)

def test_data_loaders_types(data_loaders):
    """
    Tests if the get_data_loaders function returns objects of the correct type.
    
    It's a basic sanity check to ensure that the data loaders are indeed
    instances of PyTorch's DataLoader class, which is essential for their
    functionality in training and evaluation loops.
    """
    train_loader, val_loader, test_loader, _ = data_loaders
    assert isinstance(train_loader, DataLoader)
    assert isinstance(val_loader, DataLoader)
    assert isinstance(test_loader, DataLoader)

def test_data_batch_shape_and_type(data_loaders):
    """
    Tests the shape, batch size, and data type of a single batch from the train_loader.
    
    This test verifies several critical properties of the data pipeline:
    - The batch size matches the expected value.
    - The image tensors have the correct dimensions (1 channel, 28x28 pixels).
    - The image data is of type float32, and labels are int64, as expected by PyTorch.
    """
    train_loader, _, _, _ = data_loaders
    images, labels = next(iter(train_loader))
    
    # Check batch size and image dimensions
    assert images.shape[0] == 32
    assert images.shape[1] == 1
    assert images.shape[2] == 28
    assert images.shape[3] == 28
    
    # Check tensor types
    assert images.dtype == torch.float32
    assert labels.dtype == torch.int64

def test_data_normalization(data_loaders):
    """
    Tests if the image data is properly normalized to the [0, 1] range.
    
    Normalization is a crucial preprocessing step for neural networks. This test
    fetches a batch of images and asserts that all pixel values fall within
    the expected 0 to 1 range, confirming that the ToTensor transform was applied.
    """
    train_loader, _, _, _ = data_loaders
    images, _ = next(iter(train_loader))
    
    # Check if all values are within the [0, 1] range
    assert torch.all(images >= 0) and torch.all(images <= 1)

def test_class_names(data_loaders):
    """
    Tests if the class names are returned correctly.
    
    This test ensures that the data loader function also provides the list of
    class names for the dataset. It verifies that the list contains 10 string
    elements, corresponding to the 10 classes of FashionMNIST.
    """
    _, _, _, class_names = data_loaders
    assert isinstance(class_names, list)
    assert len(class_names) == 10
    assert all(isinstance(name, str) for name in class_names)
