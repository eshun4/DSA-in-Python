"""
    This method returns the sum of the an array.
    First method uses the iterative version, the second method uses the recursive method,
    and the last function uses the recursive method with memoizathion.
"""

def sumOfArrayIterative(array):
    total = 0  # To keep track of the total
    for i in range(len(array)):  # Loop through each element
        total += array[i]  # Add each val in array to total
    return total  # return the total sum

def sumOfArrayRecursive(array, index=0):
    if not array:
        return None
    if index < 0:  # Corrected this condition
        return 0  # Return 0 when index goes below 0
    return array[index] + sumOfArrayRecursive(array, index - 1)

def sumOfArrayRecursiveWIthMemo(array, index=None, memo=None):
    if not array:
        return None
    if index is None:
        index = len(array) - 1
    if memo is None:
        memo = {}
    if index < 0:
        return 0  # Return 0 when index goes below 0
    if index in memo:
        return memo[index]
    else:
        memo[index] = array[index] + sumOfArrayRecursiveWIthMemo(array, index - 1, memo)
    return memo[index]


if __name__ == "__main__":
    # Test case 1: Empty array
    array = []
    print(sumOfArrayIterative(array) == 0)  # Expected: True
    print(sumOfArrayRecursive(array) is None)  # Expected: True
    print(sumOfArrayRecursiveWIthMemo(array) is None)  # Expected: True
    print("")

    # Test case 2: Array with one element
    array = [5]
    print(sumOfArrayIterative(array) == 5)  # Expected: True
    print(sumOfArrayRecursive(array) == 5)  # Expected: True
    print(sumOfArrayRecursiveWIthMemo(array) == 5)  # Expected: True
    print("")

    # Test case 3: Array with multiple elements
    array = [1, 2, 3, 4, 5]
    print(sumOfArrayIterative(array) == 15)  # Expected: True
    print(sumOfArrayRecursive(array, len(array) - 1) == 15)  # Expected: True
    print(sumOfArrayRecursiveWIthMemo(array, len(array) - 1) == 15)  # Expected: True

