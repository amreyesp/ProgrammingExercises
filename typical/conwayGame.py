"""Conway Game of Life"""

"""
Initially, there is a grid with some cells which may be alive or dead.
Our task to generate the next generation of cells based on the following rules:
1. Any live cell with fewer than two live neighbors dies, as if caused by under population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""

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
    #evaluate if some neighbour doesn't make sense (neighbour index is out of the grid range)
    for i in range(8): #8 is the number of neighbours
        _x = neighborhood[i,0] #acces to x coord of the ith neighbour
        _y = neighborhood[i,1] #acces to y coord of the ith neighbour
        #if coord is out of range is not a real neighbour (0)
        if _x <0 or _x >rows-1 or _x >cols-1 or _y <0 or _y >rows-1 or _y >cols-1:
            neighbours_values[i] = 0
        else: #otherwise the grid is evaluated to define if there is a neighbour
            neighbours_values[i] = grid[_x,_y]
    return neighbours_values


def count_neighbours(grid):
    for index, x in np.ndenumerate(grid):
        neighbours[index]=sum(choose_neighbours(grid,index))
    return neighbours


def next_generation(grid,neighbours):
    for index,cell in np.ndenumerate(grid):
        if cell == 1: # Any live cell...
            #case 1. ...with fewer than two live neighbors dies and
            #case 3. ...with more than three live neighbors dies.
            if neighbours[index] < 2 or neighbours[index] > 3:
                grid[index] = 0
            #case 2. ...with two or three live neighbors lives => is the default entry case
        else:
            #case 4. Any dead cell with exactly three live neighbors becomes a live cell
            if neighbours[index] == 3:
                grid[index] = 1


"""Main script"""

import numpy as np

cols = 4
rows = 4
grid = np.array([[1,0,0,1],[0,1,0,1],[0,0,0,0],[0,0,0,1]])
neighbours = np.copy(grid) #just to keep the same grid size

neighbours = count_neighbours(grid)
print(grid)
print("********")
print(neighbours)
print("********")
next_generation(grid,neighbours)
print(grid)
