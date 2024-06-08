from pprint import pprint
import random

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
    [8, 2, 7, 1, 5, 4, 3, 9, 6],
    [9, 6, 5, 3, 2, 7, 1, 4, 8],
    [3, 4, 1, 6, 8, 9, 7, 5, 2],
    [5, 9, 3, 4, 0, 8, 2, 0, 1],
    [4, 7, 2, 5, 1, 3, 6, 8, 9],
    [6, 1, 8, 9, 7, 2, 4, 3, 5],
    [7, 8, 6, 2, 3, 5, 9, 1, 4],
    [1, 5, 4, 7, 9, 6, 8, 2, 3],
    [2, 3, 9, 8, 4, 1, 5, 6, 7]
]

class SudokuController:

    def __init__(self):
        self._solutions = []

    def sudoku_is_solved(self, board: list[list[int]]) -> bool:
        """
        Check if a sudoku has been solved.
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

    def number_is_valid(self, board: list[list[int]], i: int, j: int, a: int) -> bool:
        """
        Check if a particular number at a certain square is valid.
        """

        # check the row
        if a in set(board[j]):
            return False
        
        # check the column
        if a in set([board[y][i] for y in range(9)]):
            return False
        
        # check the squares
        rstart = j // 3
        cstart = i // 3
        s = set()
        for r in range(3):
            for c in range(3):
                if a == board[3*rstart + r][3*cstart + c]:
                    return False
        return True

    def solve_sudoku(self, sudoku: list[list[int]]):
        self._solutions = []
        self._solve_sudoku_helper(sudoku)
        return self._solutions
    
    def _solve_sudoku_helper(self, sudoku: list[list[int]], early_cutoff=0):
        assert early_cutoff >= 0

        all_filled = True
        for i in range(9):
            for j in range(9):
                if sudoku[j][i] != 0:
                    continue

                all_filled = False
                for a in range(1, 10):
                    if self.number_is_valid(sudoku, i, j, a):
                        sudoku[j][i] = a
                        if self.solve_sudoku(sudoku):
                            return True
                        sudoku[j][i] = 0
                return False
            
        if all_filled:
            s = tuple(tuple(row) for row in sudoku)
            self._solutions.append(s)

        if early_cutoff > 0 and self._solutions == early_cutoff:
            return True

        return False
    

    def generate_sudoku(self) -> list[list[int]]:
        sudoku = [[0 for _ in range(9)] for _ in range(9)]

        empty_squares = set()
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] == 0:
                    empty_squares.add((r, c))
        random_points = random.sample(list(empty_squares), 16)

        # filling with random points initially
        for point in random_points:
            if point not in empty_squares:
                continue

            empty_squares.remove(point)
            for a in range(1, 10):
                if self.number_is_valid(sudoku, point[0], point[1], a):
                    sudoku[point[0]][point[1]] = a
                    break
        
        pprint(sudoku)
        # filling with random points until unique solution
        nsols = len(self.solve_sudoku(sudoku))
        while nsols >= 2:
            pprint(sudoku)
            r, c = random.sample(list(empty_squares), 1)[0]
            empty_squares.remove(point)
            for a in range(1, 10):
                if self.number_is_valid(sudoku, r, c, a):
                    sudoku[r][c] = a
                    break
                nsols = len(self.solve_sudoku(sudoku))
        
        if nsols == 0:
            return None
        return sudoku

sudokuController = SudokuController()
print(sudokuController.generate_sudoku())


    
        
    
        