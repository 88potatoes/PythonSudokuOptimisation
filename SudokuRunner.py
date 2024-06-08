from pprint import pprint
import SudokuSolver
import random
import copy

SUDOKU1 = [
    [5, 3, 4, 6, 7, 8, 9, 0, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

SUDOKU2 = [
    [8, 0, 7, 0, 0, 4, 3, 0, 0],
    [9, 6, 0, 0, 2, 7, 0, 0, 8],
    [3, 0, 1, 6, 8, 0, 7, 5, 0],
    [5, 9, 0, 0, 0, 0, 2, 0, 1],
    [0, 7, 0, 0, 1, 3, 6, 8, 9],
    [6, 1, 8, 0, 0, 0, 4, 3, 0],
    [0, 0, 6, 0, 0, 0, 9, 0, 0],
    [0, 5, 4, 0, 9, 6, 0, 2, 3],
    [2, 0, 9, 0, 0, 1, 5, 0, 0]
]

SUDOKU3 = [
    [0, 0, 2, 1, 5, 3, 0, 0, 4],
    [0, 0, 1, 0, 0, 4, 2, 0, 6],
    [7, 4, 6, 2, 0, 0, 3, 0, 5],
    [2, 0, 4, 0, 0, 1, 0, 5, 3],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [6, 5, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 2, 5, 0, 3, 0],
    [0, 2, 5, 0, 3, 0, 1, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 2, 0]
]


class SudokuController:

    def __init__(self):
        self._solutions = []
        self._early_cutoff = 0
        
            


        # filling with random points initially
        # nsols = 
        # for point in random_points:
        #     print(point)
        #     if point not in empty_squares:
        #         continue

        #     empty_squares.remove(point)
        #     candidates = [x for x in range(1, 10)]
        #     random.shuffle(candidates)
        #     for a in candidates:
        #         if self.number_is_valid(sudoku, point[0], point[1], a):
        #             sudoku[point[0]][point[1]] = a
        #             break
        # self._early_cutoff = 1
        # solution_sudoku = self.solve_sudoku(sudoku)[0]
        # self._early_cutoff = 0
        
        # pprint(solution_sudoku)

        # filling with random points until unique solution
        # self._early_cutoff = 2
        # nsols = len(self.solve_sudoku(sudoku))
        # # print("solved")
        # # pprint(sudoku)
        # # print(nsols)
        # while nsols >= 2:
        #     pprint(sudoku)
        #     r, c = random.sample(list(empty_squares), 1)[0]
        #     empty_squares.remove((r, c))
        #     for a in range(1, 10):
        #         if not self.number_is_valid(sudoku, r, c, a):
        #             continue

        #         sudoku[r][c] = a
        #         break
        #     nsols = len(self.solve_sudoku(sudoku))
        # pprint(sudoku)
        # self._early_cutoff = 0
        
        # if nsols == 0:
        #     return None
        # return sudoku
        return sudoku

pprint(SudokuController.solve_sudoku(SUDOKU2))
# pprint(sudokuController.sudoku_is_valid(SUDOKU2))
# pprint(SudokuController.generate_random_solved_sudoku())
# pprint(SudokuController.generate_random_starting_sudoku())


    
        
    
        