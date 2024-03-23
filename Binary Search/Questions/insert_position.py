"""
    Imagine we're cruisin' the galaxy and bump into an array of integers, sorted but with some stowaway duplicates.
    Your mission, oh brainy one, is to craft an algorithm, 
    using a modified binary search, to find where a given 
    integer, our target, should dock. If the target is already in the array,
    return the index of its leftmost occurrence. If it's lost in space, 
    provide the index where it should join while keeping the array sorted.

    You'll be coding a function that takes two inputs. 
    First, the array of integers, such as [1, 2, 3, 3, 5] 
    and second, the target integer, say 3. But remember, 
    it could be that the target is not on the list, for example, 4.
    
"""

def insert_position(nums, target):
    # implement this
    nums.append(float('inf'))
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            left = mid + 1
        else:
            right = mid - 1 
    return left
    

print(insert_position([1, 2, 3, 3, 5], 3))  # Expected output: 2
print(insert_position([1, 2, 3, 3, 5], 4))  # Expected output: 4
print(insert_position([1, 3, 5, 7, 9], 10)) # Expected output: 5