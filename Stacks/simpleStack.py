
class Stack(object):
    def __init__(self, maximum):
        self.__stackList = [None] * maximum #Initializes an empty stack to a specific max size
        self.__top = -1 #Keeps track of the length of the stack
        
    def push(self, val):
        self.__top += 1 #Increase stack by 1
        self.__stackList[self.__top] = val #Set the topmost value of stack to val
    
    def pop(self):
        top = self.__stackList[self.__top] #Store topmost value of stack into temporary variable
        self.__stackList[self.__top] = None  #Set topmost value in stack to None
        self.__top -= 1
        return top #Return temporary top variable
    
    def peek(self):
        if not self.isEmpty(): #Check if the stack is empty
            return self.__stackList[self.__top] #Return the topmost element of the stack
        
    def isEmpty(self):
        return self.__top < 0 #Check if the topmost value is less than zero then the stack is empty
    
    def isFull(self):
        return self.__top >= len(self.__stackList) - 1 #Check if the topmost value is greater than or equal to the length of the stack then its full
        
    def __len__(self):
        return self.__top + 1 #Return the length of the stacklist
    
    def __str__(self): #Converts the stack into a string
        ans = '['
        for i in range(self.__top + 1):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__stackList[i])
        ans += "]"
        return ans
    
    
if __name__ == "__main__":
    stack = Stack(10)
    
    for word in ['May', 'the', 'force', 'be', 'with', 'you']:
        stack.push(word)
        
    print("After pushing", len(stack), 'words on the stack, it contains:\n', stack)
    print('Is stack full?', stack.isFull())
    
    print('Popping items on the stack: ')
    while not stack.isEmpty():
        print(stack.pop(), end=' ')
    print()
        