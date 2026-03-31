class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        overlapping = 0
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        new_interval = sorted_intervals[0]

        for i in range(1, len(sorted_intervals)):
            if new_interval[1] > sorted_intervals[i][0]:
                overlapping += 1
                new_interval[1] = min(new_interval[1], sorted_intervals[i][1])
            else:
                new_interval = sorted_intervals[i]


        return overlapping
        