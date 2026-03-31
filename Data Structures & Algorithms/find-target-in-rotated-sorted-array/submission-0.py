# l , r
# while l <= r:
# mid
# 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <=r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                if target >= nums[mid] and target <= nums[r]:
                    if target == nums[mid]:
                        return mid
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target >= nums[l] and target <= nums[mid]:
                    if target == nums[mid]:
                        return mid
                    r = mid - 1  
                else:
                    l = mid + 1    
        return -1  