class TimeMap:

    def __init__(self):
        self.t_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.t_map:
            self.t_map[key].append((value, timestamp))
        else:
            self.t_map[key] = []
            self.t_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key in self.t_map:
            l = 0
            r = len(self.t_map[key]) - 1
            while l <=r:
                mid = (l + r) // 2
                arr = self.t_map[key]
                if arr[mid][1] <= timestamp:
                    ans = arr[mid][0]
                    l = mid + 1
                else:
                    r = mid - 1
        return ans