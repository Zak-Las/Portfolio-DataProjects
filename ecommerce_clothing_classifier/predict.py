import torch
import argparse
from PIL import Image
from torchvision import transforms
from src.model import DeeperCNN

def predict(image_path, model_path):
    """
    Loads a trained model and classifies a single image.
    """
    # Define the same classes as used in training
    classes = [
        'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
        'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
    ]
    num_classes = len(classes)

    # Load the model
    model = DeeperCNN(num_classes=num_classes)
    model.load_state_dict(torch.load(model_path))
    model.eval()

    # Define the image transformation
    # This should match the validation/test transformation
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),
        transforms.Resize((28, 28)),
        transforms.ToTensor()
    ])

    # Load and transform the image
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return

    image = transform(image).unsqueeze(0)  # Add batch dimension

    # Make prediction
    with torch.no_grad():
        output = model(image)
        _, predicted_idx = torch.max(output, 1)
        predicted_class = classes[predicted_idx.item()]

    print(f"The predicted class for the image is: {predicted_class}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Classify a single clothing image.")
    parser.add_argument('--image_path', type=str, required=True, help='Path to the image file.')
    parser.add_argument('--model_path', type=str, default='fashion_mnist_cnn.pth', help='Path to the saved model state dictionary.')
    
    args = parser.parse_args()
    
    predict(args.image_path, args.model_path)
