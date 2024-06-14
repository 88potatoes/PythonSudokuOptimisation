import SudokuHelpers


class SudokuChecker:

    @staticmethod
    def verify_solution(self, problem: list[list[int]], solution: list[list[int]]) -> tuple[bool, str]:
        """
        Check if a sudoku has been solved.
        """
        # first check if all the numbers in the problem are found in the same location as the solution
        for r in range(9):
            for c in range(9):
                if problem[r][c] == 0:
                    continue
                if problem[r][c] != solution[r][c]:
                    return False, f"problem[{r}][{c}] = {problem[r][c]}, solution[{r}][{c}] = {solution[r][c]} which are not the same"

        # check rows
        for i in range(9):
            row = set(solution[i])
            if len(row) != 9 or 0 in row:
                return False, f"Duplicate number in row {i}."

        # check columns
        for i in range(9):
            col = set([solution[x][i] for x in range(9)])
            if len(col) != 9 or 0 in col:
                return False, f"Duplicate number in column {i}."

        # check squares
        for i in range(3):
            for j in range(3):
                s = set()
                for k in range(3):
                    for l in range(3):
                        s.add(solution[3 * j + l][3 * i + k])
                if len(s) != 9 or 0 in s:
                    return False, f"Duplicate number in 3x3 square starting at (r={3 * j}, c={3 * i})."

        return True, ""

    def sudoku_state_is_valid(self, sudoku: list[list[int]]) -> bool:
        for r in range(9):
            for c in range(9):
                if sudoku[r][c] == 0:
                    continue
                val = sudoku[r][c]
                sudoku[r][c] = 0
                if not SudokuHelpers.number_is_valid(sudoku, r, c, val):
                    return False
                sudoku[r][c] = val

        return True
