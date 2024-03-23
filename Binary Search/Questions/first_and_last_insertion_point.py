"""
Here comes your task: you are given a sorted array of floats with values like: [3.14, 3.14, 6.28, 9.42] - 
could be any size, even empty. You've also got a target float in your pocket, say, 3.14. Your mission, 
should you choose to accept it? You need to find the start and end coordinates where this target float
appears in the list.

If the target decides to play hide-and-seek and isn't in the array,
just return [-1, -1]! Oh, and your solution should be smarter and faster than 
O(n)
O(n) time complexity. Is the jet fuel for that? Better buckle up!
"""

def get_first_last_pos(nums, target):
    def binary_search(left, right, find_first):
        # implement this
        if left <= right:
            mid = (left + right) // 2
            if find_first:
                if nums[mid] <= target:
                    right = mid - 1 
                else:
                    left = mid + 1 
            else:
                if nums[mid] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return left 

    first = binary_search(0, len(nums) - 1, True)
    last = binary_search(first, len(nums) - 1, False) - 1
    
    # implement the condition to return accurate results
    if first <= last and nums[first] == target:
        return [first, last]
    else:
        return [-1, -1]

print(get_first_last_pos([3.14, 3.14, 6.28, 9.42], 3.14)) # Should return [0, 1]
print(get_first_last_pos([3.14, 3.14, 6.28, 9.42], 4.13)) # Should return [-1, -1]
print(get_first_last_pos([], 3.14)) # Should return [-1, -1]