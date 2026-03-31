class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            toFind = target - nums[i] 
            if toFind in seen:
                return [seen[toFind], i]
            seen[nums[i]] = i
