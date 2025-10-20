import matplotlib.pyplot as plt
import numpy as np

def show_random_samples(loader, loader_name, classes):
    """
    Displays a grid of 10 random image samples from a given data loader.

    This function fetches a single batch from the loader, selects 10 random
    samples from that batch, and plots them in a 2x5 grid. It also prints
    the dimensions of the images in the loader.

    Args:
        loader (torch.utils.data.DataLoader): The data loader to sample from.
        loader_name (str): The name of the data loader (e.g., "Training Set"),
                           used for the plot title.
        classes (list of str): A list of class names corresponding to the
                               label indices.

    Examples:
        >>> train_loader, val_loader, test_loader, classes = get_data_loaders(batch_size=64)
        >>> show_random_samples(train_loader, 'Training Set', classes)
        >>> show_random_samples(val_loader, 'Validation Set', classes)
        >>> show_random_samples(test_loader, 'Test Set', classes)
    """
    # Get a single batch of data
    images, labels = next(iter(loader))
    
    # Get image size from the first image in the batch
    # The shape will be [batch_size, channels, height, width]
    # So, image_size will be (height, width)
    image_size = images[0].shape[1:]
    print(f"Image size for {loader_name}: {image_size[0]}x{image_size[1]} pixels")

    plt.figure(figsize=(15, 5))
    plt.suptitle(f'10 Random Samples from {loader_name}', fontsize=16)
    
    # Get 10 random indices from the batch
    num_samples_to_show = 10
    if len(images) < num_samples_to_show:
        num_samples_to_show = len(images)
        
    random_indices = np.random.choice(len(images), num_samples_to_show, replace=False)
    
    for i, idx in enumerate(random_indices):
        image = images[idx]
        label_index = labels[idx]
        
        plt.subplot(2, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(image.squeeze(), cmap=plt.cm.binary)
        plt.xlabel(classes[label_index])
        
    plt.show()

def plot_history(history, save_path=None):
    """
    Plots the training and validation loss and accuracy from the history dictionary.

    Args:
        history (dict): A dictionary containing the training history. 
                        It is the output of the `train_and_validate` function 
                        in `train.py` and is expected to have the following structure:
                        {
                            'train_loss': [...],
                            'train_acc': [...],
                            'val_loss': [...],
                            'val_acc': [...]
                        }
        save_path (str, optional): If provided, the plot will be saved to this path.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    ax1.plot(history['train_loss'], label='Train Loss')
    ax1.plot(history['val_loss'], label='Validation Loss')
    ax1.set_title('Loss Over Epochs')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Loss')
    ax1.legend()
    
    ax2.plot(history['train_acc'], label='Train Accuracy')
    ax2.plot(history['val_acc'], label='Validation Accuracy')
    ax2.set_title('Accuracy Over Epochs')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Accuracy')
    ax2.legend()
    
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
        
    plt.show()
