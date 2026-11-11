class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        results = []
        for interval in intervals:
            if not results:
                results.append(interval)
            else:
                if interval[0] <= results[-1][1]:
                    if results[-1][1] < interval[1]:
                        results[-1][1] = interval[1]
                    else:
                        results[-1][1] = results[-1][1]
                else:
                    results.append(interval)
        return results
                