from collections import deque

class Stack(object):
    """ This is an implementation of a Stack class with a deque from the collections module. The
    It has time complexity of O(1) for pop and push operations and a space complexity of O(n) for the same operations."""
    
    def __init__(self):
        self.array = deque()
        
    def isEmpty(self):
        return len(self.array)
    
    def push(self, val):
        return self.array.append(val)
    
    def pop(self):
        if self.isEmpty() == 0:
            return -1
        else:
            return self.array.pop()
    
    def peek(self):
        if self.isEmpty() == 0:
            return -1
        else:
            return self.array[-1]
    
    def getLength(self):
        if self.isEmpty() == 0:
            return -1 
        else:
            return self.isEmpty()
    
    def maxStack(self):
        if self.isEmpty() == 0:
            return -1
        else:
            return max(self.array)
        
    def minStack(self):
        if self.isEmpty() == 0:
            return - 1 
        else:
            return min(self.array)
        
if __name__ == "__main__":
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)
    stack.push(10)
    
    print(stack.array)
    
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    
    print(stack.array)
    print(stack.getLength())
    
    print(stack.peek())
    print(stack.maxStack())
    print(stack.minStack())
        
    