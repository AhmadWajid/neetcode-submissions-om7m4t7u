class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = {}
        row = {}
        square = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue

                if r not in row:
                    row[r] = set()
                if c not in column:
                    column[c] = set()
                if (r//3, c//3) not in square:
                    square[(r//3, c//3)] = set()

                if val in row[r] or val in column[c] or val in square[(r//3, c//3)]:
                    return False

                row[r].add(val)
                column[c].add(val)
                square[(r//3, c//3)].add(val)

        return True
