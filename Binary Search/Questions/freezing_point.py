"""
Problem: Freezing Point

You are a scientist working in a lab that develops new substances. You have developed a new substance and you want to find out at what temperature this substance freezes under a certain pressure. You have a device that can measure whether the substance is liquid or solid (i.e., whether it has frozen) at a given temperature.

Write a function:

find_freezing_point(is_solid, low, high, tol)  to find the freezing point of the substance.

Input:

is_solid: A function that takes a temperature as input and returns True if the substance is solid at that temperature, and False otherwise.
low, high: Two floats representing the lower and upper bounds of the temperature range within which the freezing point lies.
tol: A float representing the tolerance for the binary search. The function should stop when the size of the search interval is less than or equal to tol. The default value of tol is 1e-6.
Output:

Return a float representing the freezing point of the substance.

Constraints:

The function is_solid will always be such that there is a temperature t in the range [low, high] where is_solid(t) is True and is_solid(t + epsilon) is False for any epsilon > 0.
-100 <= low < high <= 100
tol will be a positive number.

"""

from typing import Callable

def find_freezing_point(is_solid: Callable[[float], bool], low: float, high: float, tol: float = 1e-6) -> float:
    while high - low > tol:
        midpoint = (high + low) / 2
        if is_solid(midpoint):
            low = midpoint
        else:
            high = midpoint
    return low 
            


# Test case 1: Substance freezes at -20 degrees Celsius
def is_solid_1(temperature):
    return temperature <= -20

print(find_freezing_point(is_solid_1, -100, 100))  # Output: -20.0

# Test case 3: Substance freezes at -50 degrees Celsius
def is_solid_3(temperature):
    return temperature <= -50

print(find_freezing_point(is_solid_3, -100, 100))  # Output: -50.0

# Test case 4: Substance freezes at 0 degrees Celsius, but search range is different
def is_solid_4(temperature):
    return temperature <= 0

print(find_freezing_point(is_solid_4, -50, 50))  # Output: 0.0
