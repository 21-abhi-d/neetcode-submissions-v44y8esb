class Solution:
    def numDecodings(self, s: str) -> int:
        # stores all possibilites, can resuse across paths and hence dp.
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            # we can take current value as single digit
            res = dfs(i + 1)
            # taking double digit case
            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            
            dp[i] = res
            return res
        
        return dfs(0)

"""
 i
"2 2 6"


dp = {

}



"""
