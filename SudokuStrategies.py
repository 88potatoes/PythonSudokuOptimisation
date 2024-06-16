import copy
from SudokuHelpers import number_is_valid


def basic_backtracking(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Basic backtracking approach to solve sudoku.
    """
    sudokucopy = copy.deepcopy(sudoku)

    solution = None
    side_length = size ** 2

    def dfs():  # TODO can optimise by not looping through everything again
        nonlocal solution
        all_filled = True
        for r in range(side_length):
            for c in range(side_length):
                if sudokucopy[r][c] != 0:
                    continue

                all_filled = False
                for a in range(1, side_length + 1):
                    if number_is_valid(sudokucopy, r, c, a, sudoku_size=size):
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
