class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        max_length = 0
        l = 0
        r = 0
        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length



"""
                  r
                  l
s = a b c a b c b b

set = (c, b)
max_length = 3


"""
