class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue

                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]:
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[r//3, c//3].add(board[r][c])

        return True