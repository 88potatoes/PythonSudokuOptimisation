import copy
import random
from collections import deque

from SudokuHelpers import number_is_valid


def basic_backtracking(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Basic backtracking approach to solve sudoku.
    """
    sudokucopy = copy.deepcopy(sudoku)

    solution = None
    side_length = size ** 2

    def dfs():
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


def opt1_backtracking(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Basic backtracking approach to solve sudoku.
    Slight optimisation to start from where the previous function call left off
    """
    sudokucopy = copy.deepcopy(sudoku)
    solution = None
    side_length = size ** 2

    def dfs(cr, cc):
        nonlocal solution
        all_filled = True
        for r in range(cr, side_length):
            for c in range(cc if r == cr else 0, side_length):
                if sudokucopy[r][c] != 0:
                    continue

                all_filled = False
                for a in range(1, side_length + 1):
                    if number_is_valid(sudokucopy, r, c, a, sudoku_size=size):
                        sudokucopy[r][c] = a

                        if c == side_length - 1:
                            if dfs(r + 1, 0):
                                return True
                        else:
                            if dfs(r, c + 1):
                                return True

                        sudokucopy[r][c] = 0
                return False

        if all_filled:
            solution = copy.deepcopy(sudokucopy)
            return True

        return False

    dfs(0, 0)
    return solution


def opt2_backtracking(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Basic backtracking approach to solve sudoku.
    Testing numbers in reverse order
    """
    sudokucopy = copy.deepcopy(sudoku)
    solution = None
    side_length = size ** 2

    def dfs(cr, cc):
        nonlocal solution
        all_filled = True
        for r in range(cr, side_length):
            for c in range(cc if r == cr else 0, side_length):
                if sudokucopy[r][c] != 0:
                    continue

                all_filled = False
                for a in range(side_length, -1, -1):
                    if number_is_valid(sudokucopy, r, c, a, sudoku_size=size):
                        sudokucopy[r][c] = a

                        if c == side_length - 1:
                            if dfs(r + 1, 0):
                                return True
                        else:
                            if dfs(r, c + 1):
                                return True

                        sudokucopy[r][c] = 0
                return False

        if all_filled:
            solution = copy.deepcopy(sudokucopy)
            return True

        return False

    dfs(0, 0)
    return solution


def opt3_backtracking(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Basic backtracking approach to solve sudoku.
    Testing numbers in random order
    """
    sudokucopy = copy.deepcopy(sudoku)
    solution = None
    side_length = size ** 2

    def dfs(cr, cc):
        nonlocal solution
        all_filled = True
        for r in range(cr, side_length):
            for c in range(cc if r == cr else 0, side_length):
                if sudokucopy[r][c] != 0:
                    continue

                all_filled = False
                nums = [x for x in range(1, 10)]
                random.shuffle(nums)
                for a in nums:
                    if number_is_valid(sudokucopy, r, c, a, sudoku_size=size):
                        sudokucopy[r][c] = a

                        if c == side_length - 1:
                            if dfs(r + 1, 0):
                                return True
                        else:
                            if dfs(r, c + 1):
                                return True

                        sudokucopy[r][c] = 0
                return False

        if all_filled:
            solution = copy.deepcopy(sudokucopy)
            return True

        return False

    dfs(0, 0)
    return solution


def opt4_backtracking(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Basic backtracking approach to solve sudoku.
    opt3 but eliminates the function call to number_is_valid and instead stores it into an array
    """
    sudokucopy = copy.deepcopy(sudoku)
    solution = None
    side_length = size ** 2

    row_nums = [set() for _ in range(9)]
    col_nums = [set() for _ in range(9)]
    box_nums = [set() for _ in range(9)]

    for r, c in [(r, c) for c in range(9) for r in range(9) if sudoku[r][c] != 0]:
        row_nums[r].add(sudoku[r][c])
        col_nums[c].add(sudoku[r][c])
        box_nums[3 * (r // 3) + c // 3].add(sudoku[r][c])

    def dfs(cr, cc):
        nonlocal solution
        all_filled = True
        for r in range(cr, side_length):
            for c in range(cc if r == cr else 0, side_length):
                if sudokucopy[r][c] != 0:
                    continue

                all_filled = False
                nums = [x for x in range(1, 10)]
                random.shuffle(nums)
                for a in nums:
                    if not (a in row_nums[r] or a in col_nums[c] or a in box_nums[3 * (r // 3) + c // 3]):
                        sudokucopy[r][c] = a
                        row_nums[r].add(a)
                        col_nums[c].add(a)
                        box_nums[3 * (r // 3) + c // 3].add(a)

                        if c == side_length - 1:
                            if dfs(r + 1, 0):
                                return True
                        else:
                            if dfs(r, c + 1):
                                return True

                        sudokucopy[r][c] = 0
                        row_nums[r].remove(a)
                        col_nums[c].remove(a)
                        box_nums[3 * (r // 3) + c // 3].remove(a)
                return False

        if all_filled:
            solution = copy.deepcopy(sudokucopy)
            return True

        return False

    dfs(0, 0)
    return solution


def opt5_backtracking(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Basic backtracking approach to solve sudoku.
    opt4 but not random number testing - goes in order from 1 - 10
    """
    sudokucopy = copy.deepcopy(sudoku)
    solution = None
    side_length = size ** 2

    row_nums = [set() for _ in range(9)]
    col_nums = [set() for _ in range(9)]
    box_nums = [set() for _ in range(9)]

    for r, c in [(r, c) for c in range(9) for r in range(9) if sudoku[r][c] != 0]:
        row_nums[r].add(sudoku[r][c])
        col_nums[c].add(sudoku[r][c])
        box_nums[3 * (r // 3) + c // 3].add(sudoku[r][c])

    def dfs(cr, cc):
        nonlocal solution
        all_filled = True
        for r in range(cr, side_length):
            for c in range(cc if r == cr else 0, side_length):
                if sudokucopy[r][c] != 0:
                    continue

                all_filled = False
                for a in range(1, 10):
                    if not (a in row_nums[r] or a in col_nums[c] or a in box_nums[3 * (r // 3) + c // 3]):
                        sudokucopy[r][c] = a
                        row_nums[r].add(a)
                        col_nums[c].add(a)
                        box_nums[3 * (r // 3) + c // 3].add(a)

                        if c == side_length - 1:
                            if dfs(r + 1, 0):
                                return True
                        else:
                            if dfs(r, c + 1):
                                return True

                        sudokucopy[r][c] = 0
                        row_nums[r].remove(a)
                        col_nums[c].remove(a)
                        box_nums[3 * (r // 3) + c // 3].remove(a)
                return False

        if all_filled:
            solution = copy.deepcopy(sudokucopy)
            return True

        return False

    dfs(0, 0)
    return solution


def constraint1(sudoku: list[list[int]], size: int = 3) -> list[list[int]] | None:
    """
    Use constraint programming.
    Backtracking with minimum remaining values heuristic
    """

    solution = None

    # each square needs to store its possible values
    domains = [[set(x for x in range(1, 10)) for _ in range(9)] for _ in range(9)]

    def ac3():
        queue = deque((r, c) for c in range(9) for r in range(9) if sudoku[r][c] != 0)
        print(queue)

    ac3()

    return solution
