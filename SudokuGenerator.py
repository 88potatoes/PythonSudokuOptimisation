import random
import SudokuHelpers
from pprint import pprint
from SudokuSolver import SudokuSolver
import copy
from SudokuHelpers import number_is_valid
    
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

        for r, c in filled_squares:
            # erase the number
            val = sudoku[r][c]
            sudoku[r][c] = 0

            # check if the sudoku still has one solution
            if len(self._solve_sudoku(sudoku, sol_limit=2)) == 1:
                continue

            # if it doesn't then replace the number and finish
            sudoku[r][c] = val
            break

        return sudoku
    
    def _solve_sudoku(self, sudoku: list[list[int]], sol_limit=0):
        """
        Solves sudoku.
        """
        sudokucopy = copy.deepcopy(sudoku)

        solutions = []

        def dfs(): # TODO can optimise by not looping through everything again
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

