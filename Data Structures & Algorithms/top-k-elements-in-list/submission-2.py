class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(f"old: {freq}")

        for i in range(len(nums)):
            count_map[nums[i]] = 1 + count_map.get(nums[i], 0)
        
        print(count_map)
        
        for num, count in count_map.items():
            freq[count].append(num)
        
        print(f"new: {freq}")

        ret = []
        for i in range(len(freq) - 1, -1, -1):
            if freq[i] != [] and len(ret) < k:
                for j in range(len(freq[i])):
                    ret.append(freq[i][j])
        
        return ret
            
