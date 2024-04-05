class Stack(object):
    
    def __init__(self):
        self.array =  []
        
    def isEmpty(self):
        return len(self.array)
    
    def pop(self):
        if self.isEmpty() == 0:
            return - 1 
        else:
            return self.array.pop()
    
    def push(self, val):
        return self.array.append(val)
    
    def getLength(self):
        return len(self.array)
    
    
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
    
    
        