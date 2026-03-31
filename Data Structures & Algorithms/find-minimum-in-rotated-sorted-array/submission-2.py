class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l+r) // 2
            if mid == l:
                l+= 1
                continue
            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]