from pprint import pprint
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

    @staticmethod
    def solve_sudoku(sudoku: list[list[int]], limit=0):
        """
        Solves sudoku
        mutates self._solutions
        but start and end is the same state
        """
        
        # self._solutions = []
        # sudoku_copy = copy.deepcopy(sudoku)
        # self._solve_sudoku_helper(sudoku_copy)
        # # print("-")
        # # pprint(self._solutions)
        # # print("-")
        # solutions = self._solutions.copy()
        # pprint(solutions)
        # self._solutions = []
        # return solutions

        solutions = []

        def dfs(): # TODO can optimise by not looping through everything again
            all_filled = True
            for r in range(9):
                for c in range(9):
                    if sudoku[r][c] != 0:
                        continue

                    all_filled = False
                    for a in range(1, 10):
                        if SudokuController.number_is_valid(sudoku, r, c, a):
                            sudoku[r][c] = a
                            if dfs():
                                return True
                            sudoku[r][c] = 0
                    return False
            
            if all_filled:
                solutions.append(copy.deepcopy(sudoku))
                if limit != 0 and len(solutions) >= limit:
                    return True
            
            return False

        dfs()
        return solutions



    @staticmethod
    def generate_random_starting_sudoku() -> list[list[int]]:
        sudoku = SudokuController.generate_random_solved_sudoku()

        filled_squares = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(filled_squares)
        print(filled_squares)

        # self.
        # for r, c in filled_squares:
            


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


    
        
    
        