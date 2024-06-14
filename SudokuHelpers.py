def number_is_valid(board: list[list[int]], r: int, c: int, a: int) -> bool:
    """
    Check if a particular number at a certain square is valid.
    """

    # check the row
    if a in set(board[r]):
        return False
    
    # check the column
    if a in set([board[y][c] for y in range(9)]):
        return False
    
    # check the squares
    r_start = r // 3
    c_start = c // 3
    for dr in range(3):
        for dc in range(3):
            if a == board[3*r_start + dr][3*c_start + dc]:
                return False
    return True

