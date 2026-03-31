class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # [1,   2,  4, 6]
        # [48, 24, 12, 8]
    # left = 1              right = 1
        # [1,   1,  2, 8]
        left = 1
        right = 1
        for i in range(len(nums)):
            res[i] = left
            left *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] = right * res[i]
            right *= nums[i]
        return res
        
        