import numpy as np
f = open("../inputs/day17.txt", "r")
moves = [line.strip('\n') for line in f][0]

n_moves = len(moves)

# Create array that's big enough:
grid = np.zeros([7000, 7])
grid = grid.astype('str')

grid[grid == '0.0'] = '.'

# Build the floor
grid[-1] = '#'

shape0 = np.array([
    [ '.', '.', '.', '.',],
    [ '.', '.', '.', '.',],
    [ '.', '.', '.', '.',],
    [ '#', '#', '#', '#',]
])

shape1 = np.array([
    [ '.', '.', '.', ],
    [ '.', '#', '.', ],
    [ '#', '#', '#', ],
    [ '.', '#', '.', ]
])

shape2 = np.array([
    ['.', '.', '.',],
    ['.', '.', '#',],
    ['.', '.', '#',],
    ['#', '#', '#',]
])

shape3 = np.array([
    ['#',],
    ['#',],
    ['#',],
    ['#',]
])

shape4 = np.array([
    ['.', '.',],
    ['.', '.',],
    ['#', '#',],
    ['#', '#',]
])


shapes = {
    0: shape0,
    1: shape1,
    2: shape2,
    3: shape3,
    4: shape4
}

highest_object = min(np.where(grid == '#')[0])

steps = 5
for step in range(steps):
    next_shape = shapes[step%5]
    grid[highest_object-7:highest_object-3, 2:2+next_shape.shape[1]] = next_shape
    shape_not_settled = True
    while shape_not_settled:


