class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)

        target = sum(nums) // 2
        for i in range(len(nums)):
            newDP = set()
            for num in dp:
                newDP.add(num + nums[i])
            dp.update(newDP)
        
        print(dp)

        return True if target in dp else False

"""
target = 5

 i
[1, 2, 3, 4]

dp = {0, 1}
newDp = {}





"""
