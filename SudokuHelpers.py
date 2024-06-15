import numpy as np


def number_is_valid(board: list[list[int]], r: int, c: int, a: int) -> bool:
    """
    Check if a particular number at a certain square is valid.
    """

    # check the row
    if a in set(board[r]):
        return False

    # check the column
    if a in set([board[y][c] for y in range(9)]):
        return False

    # check the squares
    r_start = r // 3
    c_start = c // 3
    for dr in range(3):
        for dc in range(3):
            if a == board[3 * r_start + dr][3 * c_start + dc]:
                return False
    return True


def get_n_empty_squares(sudoku: list[list[int]]) -> int:
    return sum(1 for row in sudoku for cell in row if cell == 0)


def print_mean_and_stdev(label: str, nums: list[int | float]):
    arr = np.array(nums)
    print("=======================")
    print(label)
    print(f"mean : {np.mean(arr)}")
    print(f"stdev: {np.std(arr, ddof=1)}")
    print("=======================")


def print_sudoku(sudoku: list[list[int]], ansi=True) -> None:
    reset = "\033[0m"
    blue = "\033[34m"
    print(f"{reset}==================")
    if ansi:
        for r in range(9):
            line_to_print = " ".join([f"{blue}{num}" if num != 0 else f"{reset}{num}"for num in sudoku[r]])
            print(line_to_print)
    else:
        for r in range(9):
            line_to_print = " ".join(sudoku)
            print(line_to_print)
    print(f"{reset}==================")
