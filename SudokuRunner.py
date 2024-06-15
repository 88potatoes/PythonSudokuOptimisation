import copy
import json
import time
from pprint import pprint

import numpy as np

from SudokuChecker import SudokuChecker
from SudokuGenerator import SudokuGenerator
from SudokuHelpers import get_n_empty_squares, print_array_stats, print_sudoku, Timing, get_n_filled_squares
from SudokuSolver import SudokuSolver
from SudokuStrategies import basic_backtracking

if __name__ == "__main__":
    checker = SudokuChecker()
    generator = SudokuGenerator(size=3)
    solver = SudokuSolver(basic_backtracking)

    problems = []
    NUM_PROBLEMS = 1
    SUDOKUS_FROM_FILE = False

    if SUDOKUS_FROM_FILE:
        # get sudokus from file
        with open("starting_sudokus.txt", "r") as sudoku_file:
            for line in sudoku_file:
                problems.append(json.loads(line))
    else:
        # generate new sudokus
        for i in range(NUM_PROBLEMS):
            generator_times = []
            with Timing(add_to=generator_times):
                problem = generator.generate_random_starting_sudoku()
            problems.append(copy.deepcopy(problem))

            print_array_stats("gentimes", generator_times)

        filled_squares = [get_n_filled_squares(p) for p in problems]
        print_array_stats("empty squares", filled_squares)

    pprint(problems)
    # time the solutions to solving the sudokus
    solutions = []
    solve_times = []
    for problem in problems:
        with Timing(add_to=solve_times):
            print_sudoku(problem)
            solution = solver.solve_sudoku(problem)
        solutions.append(solution)

    results = checker.verify_many_solutions(problems, solutions)

    for verified, msg in results:
        if not verified:
            print(msg)
    print_array_stats("solve time", solve_times)
