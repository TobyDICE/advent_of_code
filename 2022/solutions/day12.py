import numpy as np
import string
from matplotlib import pyplot as plt
# Read in crate data:
f = open("../inputs/day12.txt", "r")

contours = [line.strip('\n') for line in f]
alphabet = {list(string.ascii_lowercase)[i]: i for i in range(26)}
contours = [[alphabet.get(char, char) for char in line] for line in contours]
contours = np.array(contours)
start = np.where(contours == 'S')
end = np.where(contours == 'E')
contours[start] = 0
contours[end] = 25
contours = contours.astype(int)


def is_step_possible(new_height, current_height):
    return new_height - current_height <= 1

def list_adjacent_points(point, map):
    x, y = point[0], point[1]
    min_x, min_y = 0, 0
    max_x, max_y = len(map), len(map[0])

    full_list = [
        [x, y+1],
        [x, y-1],
        [x+1, y],
        [x-1, y]
    ]

    edge_checks = lambda px, py: (px in range(min_x, max_x)) & (py in range(min_y, max_y))

    return [point for point in full_list if edge_checks(point[0], point[1])]


def return_list_of_reachable_points(point, map):
    full_list = list_adjacent_points(point, map)
    reachable = [destination for destination in full_list if is_step_possible(
        map[destination[0], destination[1]],
        map[point[0], point[1]]
        )]
    return tuple(reachable)


def calculate_min_steps_needed(start, end, map):
    reached = np.zeros(map.shape)
    reached[start] = 1

    reachable_per_step = {
        0: [start]
        }

    def update_reachable_per_step():
        to_iterate_from = max(reachable_per_step.keys())
        reachable_per_step[to_iterate_from+1] = []
        for location in reachable_per_step[to_iterate_from]:
            if reached[tuple(location)] != 1:
                reached[tuple(location)] = 1
            reachable = return_list_of_reachable_points(location, contours)
            reachable = [loc for loc in reachable if not reached[tuple(loc)] ]
            reachable_per_step[to_iterate_from+1] += [i for i in reachable if i not in reachable_per_step[to_iterate_from+1]]
        del reachable_per_step[to_iterate_from]


    while not reached[end]:
        update_reachable_per_step()

    return list(reachable_per_step.keys())[0]

calculate_min_steps_needed(start, end, contours)
print(f'Part 1: {calculate_min_steps_needed(start, end, contours)}')


