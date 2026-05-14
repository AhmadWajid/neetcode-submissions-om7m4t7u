class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def backtrack(index, arr, arr_sum):
            if arr_sum == target:
                return result.append(arr.copy())
            if index == len(candidates):
                return
            if arr_sum > target:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])
                backtrack(i + 1, arr, arr_sum+ candidates[i])
                arr.pop()
        backtrack(0, [], 0)
        return result