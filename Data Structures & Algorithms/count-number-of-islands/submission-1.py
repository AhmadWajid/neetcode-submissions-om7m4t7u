class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        cols = len(grid[0])
        rows = len(grid)
        def dfs(col, row):
            if col <= -1 or col >= cols or row <= -1 or row >= rows or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    dfs(col + x, row + y)
        if grid:
            for col in range(cols):
                for row in range(rows):
                    if grid[row][col] == "1":
                        islands += 1
                        dfs(col,row)

        return islands