f = open("../inputs/day2.txt", "r")


strategy = [line.strip('\n') for line in f]


# Part 1:
possibilities = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,

    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,

    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
}

solution = sum([possibilities[matchup] for matchup in strategy])
print(f'Part 1 Score: {solution}')

# Part 2:
possibilities2 = {
    'A X': 0 + 3,
    'A Y': 3 + 1,
    'A Z': 6 + 2,

    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,

    'C X': 0 + 2,
    'C Y': 3 + 3,
    'C Z': 6 + 1,
}
solution2 = sum([possibilities2[matchup] for matchup in strategy])
print(f'Part 2 Score: {solution2}')
