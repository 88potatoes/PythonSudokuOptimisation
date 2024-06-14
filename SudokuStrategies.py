import copy
from SudokuHelpers import number_is_valid


def basic_backtracking(sudoku: list[list[int]]) -> list[list[int]] | None:
    """
        Basic backtracking approach to solve sudoku.
        """
    sudokucopy = copy.deepcopy(sudoku)

    solution = None

    def dfs():  # TODO can optimise by not looping through everything again
        nonlocal solution
        all_filled = True
        for r in range(9):
            for c in range(9):
                if sudokucopy[r][c] != 0:
                    continue

                all_filled = False
                for a in range(1, 10):
                    if number_is_valid(sudokucopy, r, c, a):
                        sudokucopy[r][c] = a
                        if dfs():
                            return True
                        sudokucopy[r][c] = 0
                return False

        if all_filled:
            solution = copy.deepcopy(sudokucopy)
            return True

        return False

    dfs()
    return solution
