class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) # -7
            second = heapq.heappop(stones) # -3
            if second > first:
                heapq.heappush(stones, first - second)


        return abs(stones[0]) if stones else 0