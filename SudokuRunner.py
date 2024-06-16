import copy
import json

from SudokuChecker import SudokuChecker
from SudokuGenerator import SudokuGenerator
from SudokuHelpers import print_array_stats, print_sudoku, Timing, get_n_filled_squares, \
    print_sudoku_stats
from SudokuSolver import SudokuSolver
from SudokuStrategies import basic_backtracking, opt1_backtracking, opt2_backtracking, opt3_backtracking, constraint1, \
    opt4_backtracking, opt5_backtracking, constraint2, constraint3, constraint4

if __name__ == "__main__":
    SUDOKU_SIZE = 3
    NUM_PROBLEMS_TO_GEN = 0
    SHOW_GEN_TIMES = False
    SUDOKUS_FROM_FILE = True
    NUM_PROBLEMS_TO_SOLVE = 0
    SHOW_VERIFICATIONS = True
    SHOW_SOLVE_TIMES = True
    SHOW_PROBLEMS_AND_SOLUTIONS = True
    SUDOKU_STRATEGY = constraint4

    checker = SudokuChecker()
    generator = SudokuGenerator(size=SUDOKU_SIZE)
    solver = SudokuSolver(SUDOKU_STRATEGY)
    problems = []

    if SUDOKUS_FROM_FILE:
        # get sudokus from file
        with open("starting_sudokus.txt", "r") as sudoku_file:
            for line in sudoku_file:
                problems.append(json.loads(line))

        print_sudoku_stats(problems)
    else:
        # generate new sudokus
        for i in range(NUM_PROBLEMS_TO_GEN):
            generator_times = []
            with Timing(add_to=generator_times):
                problem = generator.generate_random_starting_sudoku()
            problems.append(copy.deepcopy(problem))

            if SHOW_GEN_TIMES:
                print_array_stats("gentimes", generator_times)

        filled_squares = [get_n_filled_squares(p) for p in problems]
        print_array_stats("empty squares", filled_squares)

    # time the solving the sudokus
    solutions = []
    solve_times = []

    if NUM_PROBLEMS_TO_SOLVE != 0:
        for problem in problems[:NUM_PROBLEMS_TO_SOLVE]:
            with Timing(add_to=solve_times):
                solution = solver.solve_sudoku(problem)
            solutions.append(solution)
    else:
        for problem in problems:
            with Timing(add_to=solve_times):
                solution = solver.solve_sudoku(problem)
            solutions.append(solution)

    if SHOW_PROBLEMS_AND_SOLUTIONS:
        for i in range(len(solutions)):
            print_sudoku(problems[i])
            print_sudoku(solutions[i])

    results = checker.verify_many_solutions(problems[:len(solutions)], solutions)

    if SHOW_VERIFICATIONS:
        for verified, msg in results:
            if not verified:
                print(msg)
            else:
                print("VERIFIED")

    if SHOW_SOLVE_TIMES:
        print_array_stats("solve time", solve_times)
