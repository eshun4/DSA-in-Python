"""
Insert Interval
Imagine you're given a series of non-overlapping intervals sorted by their start times, and your task is to insert a new interval into the series. After insertion, if any intervals overlap, merge all overlapping intervals to produce a list of non-overlapping intervals sorted in ascending order by their start times.

You're provided with an array of intervals, where intervals[i] = [start_i, end_i], and you must insert a new interval newInterval = [start, end] into the array of intervals while ensuring the array remains sorted by start times. Merge any overlapping intervals.

Your function should return an array of the final, non-overlapping intervals.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Explanation: Because the new interval [2,5] overlaps with [1,3], merge them into [1,5].

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10], merge them into [3,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^5
newInterval.length == 2
0 <= start <= end <= 10^5
"""

def insert_interval(intervals, newInterval):
    result = []
    i = 0
    # Step 1: Add all intervals before the newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
        
    # Step 2: Merge the newInterval with overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        i += 1
    result.append(newInterval)
    
    # Step 3: Add the remaining intervals after the newInterval
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result
    