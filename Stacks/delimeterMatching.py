""" This program uses the Simple Stack to check if the delimeters being passed match. If
It will parenthesis in this case.
"""

from simpleStack import * 

stack = Stack(100)

expr = input(str('Enter Expression to check: '))

errors = 0 

for pos, letter in enumerate(expr):
    if letter in "{[(":
        if stack.isFull():
            raise Exception("Stack overflow on expression")
        else:
            stack.push(letter)
            
    elif letter in '}])':
        if stack.isEmpty():
            print("Error:", letter, "at position", pos, 'has no matching left delimiter')
            errors += 1 
        else:
            left = stack.pop()
            if not (left == '{' and letter == '}' 
                    or left == '[' and letter == ']' 
                    or left == '(' and letter == ')'):
                print("Error: ", letter, "at position", pos, 'does not match left delimeter', left)
                errors += 1
        
# After going through the entire expression, check if the stack is empty
if stack.isEmpty() and errors == 0:
    print("Delimeters balance in expression", expr)
    
elif not stack.isEmpty():
    print("Expression missing right delimiters for", stack)
                
                
        
