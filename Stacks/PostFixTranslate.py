# Import necessary modules
import sys
import os
from simpleStack import Stack

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now you can import your module
from Queues.queue import Queue

# Define operators and their precedence. In most cases you can follow PEMDAS
# We group single character operators of equal precedence in strings
# Lowest precedence is on the left; highest on the right
# Parentheses are treated as high precedence operators
operators = ['|', '^', '&', '+-', '*/%', '**', '()']

# Function to get the precedence of an operator
def precedence(operator):
    for p, ops in enumerate(operators):  # Loop through the operators
        if operator in ops:  # If operator passed in this function is in ops
            return p + 1  # Return precedence (low = 1)
    return None  # Not an operator so return none

# Function to check if a character is a delimiter
def delimiter(character):
    return precedence(character) == len(operators)

# Function to parse next token from the input string
def nextToken(s):
    token = ""  # Token is operator or operand
    s = s.strip()  # Remove any leading or trailing spaces
    if len(s) > 0:  # If not end of input
        if precedence(s[0]):  # Check if the first char is an operator
            token = s[0]  # Token is a first char, operator
            s = s[1:].strip()  # Remove leading spaces from remaining string
        else:  # It's an operand so take characters up to next operator or space
            while len(s) > 0 and not (precedence(s[0]) or s[0].isspace()):
                token += s[0]
                s = s[1:]
            s = s.strip()  # Remove leading spaces from remaining string
    return token, s  # Return the token, and remaining input string

# Function to translate infix to postfix
def PostFixTranslate(formula):
    postfix = Queue(100)  # Store postfix into queue temporarily
    s = Stack(100)  # Create stack for operators
    token, formula = nextToken(formula)
    while token:  # While there are tokens to process
        prec = precedence(token)  # Is it an operator
        delim = delimiter(token)  # Is it a delimiter
        if delim:  # If it's a delimiter
            if token == '(':  # If it's an open parenthesis
                s.push(token)  # Push it onto the stack
            else:  # If it's a close parenthesis
                while not s.isEmpty():  # Pop items off the stack
                    top = s.pop()
                    if top == "(":  # Until open parenthesis is found
                        break
                    else:
                        postfix.insert(top)  # Insert the popped items into the postfix queue

        elif prec:  # If input token is an operator
            while not s.isEmpty():  # Check top of stack
                top = s.pop()  # If open parenthesis or lower precedence operator
                if top == "(" or precedence(top) < prec:
                    s.push(top)  # Push it back on stack and stop loop
                    break
                else:  # Else top is higher precedence operator, so output it
                    postfix.insert(top)
            s.push(token)  # Push input token on stack

        else:  # If input token is an operand, it goes straight to output
            postfix.insert(token)

        token, formula = nextToken(formula)  # Fencepost loop

    while not s.isEmpty():  # At end of input, pop stack and insert into postfix queue
        postfix.insert(s.pop())

    ans = ""  # Convert the elements in the queue to a string
    while not postfix.isEmpty():
        if len(ans) > 0:
            ans += " "
        ans += postfix.remove()
    return ans  # Return the postfix expression

# Main function
if __name__ == "__main__":
    infix_expr = input("Infix expression to translate: ")  # Get the infix expression from the user
    print("The postfix representation of", infix_expr, 'is:', PostFixTranslate(infix_expr))  # Print the postfix expression
