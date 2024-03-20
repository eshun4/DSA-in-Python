def binarySearch(array, target):
    low = 0
    high = len(array) - 1 
    while low <= high:
        pivot = (low + high) // 2 
        if array[pivot] == target:
            return pivot
        if array[pivot] != target and array[pivot] > target:
            high = pivot - 1
        if array[pivot] < target:
            low = pivot + 1
    return -1

print(binarySearch([2,4,6,8,10,12,24,35,56], 4))
print(binarySearch([2,4,6,8,10,12,24,35,56], 6))
print(binarySearch([2,4,6,8,10,12,24,35,56], 8))
print(binarySearch([2,4,6,8,10,12,24,35,56], 10))
print(binarySearch([2,4,6,8,10,12,24,35,56], 12))
print(binarySearch([2,4,6,8,10,12,24,35,56], 35))
print(binarySearch([2,4,6,8,10,12,24,35,56], 1000))
