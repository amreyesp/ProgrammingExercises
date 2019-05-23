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
cols = 4
rows = 4
grid = np.array([[1,0,0,1],[0,1,0,1],[0,0,0,0],[0,0,0,1]])
neighbours = np.array([[1,2,2,1],[2,1,3,1],[1,1,2,2],[0,0,1,0]])
neighbours2 = np.zeros(shape=(rows,cols))


def count_neighbours(grid):
    for index, x in np.ndenumerate(grid):
        #choose_neighbours(grid,index)
    print(choose_neighbours(grid,(0,2)))

def choose_neighbours(grid,index):
    neighborhood = np.array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
    neighbours_values = np.array([0,0,0,0,0,0,0,0])
    #calculate all the index (potentially neighbours) of an element
    neighborhood[0,0],neighborhood[0,1] = index[0]-1,index[1]
    neighborhood[1,0],neighborhood[1,1] = index[0]-1,index[1]+1
    neighborhood[2,0],neighborhood[2,1] = index[0],index[1]+1
    neighborhood[3,0],neighborhood[3,1] = index[0]+1,index[1]+1
    neighborhood[4,0],neighborhood[4,1] = index[0]+1,index[1]
    neighborhood[5,0],neighborhood[5,1] = index[0]+1,index[1]-1
    neighborhood[6,0],neighborhood[6,1] = index[0],index[1]-1
    neighborhood[7,0],neighborhood[7,1] = index[0]-1,index[1]-1
    #print("neighborhood",neighborhood)
    #evaluate if some neighbour doesn't make sense (it's index is out of the grid range)
    for i in range(8): #8 is the number of neighbours
        _x = neighborhood[i,0] #acces to x coord of the ith neighbour
        _y = neighborhood[i,1] #acces to y coord of the ith neighbour
        #if coord is out of range it is assumed that is no neighbour (0)
        if _x <0 or _x >rows-1 or _x >cols-1 or _y <0 or _y >rows-1 or _y >cols-1:
            neighbours_values[i] = 0
        else: #otherwise the grid is evaluated to define if there is a neighbour
            neighbours_values[i] = grid[_x,_y]
    #print("neighbours_values",neighbours_values)
    return neighbours_values


def next_generation(grid,neighbours):
    pass

count_neighbors(grid)
print(grid)
print(neighbours2)
