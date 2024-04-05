""" This is a worde reversal with the implemented Simple Stack class."""

from simpleStack import * 

word = input(str('Enter a word: '))

stack = Stack(len(word))

for letter in word:
    stack.push(letter)
    
reverse = ''
while not stack.isEmpty():
    reverse += stack.pop()

print("The reverse of", word, 'is', reverse)