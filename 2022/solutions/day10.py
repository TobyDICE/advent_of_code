import numpy as np
f = open("../inputs/day10.txt", "r")
np.set_printoptions(threshold=np.inf)
inputs = [line.strip('\n') for line in f]

converted_inputs = []
for input in inputs:
    if input == 'noop':
        converted_inputs.append(0)
    else:
        converted_inputs += [0, int(input.split(' ')[1])]

inputs


res = {0:1}

for index in range(len(converted_inputs)):
    res[index+1] = res[index] + converted_inputs[index]


strengths = []
cycles = [20, 60, 100, 140,180,220]

for round in cycles:
    strengths.append(round * res[round-1])


sum(strengths)

# Part 2

pixels = []

for cycle in range(240):
    if res[cycle]%40 in np.array([cycle-1, cycle, cycle+1])%40:
        pixels.append('#')
    else:
        pixels.append('.')


np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)

output = np.array(pixels).reshape(6, 40)

x_str = np.array_repr(output)
print(x_str)

# np.array_repr(output)