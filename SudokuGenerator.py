import copy
import json
import random
import SudokuHelpers
from SudokuHelpers import number_is_valid
from SudokuSolver import SudokuSolver


class SudokuGenerator:

    def __init__(self):
        self.sudokuSolver = SudokuSolver()

    def generate_random_solved_sudoku(self):
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

    def generate_random_starting_sudoku(self) -> list[list[int]]:
        sudoku = self.generate_random_solved_sudoku()

        filled_squares = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(filled_squares)

        for i in range(len(filled_squares)):
            r, c = filled_squares[i]

            # erase the number
            val = sudoku[r][c]
            sudoku[r][c] = 0

            # check if the sudoku still has one solution
            if len(self._solve_sudoku(sudoku, sol_limit=2)) == 1:
                continue

            # if it doesn't then replace the number
            sudoku[r][c] = val
            # break
            if i >= 64:
                break

        return sudoku

    def gen_many_starting_sudokus(self, n: int) -> list[list[list[int]]]:
        return [self.generate_random_starting_sudoku() for _ in range(n)]

    def _solve_sudoku(self, sudoku: list[list[int]], sol_limit=0):
        """
        Solves sudoku.
        """
        sudokucopy = copy.deepcopy(sudoku)

        solutions = []

        def dfs():  # TODO can optimise by not looping through everything again
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
                solutions.append(copy.deepcopy(sudokucopy))
                if sol_limit != 0 and len(solutions) >= sol_limit:
                    return True

            return False

        dfs()
        return solutions


# generate a bunch of sudokus and store it to a file
if __name__ == "__main__":
    NUM_SUDOKUS = 10
    generator = SudokuGenerator()
    starting_sudokus = [generator.generate_random_starting_sudoku() for _ in range(NUM_SUDOKUS)]
    with open("starting_sudokus.txt", "a") as file:
        for sudoku in starting_sudokus:
            json.dump(sudoku, file)
            file.write('\n')
