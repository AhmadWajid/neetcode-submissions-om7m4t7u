class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        l = 0
        r = len(nums) -1
        while l <= r -2:
            if l > 0 and nums[l] == nums[l-1]:
                l += 1
                continue
            base = l
            second = base + 1
            third = r
            while second < third:
                first_num = nums[base]
                second_num = nums[second]
                third_num = nums[third]
                sum_val = first_num + second_num + third_num
                if sum_val == 0:
                    result.append([first_num,second_num,third_num])
                    second += 1
                    third -= 1 
                    while second < third and nums[second] == nums[second - 1]:
                        second += 1
                    while second < third and nums[third] == nums[third + 1]:
                        third -= 1
                elif sum_val > 0:
                    third -= 1
                else:
                    second += 1
            l += 1
        return result