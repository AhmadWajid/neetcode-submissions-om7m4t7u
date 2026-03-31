class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            current = 1
            while num + 1 in set_nums:
                current += 1
                num +=1
            longest = max(longest, current)
        return longest 