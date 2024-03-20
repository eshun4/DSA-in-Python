import math

def binarySearchAlt(array, target):
    """ This is another implementation of Binary Search. In the above procedure, the algorithm checks whether the middle element 
    is equal to the target in every iteration. Some implementations leave out this check during each iteration. 
    The algorithm would perform this check only when one element is left. This results in a faster comparison loop, as one comparison 
    is eliminated per iteration, while it requires only one more iteration on average."""
    low, high = 0, len(array) - 1
    while low != high:
        pivot = math.ceil(low + high / 2)
        if array[pivot] != target and array[pivot] > target:
            high = pivot - 1
        else:
            low = pivot
    if array[low] == target:
        return low
    return -1

if __name__ == "__main__":
    binarySearch = binarySearchAlt([2,4,6,8,10,12,24,35,56], 5)
    print(binarySearch)