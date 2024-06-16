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

    sudoku_copy = copy.deepcopy(sudoku)

    # each square needs to store its possible values
    domains = [[set(x for x in range(1, 10)) for _ in range(9)] for _ in range(9)]


    def dfs(doms: list[list[set[int]]]):
        # running ac3
        new_doms = ac3(doms, sudoku_copy)
        if new_doms is None:
            return False

        all_filled = True
        for r in range(9):
            for c in range(9):
                for val in new_doms[r][c]:
                    all_filled = False
                    sudoku_copy[r][c] = val

                    if dfs(new_doms):
                        return True

                    sudoku_copy[r][c] = 0

        if all_filled:
            return True

    dfs(domains)

    return sudoku_copy


def ac3(domains: list[list[set[int]]], sudoku: list[list[int]], size: int = 3):
    """
    Standard AC3 algorithm.
    Assumes unary constraints have not been applied yet.
    """

    def revise(row1, col1, row2, col2):
        changed = False
        to_remove = []
        for val1 in domain_copy[row1][col1]:
            val1_valid = False
            for val2 in domain_copy[row2][col2]:
                if val1 != val2:
                    val1_valid = True
                    break

            if not val1_valid:
                to_remove.append(val1)
                changed = True

        for val in to_remove:
            domain_copy[row1][col1].remove(val)
        return changed

    domain_copy = copy.deepcopy(domains)

    # apply unary constraints
    filled_squares = [(r, c) for r in range(9) for c in range(9) if sudoku[r][c] != 0]
    for r, c in filled_squares:
        if sudoku[r][c] in domain_copy[r][c]:
            domain_copy[r][c].remove(sudoku[r][c])
        for a, b in get_connected_arcs(r, c):
            r2, c2 = b
            if sudoku[r][c] in domain_copy[r2][c2]:
                domain_copy[r2][c2].remove(sudoku[r][c])

    # go through all binary constraints
    queue = deque(get_all_sudoku_arcs())
    while queue:
        a, b = queue.popleft()
        r1, c1 = a
        r2, c2 = b
        if revise(r1, c1, r2, c2):
            if len(domain_copy[r1][c2]) == 0:
                return None
            else:
                queue.extend(get_connected_arcs(r1, c1))
    return domain_copy


def get_all_sudoku_arcs():
    res = []
    for r in range(9):
        for c in range(9):
            # for each square, get all the squares in the same row, the same column and the same box
            # same row and column
            for i in range(9):
                if i != c:
                    res.append(((r, c), (r, i)))
                if i != r:
                    res.append(((r, c), (i, c)))

            # same box
            start_r, start_c = r // 3, c // 3
            for i in range(3):
                for j in range(3):
                    if 3 * start_r + i == r and 3 * start_c + j == c:
                        continue

                    res.append(((r, c), (3 * start_r + i, 3 * start_c + j)))

    return res


def get_connected_arcs(r: int, c: int, size: int = 3):
    res = []
    # same row and column
    for i in range(9):
        if i != c:
            res.append(((r, c), (r, i)))
        if i != r:
            res.append(((r, c), (i, c)))

    # same box
    start_r, start_c = r // 3, c // 3
    for i in range(3):
        for j in range(3):
            if 3 * start_r + i == r and 3 * start_c + j == c:
                continue

            res.append(((r, c), (3 * start_r + i, 3 * start_c + j)))
    return res
