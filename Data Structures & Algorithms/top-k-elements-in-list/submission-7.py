class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequencies = [ [] for i in range(len(nums)) ]
        print(frequencies)
        print(count)

        for num, freq in count.items():
            frequencies[freq - 1].append(num)

        ret = []
        for i in range(len(frequencies) - 1, -1, -1):
            for num in frequencies[i]:
                ret.append(num)
            
            if len(ret) == k:
                break

        return ret        
            
            





"""
nums = [1, 2, 2, 3, 3, 3]
count = {
    1: 1,
    2: 2,
    3: 3
}

new = [[1], [2], [3], [], [], []]



"""
            
