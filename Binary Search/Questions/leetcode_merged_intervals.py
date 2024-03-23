"""
    LeetCode Problem: Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
Starting Point:
Python
Copy
def merge(intervals):
    # Your code here
    pass
This problem is excellent for testing your ability to manipulate arrays and understand the concept of intervals. Plus, it's an excellent chance to dive into the ideas of sorting and iterating over arrays in a more complex scenario.

Would you like some hints or tips on how to approach solving this problem?
"""


def merge(intervals) :
    # First sort the intervals by the first number in the interval
    intervals.sort(key=lambda x:x[0])
    merged = [] #Create the merged array
    for interval in intervals: #Loop through all the intervals
        if not merged or merged[-1][1] < interval[0]: # If merged array is empty and 
        # current overlap does not overlap with previous
            merged.append(interval)
        else:
            # If current interval overlaps with previous one
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged # Return the merged array

def test_merge_function(merge):
    # Test Case 1: Basic Overlapping Intervals
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]], "Test Case 1 Failed"
    
    # Test Case 2: Continuous Overlaps
    assert merge([[1,4],[4,5],[5,6],[6,7]]) == [[1,7]], "Test Case 2 Failed"
    
    # Test Case 3: Non-overlapping Intervals
    assert merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]], "Test Case 3 Failed"
    
    # Test Case 4: Single Interval
    assert merge([[1,3]]) == [[1,3]], "Test Case 4 Failed"
    
    # Test Case 5: Empty List of Intervals
    assert merge([]) == [], "Test Case 5 Failed"
    
    # Test Case 6: Overlapping and Non-overlapping Mix
    assert merge([[1,5],[10,15],[6,10],[16,20]]) == [[1,5],[6,15],[16,20]], "Test Case 6 Failed"
    
    # Test Case 7: Large Overlapping Intervals
    assert merge([[1,4],[2,3],[3,5]]) == [[1,5]], "Test Case 7 Failed"
    
    # Test Case 8: Intervals Containing Other Intervals
    assert merge([[1,10],[2,6],[3,5]]) == [[1,10]], "Test Case 8 Failed"
    
    # Test Case 9: Overlapping at a Single Point
    assert merge([[1,3],[3,6],[6,8]]) == [[1,8]], "Test Case 9 Failed"
    
    # Test Case 10: Decreasing Order Intervals (To Test Sorting)
    assert merge([[5,6],[3,4],[1,2]]) == [[1,2],[3,4],[5,6]], "Test Case 10 Failed"

    print("All test cases passed!")



# Uncomment this line to test your function with the test cases
test_merge_function(merge)


        