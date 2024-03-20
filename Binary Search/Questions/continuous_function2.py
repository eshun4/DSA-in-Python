# Python program to find the value of 'x' when f(x) = 0 using Binary Search
import math
import numpy as np

# Define a continuous function 'f' where f(x) = x^6 - 3x^4 + 4x^3 - 1
def f(x):
    return x**6 - 3 * x**4 + 4 * x**3 - 1

# Binary Search Function
def binary_search(func, target, left, right, epsilon):
    while right - left > epsilon:
        middle = (left + right) / 2
        if func(middle) > target:
            right = middle
        else:
            left = middle        
    return (left + right) / 2

epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 0  # target f(x) value
start = -5  # starting point of the interval
end = 5  # ending point of the interval

result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 0 is: ", result)