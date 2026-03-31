class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frequencies = [ [] for i in range(len(nums) + 1) ]
        # print(frequencies)
        # print(count)
        ret = []

        for num, count in count.items():
            frequencies[count].append(num)
        
        for i in range(len(frequencies) - 1, -1, -1):
            for num in frequencies[i]:
                ret.append(num)
                k -= 1
            
            if k == 0:
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
            
