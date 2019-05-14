"""Conway Game of Life"""

"""
Initially, there is a grid with some cells which may be alive or dead.
Our task to generate the next generation of cells based on the following rules:
1. Any live cell with fewer than two live neighbors dies, as if caused by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

import numpy as np

grid = np.array([[0,2,0],[0,1,0]])

def print_grid(a):
    print(a)

print_grid(grid)

for row in grid:
    for element in row:
        if element == 0:
            print(".")
        else:
            print("*")
