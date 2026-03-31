class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        prevEnd = sorted_intervals[0][1]
        count = 0

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] < prevEnd:
                count += 1
                prevEnd = min(prevEnd, sorted_intervals[i][1])
            else:
                prevEnd = sorted_intervals[i][1]
        
        return count