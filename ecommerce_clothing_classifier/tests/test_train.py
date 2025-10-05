
import pytest
import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from ecommerce_clothing_classifier.src.train import train_and_validate
from ecommerce_clothing_classifier.src.model import BaselineCNN

@pytest.fixture
def dummy_data():
    """Creates dummy data for training and validation."""
    # Dummy data: 100 samples, 1 channel, 28x28 images
    X_train = torch.randn(100, 1, 28, 28)
    y_train = torch.randint(0, 10, (100,))
    X_val = torch.randn(50, 1, 28, 28)
    y_val = torch.randint(0, 10, (50,))
    
    train_dataset = TensorDataset(X_train, y_train)
    val_dataset = TensorDataset(X_val, y_val)
    
    train_loader = DataLoader(train_dataset, batch_size=10)
    val_loader = DataLoader(val_dataset, batch_size=10)
    
    return train_loader, val_loader

def test_training_loop_runs(dummy_data):
    """
    Tests if the training and validation loop runs without errors for one epoch.
    
    This is a basic integration test to ensure that the training function can
    execute a full training and validation cycle. It uses a dummy model and
    data loaders.
    """
    model = BaselineCNN(num_classes=10)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()
    train_loader, val_loader = dummy_data
    
    history = train_and_validate(model, optimizer, criterion, 1, train_loader, val_loader, 10)
    
    assert 'train_loss' in history
    assert 'val_loss' in history
    assert len(history['train_loss']) == 1

def test_model_weights_change(dummy_data):
    """
    Tests if the model's weights change after one training epoch.
    
    This test verifies that the optimizer is correctly updating the model's
    parameters during training. It checks this by comparing the state of a
    model parameter before and after a training cycle.
    """
    model = BaselineCNN(num_classes=10)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()
    train_loader, val_loader = dummy_data
    
    # Copy initial weights
    initial_weights = model.conv1.weight.clone()
    
    train_and_validate(model, optimizer, criterion, 1, train_loader, val_loader, 10)
    
    # Check if weights have changed
    assert not torch.equal(initial_weights, model.conv1.weight)

def test_history_object(dummy_data):
    """
    Tests if the history object is returned correctly.
    
    The history object is crucial for monitoring the model's performance.
    This test ensures that it contains the correct keys and that the number
    of entries matches the number of epochs.
    """
    model = BaselineCNN(num_classes=10)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    criterion = nn.CrossEntropyLoss()
    train_loader, val_loader = dummy_data
    
    history = train_and_validate(model, optimizer, criterion, 3, train_loader, val_loader, 10)
    
    assert 'train_loss' in history
    assert 'train_acc' in history
    assert 'val_loss' in history
    assert 'val_acc' in history
    assert len(history['train_loss']) == 3
    assert len(history['val_acc']) == 3
