class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endIndex = {}

        for i, v in enumerate(s):
            endIndex[v] = i
        
        ret = []
        size, end = 0, 0
        for i, v in enumerate(s):
            size += 1
            end = max(end, endIndex[v])

            if i == end:
                ret.append(size)
                size = 0
        
        return ret
