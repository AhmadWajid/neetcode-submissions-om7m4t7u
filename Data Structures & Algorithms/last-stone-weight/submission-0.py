class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        def insert(val):
            heap.append(val)

            i = len(heap) - 1

            while i > 0:

                parent = (i - 1) // 2

                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break
        def remove():
            if len(heap) == 1:
                return heap.pop()
            maxStone = heap[0]
            heap[0] = heap.pop()
            i = 0
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                biggest = i

                if left < len(heap) and heap[left] > heap[biggest]:
                    biggest = left

                if right < len(heap) and heap[right] > heap[biggest]:
                    biggest = right

                if biggest != i:
                    heap[i], heap[biggest] = heap[biggest], heap[i]
                    i = biggest
                else:
                    break
            return maxStone
        for stone in stones:
            insert(stone)
        while len(heap) > 1:
            y = remove()
            x = remove()
            if y != x:
                insert(y-x)
        if heap:
            return heap[0]

        return 0

            
        
