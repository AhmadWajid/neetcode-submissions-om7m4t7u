class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total = 0
        fresh = 0
        if not grid or not grid[0]:
            return -1
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col ] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row,col))
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            to_add = []
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        to_add.append((nr, nc))
            if len(to_add) != 0:
                 total += 1
                 queue.extend(to_add)
                 to_add = []
        if fresh == 0: 
            return total
        else: return -1