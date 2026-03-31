class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)]
        print(f"old: {freq}")
        
        print(count_map)
        
        for num, count in count_map.items():
            freq[count].append(num)
        
        print(f"new: {freq}")

        ret = []
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                ret.append(freq[i][j])
            if len(ret) == k:
                break
        
        return ret
            
