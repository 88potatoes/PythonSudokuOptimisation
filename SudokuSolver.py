from SudokuHelpers import number_is_valid
import copy

def solve_sudoku(sudoku: list[list[int]], limit=0):
    """
    Solves sudoku.
    """

    solutions = []

    def dfs(): # TODO can optimise by not looping through everything again
        all_filled = True
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] != 0:
                    continue

                all_filled = False
                for a in range(1, 10):
                    if number_is_valid(sudoku, r, c, a):
                        sudoku[r][c] = a
                        if dfs():
                            return True
                        sudoku[r][c] = 0
                return False
        
        if all_filled:
            solutions.append(copy.deepcopy(sudoku))
            if limit != 0 and len(solutions) >= limit:
                return True
        
        return False

    dfs()
    return solutions