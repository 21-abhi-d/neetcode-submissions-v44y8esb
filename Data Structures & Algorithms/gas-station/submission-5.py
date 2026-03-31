class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        diff = 0
        idx = 0
        for i in range(len(gas)):
            diff += (gas[i] - cost[i])
            if diff < 0:
                diff = 0
                idx = i + 1
        
        return idx
"""
gas = [1, 2, 3, 4, 5]
       i

cost = [3, 4, 5, 1, 2]
        i

diff = [-2, -2, -2, 3, 3]
         i


"""
