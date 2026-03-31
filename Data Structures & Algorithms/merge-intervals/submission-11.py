class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        ret = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            newInterval = ret.pop()
            if sorted_intervals[i][0] > newInterval[1]:
                ret.append(newInterval)
                ret.append(sorted_intervals[i])
            else:
                newInterval = [min(sorted_intervals[i][0], newInterval[0]), 
                           max(sorted_intervals[i][1], newInterval[1])]
                ret.append(newInterval)

        return ret
            




