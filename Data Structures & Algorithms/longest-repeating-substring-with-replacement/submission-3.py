class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_win = 0
        count = {}

        while r < len(s):
            print(f"Current window indexes: {l} {r}")
            print(f"Current window: {s[l:r+1]}")
            print(f"counter: {count}")
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                print(f"max window exceeded, removing {s[l]}")
                count[s[l]] -= 1
                l += 1
            max_win = max(max_win, (r - l + 1))
            r += 1
        
        return max_win
        