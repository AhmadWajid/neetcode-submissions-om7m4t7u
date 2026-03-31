class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l = 1
        r = max_pile
        b_rate = max_pile
        while l <= r:
            mid = (l+ r) // 2
            temp_hours = 0
            for i in piles:
                temp_hours += (i + mid -1) // mid
            if temp_hours > h:
                l = mid + 1
            if temp_hours <= h:
                b_rate = min(b_rate, mid)
                r = mid - 1
        return b_rate