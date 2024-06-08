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

    def sudoku_is_solved(self, board: list[list[int]]) -> bool:
        """
        Check if a sudoku has been solved.
        PURE
        """

        # check rows
        for i in range(9):
            row = set(board[i])
            if len(row) != 9 or 0 in row:
                return False
        
        # check columns
        for i in range(9):
            col = set([board[x][i] for x in range(9)])
            if len(col) != 9 or 0 in col:
                return False
            
        # check squares
        for i in range(3):
            for j in range(3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        s.add(board[3*j+l][3*i+k])
                if len(s) != 9 or 0 in s:
                    return False
        
        return True

    def number_is_valid(self, board: list[list[int]], r: int, c: int, a: int) -> bool:
        """
        Check if a particular number at a certain square is valid.
        PURE
        """

        # check the row
        if a in set(board[r]):
            return False
        
        # check the column
        if a in set([board[y][c] for y in range(9)]):
            return False
        
        # check the squares
        rstart = r // 3
        cstart = c // 3
        for dr in range(3):
            for dc in range(3):
                if a == board[3*rstart + dr][3*cstart + dc]:
                    return False
        return True

    def solve_sudoku(self, sudoku: list[list[int]]):
        """
        Solves sudoku
        mutates self._solutions
        but start and end is the same state
        """
        self._solutions = []
        sudoku_copy = copy.deepcopy(sudoku)
        self._solve_sudoku_helper(sudoku_copy)
        # print("-")
        # pprint(self._solutions)
        # print("-")
        solutions = self._solutions.copy()
        pprint(solutions)
        self._solutions = []
        return solutions
    
    def _solve_sudoku_helper(self, sudoku: list[list[int]]):
        print("-", end="")
        # assert self._early_cutoff >= 0
        # pprint(sudoku)
        all_filled = True
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] != 0:
                    continue

                all_filled = False
                for a in range(1, 10):
                    if self.number_is_valid(sudoku, r, c, a):
                        sudoku[r][c] = a
                        if self._solve_sudoku_helper(sudoku):
                        # self._solve_sudoku_helper(sudoku)
                            return True
                        sudoku[r][c] = 0
                return False
            
        if all_filled:
            s = tuple(tuple(row) for row in sudoku)
            self._solutions.append(s)

        if self._early_cutoff > 0 and len(self._solutions) >= self._early_cutoff:
            return True

        return False
    
    def get_random_solved_sudoku():
        sudoku = [[0 for _ in range(9)] for _ in range(9)]
        def dfs(board: list[list[int]]):
            for r in range(9):
                for c in range(9):
                    candidates = [x for x in range(9)]
                    random.shuffle(candidates)

                    for a in candidates:
                        pass # TODO

    def _get_random_solved_sudoku(sudoku: list[list[int]]):





    def generate_sudoku(self) -> list[list[int]]:
        sudoku = [[0 for _ in range(9)] for _ in range(9)]

        empty_squares = set()
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] == 0:
                    empty_squares.add((r, c))

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
        self._early_cutoff = 1
        solution_sudoku = self.solve_sudoku(sudoku)[0]
        self._early_cutoff = 0
        
        pprint(solution_sudoku)

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

    def sudoku_is_valid(self, sudoku: list[list[int]]) -> bool:
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] == 0:
                    continue
                val = sudoku[r][c]
                sudoku[r][c] = 0
                if not self.number_is_valid(sudoku, r, c, val):
                    return False
                sudoku[r][c] = val
        
        return True

sudokuController = SudokuController()
# pprint(sudokuController.solve_sudoku(SUDOKU2))
# pprint(sudokuController.sudoku_is_valid(SUDOKU2))
pprint(sudokuController.generate_sudoku())


    
        
    
        