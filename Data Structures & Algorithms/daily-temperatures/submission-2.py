class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            print(stack)
            while stack and stack[-1][1] < temp:
                curr_idx, curr_temp = stack.pop()
                ret[curr_idx] = idx - curr_idx
            stack.append((idx, temp))
        
        return ret
