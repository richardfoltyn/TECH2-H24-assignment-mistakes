from math import sqrt 

# MISTAKE: 
# import NumPy as np
import numpy as np

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    N = 0

    # Compute mean
    mean = 0.0
    for i, xi in enumerate(x):
        mean += xi
        N += 1
    mean /= N

    # Compute the mean of squares
    S = 0.0
    for xi in x:
        S += xi**2.0
    S /= N

    # Compute variance
    var = S - mean**2.0

    # Compute standard deviation
    sd = sqrt(var)

    print(f'Standard deviation: {sd:.8f}')

    return sd



def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """

    # MISTAKE: Don't overwrite function argument with some fixed value
    # num_lst = [1,2,3,4,5]
    # x = num_lst
    
    N = len(x)
    # Compute mean
    mean = sum(x) / N

    # Compute the mean of squares
    # UNNECESSARY:
    # S = sum(map(lambda xi: xi**2, x)) / N
    # The built-in sum can directly iterate over arguments, no map() needed:
    S = sum(xi**2 for xi in x) / N

    # Compute variance
    var = S - mean**2.0

    # Compute standard deviation
    sd = sqrt(var)

    print(f'Standard deviation: {sd:.8f}')

    return sd


# List of 5 integers
# UNNECESSARY:
# num_lst=[int(1),int(2),int(3),int(4),int(5)]
# Integer literals 1, 2, 3,.. are already integers
num_lst = [1, 2, 3, 4, 5]

# Print results
std_loops(num_lst)
std_builtin(num_lst)
print(f'Standard deviation: {np.std(num_lst):.8f}')
