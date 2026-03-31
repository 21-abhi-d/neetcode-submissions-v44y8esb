class Solution:
    def countSubstrings(self, s: str) -> int:
        
        num_pali = 0
        for i in range(len(s)):
            num_pali += self.countPalindrome(s, i, i)
            num_pali += self.countPalindrome(s, i, i + 1)
        
        return num_pali


    def countPalindrome(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        return count
