class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, arr, arr_sum):
            if arr_sum == target:
                return result.append(arr.copy())
            if index == len(nums):
                return
            if arr_sum > target:
                return
            arr.append(nums[index])
            arr_sum += nums[index]
            backtrack(index, arr, arr_sum)
            arr_sum -= arr.pop()
            backtrack(index + 1, arr, arr_sum)
             


        backtrack(0, [], 0)
        return result