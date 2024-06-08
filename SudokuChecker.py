import SudokuHelpers

def sudoku_is_solved(board: list[list[int]]) -> bool:
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

def sudoku_state_is_valid(sudoku: list[list[int]]) -> bool:
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