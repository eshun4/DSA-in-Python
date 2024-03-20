def recursiveBinarySearch(array, target, low, high):
    pivot = (low + high) // 2
    if low > high:
        return "Not found"
    if array[pivot] == target:
        return pivot
    if array[pivot] != target and array[pivot] > target:
        return recursiveBinarySearch(array, target, low, pivot - 1 )
    if array[pivot] < target:
        return recursiveBinarySearch(array, target, pivot + 1, high)


print(recursiveBinarySearch([2,4,6,8,10,12,24,35,56], 4, 0, 8 ))
print(recursiveBinarySearch([2,4,6,8,10,12,24,35,56], 6, 0, 8))
print(recursiveBinarySearch([2,4,6,8,10,12,24,35,56], 8, 0, 8))
print(recursiveBinarySearch([2,4,6,8,10,12,24,35,56], 10, 0, 8))
print(recursiveBinarySearch([2,4,6,8,10,12,24,35,56], 12, 0, 8))
print(recursiveBinarySearch([2,4,6,8,10,12,24,35,56], 35, 0, 8))
print(recursiveBinarySearch([2,4,6,8,10,12,24,35,56], 1000, 0, 8))