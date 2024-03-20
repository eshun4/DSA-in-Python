class BinarySearch(object):
    """ This is a Binary Search algorithm that runs in O(log n) time. This is because
    in iterating the array, it divides the array into 2 in each iteration."""
    
    def __init__(self, array, target):
        self._array = array
        self._target = target
        
    def binarySearch(self):
        low = 0 
        high = len(self._array) - 1 
        while low <= high:
            pivot = (low + high) // 2
            if self._array[pivot] == self._target:
                return pivot
            if self._array[pivot] != self._target and self._array[pivot] > self._target:
                high = pivot - 1 
            if self._array[pivot] < self._target:
                low = pivot + 1 
        return - 1
    
if __name__ == "__main__":
    binarySearch = BinarySearch([2,4,6,8,10,12,24,35,56], 4)
    print(binarySearch.binarySearch())
                