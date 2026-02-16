import torch
from torchmetrics import Accuracy, Precision, Recall

def evaluate_model(model, test_loader, classes, device):
    model.to(device)
    model.eval()
    
    accuracy_metric = Accuracy(task='multiclass', num_classes=len(classes)).to(device)
    precision_metric = Precision(task='multiclass', num_classes=len(classes), average=None).to(device)
    recall_metric = Recall(task='multiclass', num_classes=len(classes), average=None).to(device)
    
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for features, labels in test_loader:
            features, labels = features.to(device), labels.to(device)
            outputs = model(features)
            _, preds = torch.max(outputs, 1)
            
            accuracy_metric.update(preds, labels)
            precision_metric.update(preds, labels)
            recall_metric.update(preds, labels)
            
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    # Compute final metrics
    accuracy = accuracy_metric.compute().item()
    precision = precision_metric.compute().tolist()
    recall = recall_metric.compute().tolist()
    
    print(f'Overall Test Accuracy: {accuracy:.4f}\n')
    
    print("Per-Class Precision and Recall:")
    for i, class_name in enumerate(classes):
        print(f"{class_name:<12}: Precision={precision[i]:.4f}, Recall={recall[i]:.4f}")

    return accuracy, precision, recall, all_labels, all_preds
