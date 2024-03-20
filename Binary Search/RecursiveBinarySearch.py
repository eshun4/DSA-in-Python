class RecursiveBinarySearch(object):
    def __init__(self, array,target):
        self._array = array
        self._target = target 
        self._low = 0
        self._high = len(self._array) - 1
    
    def recursiveBinarySearch(self):
        pivot = (self._low + self._high) // 2
        if self._low > self._high:
            return "Not Found"
        if self._array[pivot] == self._target:
            return pivot
        if self._array[pivot] != self._target and self._array[pivot] > self._target:
            self._high = pivot - 1
            return self.recursiveBinarySearch()
        if self._array[pivot] < self._target:
            self._low = pivot + 1
            return self.recursiveBinarySearch()

if __name__ == '__main__':
    recBinSearch = RecursiveBinarySearch([2,4,6,8,10,12,24,35,56], 8)
    print(recBinSearch.recursiveBinarySearch())
    
# Icomparable in C sharp is an interface used to define how to compare things. 