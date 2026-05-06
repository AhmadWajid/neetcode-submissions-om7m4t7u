class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        def insert(val):
            minHeap.append(val)

            i = len(minHeap) - 1

            while i > 0:

                parent = (i - 1) // 2

                if minHeap[i][0] < minHeap[parent][0]:
                    minHeap[i], minHeap[parent] = minHeap[parent], minHeap[i]
                    i = parent
                else:
                    break
        def remove():
            if len(minHeap) == 1:
                return minHeap.pop()

            minVal = minHeap[0]

            minHeap[0] = minHeap.pop()

            i = 0

            while True:

                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < len(minHeap) and minHeap[left][0] < minHeap[smallest][0]:
                    smallest = left

                if right < len(minHeap) and minHeap[right][0] < minHeap[smallest][0]:
                    smallest = right

                if smallest != i:
                    minHeap[i], minHeap[smallest] = minHeap[smallest], minHeap[i]
                    i = smallest
                else:
                    break

            return minVal
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            insert([dist, x, y])
        res = []
        while k > 0:
            dist, x, y = remove()
            res.append([x,y])
            k -= 1
        return res            

