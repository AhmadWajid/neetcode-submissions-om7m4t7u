from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or  not grid[0]:
            return 
        row, col = len(grid), len(grid[0])
        queue = deque()
        INF = 2147483647
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    queue.append((r,c))
        directions = [(-1,0), (0,-1), (1,0), (0, 1)]
        while queue:
              r, c = queue.popleft()
              for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == INF:
                     grid[nr][nc] = grid[r][c] + 1
                     queue.append((nr, nc))
        