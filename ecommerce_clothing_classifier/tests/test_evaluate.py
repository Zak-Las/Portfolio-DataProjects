
import pytest
import torch
from torch.utils.data import TensorDataset, DataLoader
from ecommerce_clothing_classifier.src.evaluate import evaluate_model
from ecommerce_clothing_classifier.src.model import BaselineCNN

@pytest.fixture
def dummy_test_data():
    """Creates dummy data for evaluation."""
    X_test = torch.randn(100, 1, 28, 28)
    y_test = torch.randint(0, 10, (100,))
    
    test_dataset = TensorDataset(X_test, y_test)
    test_loader = DataLoader(test_dataset, batch_size=10)
    
    classes = [f"Class_{i}" for i in range(10)]
    
    return test_loader, classes

def test_evaluate_model_runs(dummy_test_data):
    """
    Tests if the evaluation function runs without errors.
    
    This is a basic integration test to ensure that the evaluate_model function
    can execute completely. It uses a dummy model and test data.
    """
    model = BaselineCNN(num_classes=10)
    test_loader, classes = dummy_test_data
    
    # This will raise an error if something is wrong
    evaluate_model(model, test_loader, classes)

def test_evaluate_model_output_types_and_shapes(dummy_test_data):
    """
    Tests the types and shapes of the outputs from the evaluation function.
    
    This test verifies that the function returns metrics in the expected format:
    - Accuracy should be a float.
    - Precision and recall should be lists with a length equal to the number of classes.
    - The lists of all predictions and labels should have the correct length.
    """
    model = BaselineCNN(num_classes=10)
    test_loader, classes = dummy_test_data
    
    accuracy, precision, recall, all_labels, all_preds = evaluate_model(model, test_loader, classes)
    
    assert isinstance(accuracy, float)
    assert isinstance(precision, list)
    assert isinstance(recall, list)
    assert len(precision) == 10
    assert len(recall) == 10
    assert len(all_labels) == 100
    assert len(all_preds) == 100

def test_metrics_calculation(dummy_test_data):
    """
    Tests the metric calculations with predictable data.
    
    This test uses a model that always predicts class 0. This allows us to
    verify that the accuracy, precision, and recall are calculated correctly.
    """
    # A model that always predicts class 0
    class MockModel(torch.nn.Module):
        def forward(self, x):
            # Return high score for class 0, low for others
            output = torch.full((x.shape[0], 10), -1.0)
            output[:, 0] = 1.0
            return output

    model = MockModel()
    test_loader, classes = dummy_test_data
    
    # Get the actual labels from the dummy data
    true_labels = []
    for _, labels in test_loader:
        true_labels.extend(labels.tolist())
    
    num_class_0 = sum(1 for label in true_labels if label == 0)
    
    accuracy, precision, recall, _, _ = evaluate_model(model, test_loader, classes)
    
    # Expected accuracy is the proportion of class 0
    expected_accuracy = num_class_0 / len(true_labels)
    assert pytest.approx(accuracy, 0.01) == expected_accuracy
    
    # Expected recall for class 0 is 1.0, as all class 0 instances are found
    assert pytest.approx(recall[0], 0.01) == 1.0
    
    # Expected precision for class 0 is the proportion of class 0
    expected_precision_0 = num_class_0 / len(true_labels)
    assert pytest.approx(precision[0], 0.01) == expected_precision_0
    
    # For other classes, precision and recall should be 0
    for i in range(1, 10):
        assert precision[i] == 0.0
        assert recall[i] == 0.0
