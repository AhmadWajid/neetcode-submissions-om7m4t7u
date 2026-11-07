class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left
            left *= nums[i]
        for i in reversed(range(len(nums))):
            result[i] = right * result[i]
            right *= nums[i]
        return result
