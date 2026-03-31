class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count = {}
        max_freq = 0
        max_res = 0
        while r < len(s):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            max_freq = max(max_freq, count[s[r]])

            while ((r - l + 1) - max_freq) > k:
                count[s[l]] -= 1
                l += 1
            max_res = max(max_res, r - l +1)
            r += 1                
        return max_res
                


            