def binarySearchLeftMost(array, target):
    """  It is sometimes necessary to find the leftmost element or the rightmost element for a target value that is duplicated in the array."""
    low, high = 0, len(array) - 1
    while low < high:
        pivot = (low + high) // 2
        if array[pivot] != target and array[pivot] < target:
            low = pivot + 1 
        else:
            high = pivot 
    return low

def binarySearchRightMost(array, target):
    """  It is sometimes necessary to find the leftmost element or the rightmost element for a target value that is duplicated in the array."""
    low, high = 0, len(array) - 1
    while low < high:
        pivot = (low + high) // 2
        if array[pivot] != target and array[pivot] > target:
            high = pivot
        else:
            low = pivot + 1
    return high - 1

if __name__ == "__main__":
    binarySearch = binarySearchLeftMost([2,4,6,8,10,10,12,24,35,56], 10)
    print(binarySearch)
    binarySearch2 = binarySearchRightMost([2,4,6,8,10,10,12,24,35,56], 10)
    print(binarySearch2)
            
            