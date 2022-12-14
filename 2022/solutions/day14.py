import numpy as np
from functools import reduce

f = open("../inputs/day14.txt", "r")

rock_mappings = [line.strip('\n') for line in f]

def parse_rock_mappings(input_row):
    inter =  input_row.split(' -> ')
    return [eval(pair) for pair in inter]

rock_mappings = [parse_rock_mappings(row) for row in rock_mappings]

# What shape is our grid?
all_coords = sum(rock_mappings, start = [])
x_coords = [coord[0] for coord in all_coords]
y_coords = [coord[1] for coord in all_coords]

x_max = max(x_coords) 
y_max = max(y_coords) 

cave = np.zeros((x_max+1, y_max+1)).astype(str)
cave[cave == '0.0'] = '.'
cave[500, 0] = '+'




# Build cave

def build_rock_line(coord1, coord2, cave):
    cave[
        min(coord1[0], coord2[0]):max(coord1[0], coord2[0])+1, 
        min(coord1[1], coord2[1]):max(coord1[1], coord2[1])+1
        ] = '#'
    return cave



for rock in rock_mappings:
    for i in range(len(rock)-1):
        cave = build_rock_line(rock[i], rock[i+1], cave)






# Drop in Sand

def check_below(coordinate, map, x_distance = 0):
    return map[
        coordinate[0] + x_distance,
        coordinate[1] + 1]


def update_cave(latest_cave):
    sand_pos = np.where(latest_cave == '+')

    def update_spaces_below(latest_cave, sand_pos):

        try:
            bl = check_below(sand_pos, latest_cave, -1)
        except:
            bl = 'e'
        
        try:
            b = check_below(sand_pos, latest_cave)
        except:
            b = 'e'

        try:
            br = check_below(sand_pos, latest_cave, 1)
        except:
            br = 'e'

        spaces_below = [
            bl,
            b,
            br
        ]
        return spaces_below


    spaces_below = update_spaces_below(latest_cave, sand_pos)
    if spaces_below[1] == '~':
        print('Cave is now full!')
        return latest_cave

    for height in range(latest_cave.shape[1]-1):
        if spaces_below[1] == '.':
            sand_pos = (sand_pos[0], sand_pos[1] + 1)
            spaces_below = update_spaces_below(latest_cave, sand_pos)
        
        elif spaces_below[1] in ['#', 'O'] and spaces_below[0] == '.':
            sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
            spaces_below = update_spaces_below(latest_cave, sand_pos)

        elif spaces_below[0] in ['#', 'O'] and spaces_below[1] in ['#', 'O'] and spaces_below[2] == '.':
            sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
            spaces_below = update_spaces_below(latest_cave, sand_pos)

        elif '.' not in spaces_below:
            if '~' in spaces_below:
                latest_cave[sand_pos] = '~'
                return latest_cave
            latest_cave[sand_pos] = 'O'
            return latest_cave
    
    latest_cave[sand_pos] = '~'
    return latest_cave
    

while cave[np.where(cave == '+')[0], np.where(cave == '+')[1]+1] == '.':
    cave = update_cave(cave)

print(f"Part 1: {np.count_nonzero(cave == 'O')}")

cave = np.zeros((x_max+1, y_max+1)).astype(str)
cave[cave == '0.0'] = '.'
cave[500, 0] = '+'

for rock in rock_mappings:
    for i in range(len(rock)-1):
        cave = build_rock_line(rock[i], rock[i+1], cave)


either_side = np.zeros(cave.shape).astype(str)
either_side[either_side == '0.0'] = '.'
cave = np.append(cave, either_side, axis = 0)
cave = np.append(either_side, cave, axis = 0)


cave = np.append(
    cave, 
    np.array(['.' for space in range(len(cave))]).reshape(cave.shape[0], 1), 
    axis=1)

cave = np.append(
    cave, 
    np.array(['#' for space in range(len(cave))]).reshape(cave.shape[0], 1), 
    axis=1)

last_count = np.count_nonzero(cave == 'O') -1
while last_count != np.count_nonzero(cave == 'O'):
    last_count = np.count_nonzero(cave == 'O')
    cave = update_cave(cave)

print(f"Part 2: {np.count_nonzero(cave == 'O')}")

