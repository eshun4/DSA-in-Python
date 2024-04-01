"""
This Functions finds the longest streak of ones in a 0 and 1's array.    
"""

def longest_streak(zeros_and_ones_array):
    longest_streak, current_streak = 0, 0
    for element in zeros_and_ones_array:
        if element == 1:
            current_streak += 1
            longest_streak = max(current_streak, longest_streak)
        else:
            current_streak = 0
    return longest_streak

def longest_subsequence(string):
    if not string:
        return 0
    longest_occurence, current_streak = 0, 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            current_streak += 1
        else:
            longest_occurence = max(current_streak, longest_occurence)
            current_streak = 1
    return max(longest_occurence, current_streak)

def longest_subsequence_string(string):
    if not string:
        return ""

    longest_subsequence, current_subsequence = string[0], string[0]
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            current_subsequence += string[i]
        else:
            if len(current_subsequence) > len(longest_subsequence):
                longest_subsequence = current_subsequence
            current_subsequence = string[i]
    return longest_subsequence if len(current_subsequence) <= len(longest_subsequence) else current_subsequence




print(longest_streak([0,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1]))
print(longest_subsequence("aaccccaaaaa"))
print(longest_subsequence_string("aaccccaaaaa"))
    