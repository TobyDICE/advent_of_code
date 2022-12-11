from numpy import sqrt
monkeys = {
    0: {
        'start_items': [80],
        'operation': lambda x: (5*x),
        'test': lambda x: 4 if x%2 == 0 else 3
    },

    1: {
        'start_items': [75, 83, 74],
        'operation': lambda x: (7 + x),
        'test': lambda x: 5 if x%7 == 0 else 6

    },

    2: {
        'start_items': [86, 67, 61, 96, 52, 63, 73],
        'operation': lambda x: (5 + x),
        'test': lambda x: 7 if x%3 == 0 else 0

    },

    3: {
        'start_items': [85, 83, 55, 85, 57, 70, 85, 52],
        'operation': lambda x: (8 + x),
        'test': lambda x: 1 if x%17 == 0 else 5

    },

    4: {
        'start_items': [67, 75, 91, 72, 89],
        'operation': lambda x: (4 + x),
        'test': lambda x: 3 if x%11 == 0 else 1

    },

    5: {
        'start_items': [66, 64, 68, 92, 68, 77],
        'operation': lambda x: (2*x),
        'test': lambda x: 6 if x%19 == 0 else 2

    },

    6: {
        'start_items': [97, 94, 79, 88],
        'operation': lambda x: (x*x),
        'test': lambda x: 2 if x%5 == 0 else 7

    },

    7: {
        'start_items': [77, 85],
        'operation': lambda x: (6 + x),
        'test': lambda x: 4 if x%13 == 0 else 0

    },
}





for monkey in monkeys.keys():
    monkeys[monkey]['n_inspections'] = 0


rounds = range(20)

for round in rounds:
    for monkey in range(8):

        for item in monkeys[monkey]['start_items']:
            
            monkeys[monkey]['n_inspections'] += 1

            worry_level = monkeys[monkey]['operation'](item)
            pass_to = monkeys[monkey]['test'](worry_level)

            monkeys[pass_to]['start_items'].append(worry_level)

        monkeys[monkey]['start_items'] = []


for i in range(8):
    print(monkeys[i]['n_inspections'])

rounds = range(20)

for round in rounds:
    for monkey in range(8):

        for item in monkeys[monkey]['start_items']:
            
            monkeys[monkey]['n_inspections'] += 1

            worry_level = monkeys[monkey]['operation'](item)
            pass_to = monkeys[monkey]['test'](worry_level)

            monkeys[pass_to]['start_items'].append(worry_level)

        monkeys[monkey]['start_items'] = []


for i in range(8):
    print(monkeys[i]['n_inspections'])





def vectorise_worry(number):
    to_modulo = np.array([2, 7, 3, 17, 11, 19, 5, 13])
    return number%to_modulo
    
def revectorise_worry(worry_vector):
    to_modulo = np.array([2, 7, 3, 17, 11, 19, 5, 13])
    return np.array(worry_vector) % to_modulo


worry_vector = np.array([2, 7, 3, 17, 11, 19, 5, 13])


for monkey in range(8):
    monkeys[monkey]['start_items'] = [worry_level%worry_vector for worry_level in monkeys[monkey]['start_items']]
    monkeys[monkey]['n_inspections'] = 0

rounds = range(10000)
for round in rounds:
    for monkey in range(8):

        for item in monkeys[monkey]['start_items']:
            monkeys[monkey]['n_inspections'] += 1

            worry_level = monkeys[monkey]['operation'](item)%worry_vector

            pass_to = monkeys[monkey]['test'](worry_level[monkey])


            monkeys[pass_to]['start_items'].append(worry_level)

        monkeys[monkey]['start_items'] = []

for i in range(8):
    print(monkeys[i]['n_inspections'])





tst6 = vectorise_worry(6)

tst10 = revectorise_worry(4 + tst6)

tst100 = revectorise_worry(10 * tst10)

tst200 = revectorise_worry(2 * tst100)
tst200
vectorise_worry(200)



