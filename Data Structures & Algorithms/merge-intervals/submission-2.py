class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        # print(intervals)

        output = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] <= output[-1][1]:
                sorted_intervals[i] = [min(output[-1][0], sorted_intervals[i][0]), 
                                       max(output[-1][1], sorted_intervals[i][1])]
                output[-1] = sorted_intervals[i]
            else: 
                output.append(sorted_intervals[i])
        
        return output
            




