# Python program to find the value of 'x' when f(x) = 0 using Binary Search on Continuous Space
import math

# Define a continuous function 'f'
def f(x):
    return x**3 - 5 * x**2 + 5

# TODO: Write the Binary Search Function that performs the search on the continuous function in the interval [2, 5]
def binarySearchFunction(func, target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        if f(mid) < target:
            right = mid
        else:
            left = mid
    return (left + right) / 2

# TODO: Define precision, target value, and interval bounds
epsilon = 1e-6
target = 0
interval_bounds = [2, 5]
# TODO: Implement the binary search function and print out the value of 'x' for which f(x) is approximately 0.
root = binarySearchFunction(f,target, interval_bounds[0], interval_bounds[1], epsilon)
print(f"The root of the contiunuous function is: {root}")