class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                ret[stackIdx] = (idx - stackIdx)
            
            stack.append((temp, idx))
        
        return ret


"""
temperatures = [30, 38, 30, 36, 35, 40, 28]
                     i

stack = [(40, 5), (28, 6)]

ret = [1, 4, 1, 2, 1, 0, 0]


"""