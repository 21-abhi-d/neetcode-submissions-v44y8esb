class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len




"""
                r
            l
s = a b c a b c b b

set = (a, c)
max_length = 3


"""
