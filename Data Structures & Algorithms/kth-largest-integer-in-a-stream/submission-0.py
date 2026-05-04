class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if not self.heap:
            self.heap.append(val)
            return val
        if len(self.heap) < self.k:
            self.heap.append(val)
            start = len(self.heap) - 1
            while start > 0:
                    parent = (start - 1 ) // 2
                    if self.heap[start] < self.heap[parent]:
                        self.heap[start], self.heap[parent] = self.heap[parent], self.heap[start]
                        start = parent
                    else:
                        break
        else:
            if val > self.heap[0]:
                self.heap[0] = val
                i = 0
                while True:
                    left = 2 * i + 1
                    right = 2 * i + 2
                    smallest = i
                    if left < self.k and self.heap[left] < self.heap[smallest]:
                        smallest = left
                    if right < self.k and self.heap[right] < self.heap[smallest]:
                        smallest = right
                    if smallest != i:
                        self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
                        i = smallest
                    else:
                        break
        return self.heap[0]