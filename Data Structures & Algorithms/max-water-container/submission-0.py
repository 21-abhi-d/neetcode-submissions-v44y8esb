class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = float("-inf")

        while l < r:
            min_h = min(heights[l], heights[r])
            print(min_h)
            max_area = max(max_area, min_h * (r - l))
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area


    

"""
 l
[1, 7, 2, 5, 4, 7, 3, 6]
                      r

width (r - l) = 7

max_area = -inf

max_area = 7

"""