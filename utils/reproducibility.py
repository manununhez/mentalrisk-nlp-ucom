import random
import numpy as np
import torch

def set_seed(seed: int = 42):
    """
    Fija la semilla en todos los módulos relevantes para asegurar resultados reproducibles.

    Parámetros:
    - seed (int): valor de la semilla a fijar. Por defecto, 42.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
