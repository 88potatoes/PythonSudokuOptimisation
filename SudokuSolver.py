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

    def solve_many_sudokus(self, sudoku_list: list[list[list[int]]]) -> list[list[list[int]]]:
        return [self.solve_sudoku(sudoku) for sudoku in sudoku_list]