from pprint import pprint
from SudokuChecker import SudokuChecker
from SudokuGenerator import SudokuGenerator
from SudokuSolver import SudokuSolver
from SudokuStrategies import basic_backtracking
import time

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

if __name__ == "__main__":
    checker = SudokuChecker()
    generator = SudokuGenerator()
    solver = SudokuSolver(basic_backtracking)

    # get a problem sudoku
    # problem_sudoku = generator.generate_random_starting_sudoku()
    # pprint(problem_sudoku)
    # print("Problem:")
    problems = generator.gen_many_starting_sudokus(100)
    # zeros = 0
    # for r in range(9):
    #     for c in range(9):
    #         if sudoku[r][c] == 0:
    #             zeros += 1
    # print(zeros)

    # get a solution to the sudoku
    start_time = time.time()
    solutions = solver.solve_many_sudokus(problems)
    end_time = time.time()
    # print("Solution")
    # pprint(solved_sudoku)

    # verify the sudoku is a solution
    # verified, status = checker.verify_solution(problem_sudoku, solved_sudoku)
    results = checker.verify_many_solutions(problems, solutions)

    for verified, msg in results:
        if not verified:
            print(msg)
    print(f"Time elapsed: {end_time - start_time}s")

    
        