import numpy as np
from copy import deepcopy
f = open("../inputs/day9.txt", "r")

H_movements = [line.strip('\n') for line in f]

def which_direction_will_head_move(head, instruction):
    instruction = instruction.split(' ')  

    head_new = head

    if instruction[0] == 'R':
        head_new = head_new[0] + 1, head_new[1]
    if instruction[0] == 'L':
        head_new = head_new[0] - 1, head_new[1]
    if instruction[0] == 'U':
        head_new = head_new[0], head_new[1] + 1
    if instruction[0] == 'D':
        head_new = head_new[0], head_new[1] - 1
    return head_new


def how_will_tail_move(head_new, tail_current):

    x_diff = head_new[0] - tail_current[0]
    x_diff_abs = np.abs(x_diff)
    y_diff = head_new[1] - tail_current[1]
    y_diff_abs = np.abs(y_diff)

    if all([x_diff_abs < 2, y_diff_abs < 2]):
        return tail_current

    if x_diff_abs + y_diff_abs == 3:
        x_movement, y_movement = np.sign(x_diff), np.sign(y_diff)
    
    else:
        x_movement, y_movement = int(x_diff/2), int(y_diff/2)

    return tail_current[0] + x_movement, tail_current[1] + y_movement


def iterate_with_n_knots(n_knots, instructions):
    positions_current = [(0,0) for knot in range(n_knots)]
    positions_new = positions_current
    res = {0: [positions_current]}
    counter = 0

    for instruction in instructions:

        for steps in range(int(instruction.split(' ')[1])):
            
            h_pos_new = which_direction_will_head_move(positions_current[0], instruction)
            positions_new[0] = h_pos_new

            for follower_knot in range(1, n_knots):

                positions_new[follower_knot] = how_will_tail_move(
                    positions_new[follower_knot-1],
                    positions_new[follower_knot]
                    )
    
            res[counter] = [deepcopy(positions_new)]

            positions_current = deepcopy(positions_new)
            counter+=1
            
    tail_positions = set([res[key][0][-1] for key in res])
    return len(tail_positions)

print(f'Part 1: {iterate_with_n_knots(2, H_movements)}')
print(f'Part 2: {iterate_with_n_knots(10, H_movements)}')



