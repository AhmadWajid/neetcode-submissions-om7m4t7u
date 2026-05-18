class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(arr):
            if len(arr) == len(nums):
                return result.append(arr.copy())
            for num in nums:
                    if num in arr:
                        continue
                    arr.append(num)
                    backtrack(arr)
                    arr.pop()

        backtrack([])
        return result