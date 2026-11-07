class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        buckets = [[] for i in range(len(nums)+1)]
        for key, v in freq.items():
            buckets[v].append(key)
        result = []
        for i in reversed(range(len(buckets))):
            for num in buckets[i]:
                if k == 0:
                    return result
                result.append(num)
                k -= 1
        return result

            
