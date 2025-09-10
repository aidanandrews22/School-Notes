import numpy
import torch

## You only need to complete the two functions .
def numpy_squares ( k ) :
    """ return (1 , 4 , 9 , ... , k^2) as a numpy array """
    return numpy.array([i**2 for i in range(1, k+1)])

def torch_squares ( k ) :
    """ return (1 , 4 , 9 , ... , k^2) as a torch array """
    return torch.tensor([i**2 for i in range(1, k+1)])
    # your code here