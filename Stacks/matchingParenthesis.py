""" This program check for matching paranthesis using an array as a stack."""


def matchingParenthesis(line):
    stack = []
    for letter in line:
        if letter in "{[(":
            stack.append(letter)
        elif letter in '}])':
            if not stack:
                return False
            left = stack.pop()
            if not (left == '{' and letter == '}' 
                    or left == '[' and letter == ']' 
                    or left == '(' and letter == ')'):
                return False
    return len(stack) == 0

def are_brackets_balanced(input_str):
    brackets = set(["(", ")", "[", "]", "{", "}"])
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []

    for character in input_str:
        if character not in brackets:
            # Skipping non-bracket characters
            continue
        if character in open_par:
            stack.append(character)
        elif stack and character == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return len(stack) == 0


def test_matchingParenthesis():
    assert matchingParenthesis("{[()]}") == True, "Test Case 1 Failed"
    assert matchingParenthesis("{[(])}") == False, "Test Case 2 Failed"
    assert matchingParenthesis("{{[[(())]]}}") == True, "Test Case 3 Failed"
    assert matchingParenthesis("") == True, "Test Case 4 Failed"
    assert matchingParenthesis("{") == False, "Test Case 5 Failed"
    assert matchingParenthesis("}") == False, "Test Case 6 Failed"
    assert matchingParenthesis("(") == False, "Test Case 7 Failed"
    assert matchingParenthesis(")") == False, "Test Case 8 Failed"
    assert matchingParenthesis("[") == False, "Test Case 9 Failed"
    assert matchingParenthesis("]") == False, "Test Case 10 Failed"
    print("All test cases pass")


if __name__ == "__main__":
    test_matchingParenthesis()
