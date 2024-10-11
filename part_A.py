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

    # Compute mean
    mean = 0.0
    for i, xi in enumerate(x):
        mean += xi

        # Check if item is the last in the list. 
        # This is done by trying to access the next item in the list.
        try:
            x[i+1]
        except IndexError:
            N = i + 1
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

    return



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

    num_lst = [1,2,3,4,5]

    x = num_lst
    
    N = len(x)
    # Compute mean
    mean = sum(x) / N

    # Compute the mean of squares
    S = sum(map(lambda xi: xi**2, x)) / N

    # Compute variance
    var = S - mean**2.0

    # Compute standard deviation
    sd = sqrt(var)

    print(f'Standard deviation: {sd:.8f}')

    return


# List of 5 integers
num_lst=[int(1),int(2),int(3),int(4),int(5)]

# Print results
std_loops(num_lst)
std_builtin(num_lst)
print(f'Standard deviation: {np.std(num_lst):.8f}')
