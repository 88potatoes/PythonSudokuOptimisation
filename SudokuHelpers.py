import time

import numpy as np


def number_is_valid(board: list[list[int]], r: int, c: int, a: int, sudoku_size=3) -> bool:
    """
    Check if a particular number at a certain square is valid.
    """
    side_length = sudoku_size ** 2

    # check the row
    if a in set(board[r]):
        return False

    # check the column
    if a in set(board[y][c] for y in range(sudoku_size)):
        return False

    # check the squares
    r_start = r // sudoku_size
    c_start = c // sudoku_size
    for dr in range(sudoku_size):
        for dc in range(sudoku_size):
            if a == board[sudoku_size * r_start + dr][sudoku_size * c_start + dc]:
                return False
    return True


def get_n_empty_squares(sudoku: list[list[int]]) -> int:
    return sum(1 for row in sudoku for cell in row if cell == 0)


def get_n_filled_squares(sudoku: list[list[int]]) -> int:
    return sum(1 for row in sudoku for cell in row if cell != 0)


def print_array_stats(label: str, nums: list[int | float]):
    arr = np.array(nums)
    print("=======================")
    print(label)
    print(f"mean : {np.mean(arr)}")
    print(f"stdev: {np.std(arr, ddof=1)}")
    print(f"min: {np.min(arr)}")
    print(f"max: {np.max(arr)}")
    print("=======================")


def print_sudoku(sudoku: list[list[int]], ansi=True) -> None:
    reset = "\033[0m"
    blue = "\033[34m"
    print(f"{reset}==================")
    if ansi:
        for r in range(9):
            line_to_print = " ".join([f"{blue}{num}" if num != 0 else f"{reset}{num}" for num in sudoku[r]])
            print(line_to_print)
    else:
        for r in range(9):
            line_to_print = " ".join(sudoku[r])
            print(line_to_print)
    print(f"{reset}==================")


class Timing:
    def __init__(self, label: str | None = None, add_to=None):
        self.label = label
        self.add_to = add_to

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time

        if self.add_to is not None:
            self.add_to.append(elapsed_time)

        if self.label is not None:
            print(f"{self.label} | elapsed time: {elapsed_time}s")
