""" This is a function that just reverses a string."""

def reverse(string):
    stack = []
    for letter in string:
        stack.append(letter)
    reverse = ""
    while stack:
        reverse += stack.pop()
    return reverse

def reverse2(string):
    reverse = ""
    for i in range(len(string)-1, -1, -1):
        reverse += string[i]
    return reverse

print(reverse("Hello"))
print(reverse2("Hello"))
