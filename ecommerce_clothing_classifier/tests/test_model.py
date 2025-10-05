
import pytest
import torch
from ecommerce_clothing_classifier.src.model import BaselineCNN, DeeperCNN

@pytest.fixture(scope="module")
def models():
    """
    Pytest fixture to provide instances of both CNN models for testing.
    
    This fixture is scoped to the module, so the models are instantiated only
    once per test file. It returns a tuple containing an instance of
    BaselineCNN and DeeperCNN.
    """
    baseline_model = BaselineCNN(num_classes=10)
    deeper_model = DeeperCNN(num_classes=10)
    return baseline_model, deeper_model

def test_model_instantiation(models):
    """
    Tests if the BaselineCNN and DeeperCNN models can be instantiated correctly.
    
    This is a fundamental check to ensure that the model's __init__ method
    is syntactically correct and that the model objects can be created without error.
    """
    baseline_model, deeper_model = models
    assert isinstance(baseline_model, BaselineCNN)
    assert isinstance(deeper_model, DeeperCNN)

def test_forward_pass(models):
    """
    Tests the forward pass for both models using a dummy input tensor.
    
    This is a critical test that verifies the integrity of the model's architecture.
    It ensures that an input tensor of the correct shape can pass through all
    the layers of the network and produce an output tensor with the expected
    shape (batch_size, num_classes).
    """
    baseline_model, deeper_model = models
    
    # Create a dummy input tensor with a batch size of 64
    dummy_input = torch.randn(64, 1, 28, 28)
    
    # Test BaselineCNN
    output_baseline = baseline_model(dummy_input)
    assert output_baseline.shape == (64, 10)
    
    # Test DeeperCNN
    output_deeper = deeper_model(dummy_input)
    assert output_deeper.shape == (64, 10)

def test_model_parameters_device(models):
    """
    Checks if the model parameters are on the correct device (CPU by default).
    
    This test also verifies that the model can be successfully moved to a CUDA
    device if one is available. It's important for ensuring that the model
    can be trained on different hardware configurations.
    """
    baseline_model, deeper_model = models
    
    for model in [baseline_model, deeper_model]:
        for param in model.parameters():
            assert param.device.type == 'cpu'

    if torch.cuda.is_available():
        device = torch.device("cuda")
        for model in [baseline_model, deeper_model]:
            model.to(device)
            for param in model.parameters():
                assert param.device.type == 'cuda'
