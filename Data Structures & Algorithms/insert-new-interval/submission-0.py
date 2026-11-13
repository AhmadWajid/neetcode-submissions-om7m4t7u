class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # Case 1: New interval comes before current interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # Case 2: New interval comes after current interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # Case 3: Intervals overlap, so merge
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        result.append(newInterval)
        return result