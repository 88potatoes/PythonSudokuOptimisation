import json
import time
from pprint import pprint

import numpy as np

from SudokuChecker import SudokuChecker
from SudokuGenerator import SudokuGenerator
from SudokuHelpers import get_n_empty_squares, print_mean_and_stdev, print_sudoku
from SudokuSolver import SudokuSolver
from SudokuStrategies import basic_backtracking

if __name__ == "__main__":
    checker = SudokuChecker()
    generator = SudokuGenerator()
    solver = SudokuSolver(basic_backtracking)

    generator_times = []
    problems = []
    NUM_PROBLEMS = 100
    SUDOKUS_FROM_FILE = True

    if SUDOKUS_FROM_FILE:
        # get sudokus from file
        with open("starting_sudokus.txt", "r") as sudoku_file:
            for line in sudoku_file:
                problems.append(json.loads(line))
    else:
        # generate new sudokus
        # TODO maybe i can do one of the the '@' thingos to keep track of time
        for i in range(NUM_PROBLEMS):
            startgen = time.time()
            problem = generator.gen_many_starting_sudokus(1)
            endgen = time.time()
            generator_times.append(endgen - startgen)
            problems.append(problem[0])

        print_mean_and_stdev("gentimes", generator_times)

        zeroes = [get_n_empty_squares(p) for p in problems]
        print_mean_and_stdev("empty squares", zeroes)

    # time the solutions to solving the sudokus
    solutions = []
    solve_times = []
    for problem in problems:
        start_time = time.time()
        solution = solver.solve_sudoku(problem)
        end_time = time.time()

        solutions.append(solution)
        solve_times.append(end_time - start_time)

    results = checker.verify_many_solutions(problems, solutions)

    for verified, msg in results:
        if not verified:
            print(msg)
    print_mean_and_stdev("solve time", solve_times)
    
        