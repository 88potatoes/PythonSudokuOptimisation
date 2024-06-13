from SudokuHelpers import number_is_valid
import copy

class SudokuSolver:

    def __init__(self, strategy=None):
        self._strategy = strategy
    
    def set_strategy(self, strategy):
        if not self._strategy:
            raise ValueError("SudokuSolver has no strategy")
        self._strategy = strategy

    def solve_sudoku(self, sudoku: list[list[int]]) -> list[list[int]]:
        """
        Returns 1 solution to the sudoku.
        """

        if not self._strategy:
            raise ValueError("SudokuSolver has no strategy")
        
        return self._strategy(sudoku)

    # def solve_sudoku(self, sudoku: list[list[int]], sol_limit=0):
    #     """
    #     Solves sudoku.
    #     """
    #     sudokucopy = copy.deepcopy(sudoku)

    #     solutions = []

    #     def dfs(): # TODO can optimise by not looping through everything again
    #         all_filled = True
    #         for r in range(9):
    #             for c in range(9):
    #                 if sudokucopy[r][c] != 0:
    #                     continue

    #                 all_filled = False
    #                 for a in range(1, 10):
    #                     if number_is_valid(sudokucopy, r, c, a):
    #                         sudokucopy[r][c] = a
    #                         if dfs():
    #                             return True
    #                         sudokucopy[r][c] = 0
    #                 return False
            
    #         if all_filled:
    #             solutions.append(copy.deepcopy(sudokucopy))
    #             if sol_limit != 0 and len(solutions) >= sol_limit:
    #                 return True
            
    #         return False

    #     dfs()
    #     return solutions

    # def solve_multiple_sudokus(sudoku_list: list[list[list[int]]]) -> list[list[list[int]]]:
        