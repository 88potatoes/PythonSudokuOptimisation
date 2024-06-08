import random
import SudokuHelpers
import SudokuSolver
    
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
                    if SudokuHelpers.number_is_valid(board, r, c, a):
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

def generate_random_starting_sudoku() -> list[list[int]]:
    sudoku = generate_random_solved_sudoku()

    filled_squares = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(filled_squares)
    print(filled_squares)

    for r, c in filled_squares:
        # erase the number
        val = sudoku[r][c]
        sudoku[r][c] = 0

        # check if the sudoku still has one solution
        if len(SudokuSolver.solve_sudoku(sudoku, limit=2)) == 1:
            continue

        # if it doesn't then replace the number and finish
        sudoku[r][c] = val
        break

    return sudoku

