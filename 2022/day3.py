import numpy as np
f = open("day3.txt", "r")


bags = [line.strip('\n') for line in f]



def half_string(string):
    '''Split a string down the middle'''
    return string[:len(string)//2], string[len(string)//2:]
        


def common_item(string1, string2):
    '''return the common character between 
    strings'''
    return ''.join([char for char in string1 if char in string2][0])



alphabet_lower = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

alphabet_upper = [letter.upper() for letter in alphabet_lower]

alphabet_full = alphabet_lower + alphabet_upper

alphabet_scores = {
    alphabet_full[i]:i+1 for i in range(52)}

answer1 = sum([alphabet_scores[common_item(
    half_string(bag)[0],
    half_string(bag)[1]
)] for bag in bags])


# part 2:

elf_groupings = np.array(bags).reshape(100,3)

def common_items_3way(a,b,c):
    return ''.join([char for char in a if char in b and char in c][0])

badges = [common_items_3way(
    grouping[0], grouping[1], grouping[2]
) for grouping in elf_groupings]

answer2 = sum([alphabet_scores[badge] for badge in badges])