import copy
import json
import random
import SudokuHelpers
from SudokuHelpers import number_is_valid, print_sudoku, Timing, print_sudoku_stats, print_array_stats
from SudokuSolver import SudokuSolver


class SudokuGenerator:

    def __init__(self, size=3):
        self.sudokuSolver = SudokuSolver()
        self.size = size
        self.side_length = size ** 2

    def generate_random_solved_sudoku(self):
        board = [[0 for _ in range(self.side_length)] for _ in range(self.side_length)]

        def dfs():
            all_filled = True
            for r in range(self.side_length):
                for c in range(self.side_length):
                    if board[r][c] != 0:
                        continue
                    all_filled = False

                    candidates = [x for x in range(1, self.side_length + 1)]
                    random.shuffle(candidates)
                    for a in candidates:
                        if SudokuHelpers.number_is_valid(board, r, c, a, sudoku_size=self.size):
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

    def generate_random_starting_sudoku(self) -> list[list[int]]:
        solved_sudoku = self.generate_random_solved_sudoku()

        filled_squares = [(r, c) for r in range(self.side_length) for c in range(self.side_length)]
        random.shuffle(filled_squares)

        n_filled = len(filled_squares)

        for i in range(len(filled_squares)):
            r, c = filled_squares[i]

            # erase the number
            val = solved_sudoku[r][c]
            solved_sudoku[r][c] = 0

            # check if the sudoku still has one solution
            if len(self._solve_sudoku(solved_sudoku, sol_limit=2)) == 1:
                n_filled -= 1
                continue

            # if it doesn't then replace the number
            solved_sudoku[r][c] = val
            # break
            if (self.size == 3 and n_filled <= 17) or (self.size == 4 and n_filled <= 55):
                break

        return solved_sudoku

    def gen_many_starting_sudokus(self, n: int) -> list[list[list[int]]]:
        return [self.generate_random_starting_sudoku() for _ in range(n)]

    def _solve_sudoku(self, problem: list[list[int]], sol_limit=0) -> list[list[list[int]]]:
        """
        Solves sudoku with basic backtracking solution.
        Stops when more than sol_limit solutions have been found.
        """
        sudokucopy = copy.deepcopy(problem)

        solutions = []

        def dfs():  # TODO can optimise by not looping through everything again
            all_filled = True
            for r in range(self.side_length):
                for c in range(self.side_length):
                    if sudokucopy[r][c] != 0:
                        continue

                    all_filled = False
                    for a in range(1, self.side_length + 1):
                        if number_is_valid(sudokucopy, r, c, a, sudoku_size=self.size):
                            sudokucopy[r][c] = a
                            if dfs():
                                return True
                            sudokucopy[r][c] = 0
                    return False

            if all_filled:
                solutions.append(copy.deepcopy(sudokucopy))
                if sol_limit != 0 and len(solutions) >= sol_limit:
                    return True

            return False

        dfs()
        return solutions


# generate a bunch of sudokus and store it to a file
if __name__ == "__main__":
    NUM_SUDOKUS = 2
    SHOW_TIMING = True
    SHOW_SUDOKU_STATS = True
    SUDOKU_FILE = "starting_sudokus.txt"

    generator = SudokuGenerator()
    starting_sudokus = []
    timings = []

    # generating the sudokus and keeping track of time
    for i in range(NUM_SUDOKUS):
        with Timing(add_to=timings):
            problem = generator.generate_random_starting_sudoku()
        starting_sudokus.append(problem)

    # printing generation information
    if SHOW_TIMING:
        print_array_stats(nums=timings, label="timing")

    if SHOW_SUDOKU_STATS:
        print_sudoku_stats(sudoku_list=starting_sudokus)

    # writing the sudokus to the file
    with open(SUDOKU_FILE, "a") as file:
        for sudoku in starting_sudokus:
            json.dump(sudoku, file)
            file.write('\n')
