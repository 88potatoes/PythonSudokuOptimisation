## This repo follows the Quick Sudoku Solver series on Medium.

### Read the articles:
- [Part 1:](https://medium.com/@spooky_man/quick-sudoku-solver-pt-1-eb9a748e3e7a) Laying the groundwork

Some thing to look into:
- Shaving
- System Verilog Constraint
- https://ai.dmi.unibas.ch/_files/teaching/fs13/ki/material/ki10-sudoku-inference.pdf
- https://www.dbai.tuwien.ac.at/research/project/arte/sudoku/paper.pdf
- https://info.bb-ai.net/student_projects/project_reports/Henry-Davies-Killer-Sudoku.pdf
- hill climbing solutions


Things to talk about in the next article:
1. optimised generator
  - beforehand, the generator had an average of 36 empty squares and a standard deviation of about 8
  - now the generator produces sudokus with an average of 55 squares with a standard deviation of <1
  - is a lot slower
    - before (100 runs)
      - mean gen time: 0.02375178098678589
      - stdev gen time: 0.039746322263617254
      - mean empty squares: 35.28
      - stdev empty squares: 9.490111812946266
    - after (10 runs):
      - mean gen time: 3.1263929128646852
      - stdev gen time: 4.8535482937463215
      - mean empty squares: 53.6
      - stdev empty squares: 1.4298407059684815
  - change: don't return sudoku  immediately when it removes a square which results in duplicate solution; instead just go on to the next square
  - theres a tradeoff between harder sudoku and generated sudokus
  - 