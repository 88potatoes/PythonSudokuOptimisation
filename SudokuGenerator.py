import random
from SudokuHelpers import number_is_valid
    
def generate_random_solved_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    def dfs():
        all_filled = True
        for r in range(9):
            for c in range(9):
                if board[r][c] != 0:
                    continue
                all_filled = False

                candidates = [x for x in range(1, 10)]
                random.shuffle(candidates)
                for a in candidates:
                    if number_is_valid(board, r, c, a):
                        board[r][c] = a
                        if dfs():
                            return True
                        board[r][c] = 0
                return False

        if all_filled:
            return True
        return False
    
    dfs()
    return board

