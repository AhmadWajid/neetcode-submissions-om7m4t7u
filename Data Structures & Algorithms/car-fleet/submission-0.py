class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        both = list(zip(position,speed))
        both.sort(reverse=True)
        fleet = 0
        max_time = 0
        for position, speed in both:
            time = (target - position) / speed
            if time > max_time:
                fleet += 1
                max_time = time
        return fleet
