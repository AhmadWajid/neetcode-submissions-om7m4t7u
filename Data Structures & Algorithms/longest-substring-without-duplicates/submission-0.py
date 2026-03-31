class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeating = set()
        max_length = 0
        l = 0
        for r in range(len(s)):
            while s[r] in repeating:
                repeating.remove(s[l])
                l += 1
            repeating.add(s[r])
            max_length = max(max_length, r - l + 1)
        return max_length
