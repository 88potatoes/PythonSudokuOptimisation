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

3. 4x4
 - estimated time:
 - 3x3:
   - crude: 9^81 = 1.9662705e+77
   - not checking everything: (9!)*9 = 3265920
   - took: 0.13218548423365542s
 - 4x4:
   - crude: 16^256 = infinity
   - ![img.png](images/img.png)
   - optimised: 16!*16 = 3.3476464e+14
   - estimated time: 3.3476464e+14 / 3265920 = 102502400; 102502400 * 0.13218548423365542s = 13549279.744s = 225821.329067 min = 3763.68881778 hrs = 156.8 days - about half a year
   - hell nah i ain't running that
 
