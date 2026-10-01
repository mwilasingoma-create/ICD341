import numpy as np

def calculate_statistics(x):
    total = np.sum(x)
    mean = np.mean(x)
    variance = np.var(x)
    result = np.sqrt(variance)
    return total, mean, result