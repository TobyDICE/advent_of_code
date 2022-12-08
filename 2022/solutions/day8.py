import numpy as np

f = open("../inputs/day8.txt", "r")


trees = [[int(number) for number in line.strip('\n')] for line in f]
trees = np.array(trees)

trees[0, :]
trees[:, 0]


def check_tree_is_visible(forest, y, x):

    tree_height = forest[x,y]
    
    up = forest[:x, y]
    down = forest[x+1:, y]
    left = forest[x, :y]
    right = forest[x, y+1:]

    # print(up)
    # print(down)
    # print(left)
    # print(right)

    for section in [up, down, left, right]:
        # print(f'section: {section}: {len(section)}')
        if len(section) == 0:
            return True
        if max(section) < tree_height:
            return True
    # print(f'visible: {x,y}')
    return False






number_visible = 0
for col in range(99):
    for row in range(99):
        number_visible += int(check_tree_is_visible(trees, col, row))

print(number_visible)


def get_scenic_score(forest, y, x):

    tree_height = forest[x,y]
    
    up = np.flip(forest[:x, y])
    down = forest[x+1:, y]
    left = np.flip(forest[x, :y])
    right = forest[x, y+1:]

    # print(up)
    # print(down)
    # print(left)
    # print(right)

    counters = []
    for section in [up, down, left, right]:
        # print(f'section: {section}')
        current_distance = 0
        if len(section) == 0:
            counters.append(current_distance)

        else:
            for tree in section:
                # print(f'tree {tree}')
                current_distance += 1
                if tree >= tree_height:
                    counters.append(current_distance)
                    # print('appending because tall tree found')
                    break

            if tree_height > max(section):
                counters.append(len(section))
                # print('appending because no tall trees found')
                # print(f'tree height {tree_height}')
                # print(f'max(section): {max(section)}')
    


    # print(counters)
            
    return np.prod(counters)




reigning_max = 0
coords =  (0,0)
for col in range(99):
    for row in range(99):
        current = get_scenic_score(trees, col, row)
        if current > reigning_max:
            reigning_max = current
            coords = (col, row)
        



print(reigning_max)





