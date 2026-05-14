class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, arr):
            if index == len(nums):
                return result.append(arr.copy())
            arr.append(nums[index])
            backtrack(index + 1, arr)
            arr.pop()
            backtrack(index + 1, arr)
        
        backtrack(0, [])
        return result