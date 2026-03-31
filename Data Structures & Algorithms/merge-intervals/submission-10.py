class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        ret = [sorted_intervals[0]]
        print(f"Sorted intervals: {sorted_intervals}")

        for i in range(1, len(sorted_intervals)):
            newInterval = ret.pop()
            print(f"comparing {newInterval} with {intervals[i]}")
            if sorted_intervals[i][0] > newInterval[1]:
                ret.append(newInterval)
                ret.append(sorted_intervals[i])
                print(f"No adds: {ret}")
            else:
                ret.append([min(sorted_intervals[i][0], newInterval[0]), 
                           max(sorted_intervals[i][1], newInterval[1])])
                print(f"Merged and added {ret}")

        return ret
            




