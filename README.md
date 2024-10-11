# TECH2 mandatory assignment: common mistakes

This repository collects common mistakes made in student submissions 
for the mandatory assignment.

See the git commit history for how these mistakes can be corrected.

## Some hints on how to avoid common mistakes

1.  Don't use spaces in Python file names such as `Part A.py`, it is not possible to import such modules.
2.  Python variable and module names are case sensitive. Something like
    ```python
    import NumPy
    ```
    will not work because such a module most likely does not exist.
3.  Your functions `std_loops()` and `std_builtin()` should have a return value instead of simply printing the result.
    Note that an empty return statement
    ```python
    def std_loops(x):
        return
    ```
    does not do anything if placed at the end of the function, and the function just returns `None` as it would by default.
4.  Don't use exceptions (`try`/`except`) to handle situations that are guaranteed to happen. Use exceptions for cases that you anticipate might happen in some circumstances.
5.  Don't overwrite function arguments with some deterministic value, that undermines the general usefulness of functions. For example,
    ```python
    def std_loops(x):
        x = [1,2, 3, 4, 5]
    ```
    renders the function useless except for the very specific value of `x = [1, 2, 3, 4, 5]`.
6. Wrap directly executable code in a Python module in an `if` block so that it does not get executed each time a module is imported.
    ```python
    if __name__ == '__main__':
        # Print only if module is run directly as a Python script, not when imported
        print('Executed directly')
    ```
7.  Don't use `print()` statements in library functions: your functions `std_loops()` and `std_builtin()` are called in part B thousands of times in the `%timeit` cell magic, you don't want to print thousands of statements to your notebook. 
8.  Restart the kernel and rerun the whole notebook once you are done to make sure that the code actually works!