from PostFixTranslate import *
from simpleStack import *


def postFixEvaluate(formula):
    """This function evaluates a postfix expression."""
    
    postfix = PostFixTranslate(formula) #Postfix string
    s = Stack(100) # Operand stack
    
    token, postfix = nextToken(postfix) 
    
    while token:
        prec = precedence(token) #Is it an operator
        
        if prec: #If input token is an operator
            right = s.pop() #Get left and right
            left = s.pop() #operators from the stack
            if token == "|":
                s.push(left | right)
            elif token == '&':
                s.push(left & right)
            elif token == '+':
                s.push(left + right)
            elif token == '-':
                s.push(left - right)
            elif token == '*':
                s.push(left * right)
            elif token == '/':
                s.push(left / right)
            elif token == '%':
                s.push(left % right)
            elif token == '^':
                s.push(left ^ right)
        else:
            s.push(int(token)) #Else token is operand, convert to integer and push
        
        print("After processing", token, 'stack holds', s)
        
        token, postfix = nextToken(postfix) #Fencepost loop
    
    print('Final result =', s.pop())
    
if __name__ == "__main__":
    infix_expre = input("Input expression to evaluate: ")
    print("The postfix representation of", infix_expre, "is", PostFixTranslate(infix_expre))
    postFixEvaluate(infix_expre)
        
        