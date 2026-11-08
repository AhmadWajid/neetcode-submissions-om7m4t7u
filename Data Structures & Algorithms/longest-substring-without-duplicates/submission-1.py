class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        r= 0
        longest = 0
        while r < len(s):
            if s[r] not in charset:
                charset.add(s[r])
                longest = max(longest, (r-l)+1)
                r += 1
            else:
                charset.remove(s[l])
                l += 1
        return longest
            