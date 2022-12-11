monkeys = {
    0: {
        'start_items': [80],
        'operation': lambda x: (5*x),
        'test': lambda x: 4 if x%2 == 0 else 3,
        'n_inspections': 0
    },

    1: {
        'start_items': [75, 83, 74],
        'operation': lambda x: (7 + x),
        'test': lambda x: 5 if x%7 == 0 else 6,
        'n_inspections': 0

    },

    2: {
        'start_items': [86, 67, 61, 96, 52, 63, 73],
        'operation': lambda x: (5 + x),
        'test': lambda x: 7 if x%3 == 0 else 0,
        'n_inspections': 0

    },

    3: {
        'start_items': [85, 83, 55, 85, 57, 70, 85, 52],
        'operation': lambda x: (8 + x),
        'test': lambda x: 1 if x%17 == 0 else 5,
        'n_inspections': 0

    },

    4: {
        'start_items': [67, 75, 91, 72, 89],
        'operation': lambda x: (4 + x),
        'test': lambda x: 3 if x%11 == 0 else 1,
        'n_inspections': 0

    },

    5: {
        'start_items': [66, 64, 68, 92, 68, 77],
        'operation': lambda x: (2*x),
        'test': lambda x: 6 if x%19 == 0 else 2,
        'n_inspections': 0

    },

    6: {
        'start_items': [97, 94, 79, 88],
        'operation': lambda x: (x*x),
        'test': lambda x: 2 if x%5 == 0 else 7,
        'n_inspections': 0

    },

    7: {
        'start_items': [77, 85],
        'operation': lambda x: (6 + x),
        'test': lambda x: 4 if x%13 == 0 else 0,
        'n_inspections': 0

    },
}