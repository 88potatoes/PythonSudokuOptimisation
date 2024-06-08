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
    rstart = r // 3
    cstart = c // 3
    for dr in range(3):
        for dc in range(3):
            if a == board[3*rstart + dr][3*cstart + dc]:
                return False
    return True

