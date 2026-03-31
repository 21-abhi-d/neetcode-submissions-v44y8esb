class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlapping = 0
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        newInterval = sorted_intervals[0]

        print(sorted_intervals)
        for i in range(1, len(sorted_intervals)):
            print(f"new interval: {newInterval}")
            if newInterval[1] > sorted_intervals[i][0]:
                overlapping += 1
                newInterval[1] = min(newInterval[1], sorted_intervals[i][1])
            else:
                newInterval = sorted_intervals[i]
        
        return overlapping