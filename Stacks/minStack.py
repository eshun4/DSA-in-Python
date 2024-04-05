"""This is a MinStack implementation.

MinStack Implementation Steps:

1. Initialize Two Stacks: One for 
storing the actual stack elements 
(mainStack) and the other for keeping
track of the minimum elements (minStack).

2. Push Operation: When pushing an element 
onto the mainStack, also decide whether to
push it onto the minStack.
If the minStack is empty or the new element
is less than or equal to the top element of
the minStack, push it onto the minStack as well.

3. Pop Operation: When popping an element
from the mainStack,
if the popped element is the same as the top
element of the minStack, pop it from the minStack
as well. This keeps the minStack aligned with
the current minimum of the remaining elements.

4. Top Operation: 
To fetch the top element of
the mainStack without removing it.

5. GetMin Operation: The top element
of the minStack represents the current
minimum element of the mainStack.

Explanation:
Push Logic: By pushing elements onto the 
minStack only when they are less than or
equal to the current minimum, you are effectively 
tracking the minimum for the current state of the
mainStack. This is akin to identifying a 
“preceding smaller element”, but applied
here to maintain a running minimum.

Pop Logic: Popping from the minStack in sync 
with the mainStack ensures that the minStack 
always reflects the minimum of the mainStack's 
current state.

This approach efficiently extends the idea of 
tracking preceding smaller elements (or relevant 
elements for some condition) to implementing a 
MinStack, where the condition is maintaining the
global minimum for the stack's current state. 
The minStack effectively remembers the minimum
element for each level of the mainStack, similar
to how you remember preceding smaller elements, 
but tailored here for a cumulative property (the 
global minimum) rather than a relational property
(previous smaller element for each entry).
"""


class MinStack:
    def __init__(self):
        self.mainStack = []
        self.minStack = []
    
    def push(self, x):
        self.mainStack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
            
    def pop(self):
        if self.mainStack:
            top = self.mainStack.pop()
            if top == self.minStack[-1]:
                self.minStack.pop()
    
    def top(self):
        if self.mainStack:
            return self.mainStack[-1]
        
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        
if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # Returns -3
    minStack.pop()
    print(minStack.top())  # Returns 0
    print(minStack.getMin())  # Returns -2

    # Test with an empty stack
    emptyStack = MinStack()
    print(emptyStack.top())  # Returns None
    print(emptyStack.getMin())  # Returns None
    emptyStack.pop()  # Does nothing
