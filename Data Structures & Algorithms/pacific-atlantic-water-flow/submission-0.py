class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visited):
            if (r, c) in visited:
                return

            visited.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < len(heights) and
                    0 <= nc < len(heights[0]) and
                    (nr, nc) not in visited and
                    heights[nr][nc] >= heights[r][c]):

                    dfs(nr, nc, visited)

        # Pacific: top + left
        for c in range(len(heights[0])):
            dfs(0, c, pacific_set)

        for r in range(len(heights)):
            dfs(r, 0, pacific_set)

        # Atlantic: bottom + right
        for c in range(len(heights[0])):
            dfs(len(heights) - 1, c, atlantic_set)

        for r in range(len(heights)):
            dfs(r, len(heights[0]) - 1, atlantic_set)

        result = []

        for r, c in pacific_set:
            if (r, c) in atlantic_set:
                result.append([r, c])

        return result   