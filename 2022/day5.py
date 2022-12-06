import numpy as np

# Will formulate the problem as 9 lists. Left to right is bottom to top.

# Read in crate data:
f = open("day5.txt", "r")

crates_raw = [line.strip('\n') for line in f][:8]

def clean_crate_data(crate_data):
    # Reshape data:
    crates_reshaped = [
        [crate_data[row][col] for row in range(7, -1 , -1)] 
            for col in range(len(crate_data[0]))
        ]
        
    # Clean out junk
    crates_cleaned = [
        [char for char in crates_reshaped[row] if char.isalpha()
        ] for row in range(len(crates_reshaped))]
        
    crates = [row for row in crates_cleaned if row != []]
    return crates

crates = clean_crate_data(crates_raw)
crates
# Looks beautiful now.


# Read in and clean up instructions:
f = open("day5.txt", "r")
instructions = [line.strip('\n') for line in f][10:]

def clean_instruction_line(instruction_line):
    instruction_line_split = instruction_line.split(' ')
    instruction_line_numbers_only = [
        int(string) for string in instruction_line_split if string.isdigit()
    ]
    return instruction_line_numbers_only
    
instructions = [clean_instruction_line(line) for line in instructions]

# Apply instructions:


# ## For part 1:
# For each instruction line:
for instruction in instructions:
    # We apply movements for this number of crates:
    for crate in range(instruction[0]):
        crates[instruction[2]-1].append(crates[instruction[1]-1].pop(-1))

print(''.join([stack[-1] for stack in crates]))



## For part 2: 

# Reset crates:
crates = clean_crate_data(crates_raw)
# For each instruction line:
for instruction in instructions:
    # We apply movements for this number of crates:
    crates[instruction[2]-1] += (crates[instruction[1]-1][-instruction[0]:])
    del crates[instruction[1]-1][-instruction[0]:]

print(''.join([stack[-1] for stack in crates]))