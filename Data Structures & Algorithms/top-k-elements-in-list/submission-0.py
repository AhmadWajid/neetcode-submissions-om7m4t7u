class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        freq_list = [[] for _ in range(len(nums)+ 1)]       
        for ke, v in counter.items():
            freq_list[v].append(ke)
        res = []
        for freq in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[freq]:
                res.append(num)
                if len(res) == k:
                    return res