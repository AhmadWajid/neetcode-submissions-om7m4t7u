class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key = lambda x: x[0], reverse=True)
        fleet = []
        for car in cars:
            time = ((target - car[0]) / car[1])
            if not fleet:
                fleet.append(time)
            else:
                if fleet[-1] < time:
                    fleet.append(time)
        return len(fleet)
