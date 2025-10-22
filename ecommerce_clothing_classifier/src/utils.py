import random
import numpy as np
import torch

def set_seed(seed):
    """
    Set seed for reproducibility across different hardware.
    
    Args:
        seed (int): The seed value.
    """
    # Set seed for general randomness
    random.seed(seed)
    np.random.seed(seed)
    
    # Set seed for PyTorch on CPU and GPU
    torch.manual_seed(seed)
    
    if torch.cuda.is_available():
        # Set seed for CUDA specifically
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)  # if you are using multi-GPU
        
        # Configure CuDNN for deterministic behavior
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
