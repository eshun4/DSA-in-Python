"""
    This is an implementation of a maxstack.
    It keeps track of the maximum element in the stack.
"""


class MaxStack(object):
    
    def __init__(self):
        self.mainStack = []
        self.maxStack = []
        
    def push(self, x):
        self.mainStack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)
            
    def pop(self):
        if self.mainStack:
            top = self.mainStack.pop()
            if self.maxStack and top == self.maxStack[-1]:
                self.maxStack.pop()

                
    def top(self):
        """Return the topmost element in the main stack."""
        if self.mainStack:
            return self.mainStack[-1]
            
    def getMax(self):
        if self.maxStack:
            return self.maxStack[-1]
            

if __name__ == "__main__":
    maxStack = MaxStack()
    maxStack.push(2)
    maxStack.push(0)
    maxStack.push(3)
    print(maxStack.getMax())  # Expected output: 3
    maxStack.pop()
    print(maxStack.top())  # Expected output: 0
    print(maxStack.getMax())  # Expected output: 2

    # Test with an empty stack
    emptyStack = MaxStack()
    print(emptyStack.top())  # Expected output: None
    print(emptyStack.getMax())  # Expected output: None
    emptyStack.pop()  # Does nothing

