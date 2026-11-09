# 21 22, 23
#temps = [2]
# days = [0,0,0]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        days = [0] * len(temperatures)

        for i in reversed(range(len(temperatures))):
            if not temps:
                days[i] = 0
                temps.append(i)
            else:
                while temps and temperatures[temps[-1]] <= temperatures[i]:
                    temps.pop()
                if temps:
                    days[i] = temps[-1] - i
                temps.append(i)
        return days
