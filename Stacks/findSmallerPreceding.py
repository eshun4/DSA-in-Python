"""
    This function return the smaller preceeding number before a given number in an array.
"""


def smallerPreceedingElement(numbers):
    result = [-1]
    stack = []
    for num in numbers:
        while stack and stack[-1] >= num:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(num)
    return result[1:]


if __name__ == "__main__":
    print(smallerPreceedingElement([4, 5, 2, 10, 8]))  # Expected output: [-1, 4, -1, 2, 2]
    print(smallerPreceedingElement([1, 3, 0, 2, 5]))  # Expected output: [-1, 1, -1, 0, 2]
    print(smallerPreceedingElement([]))  # Expected output: []
    print(smallerPreceedingElement([7]))  # Expected output: [-1]
    print(smallerPreceedingElement([9, 7, 5, 3, 1]))  # Expected output: [-1, -1, -1, -1, -1]
