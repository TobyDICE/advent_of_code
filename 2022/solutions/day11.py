import os
from copy import deepcopy
import numpy as np
os.chdir('../inputs')
os.getcwd()
from day11monkeys import monkeys as monkeys_raw


monkeys =  deepcopy(monkeys_raw)
rounds = range(20)
for round in rounds:
    for monkey in range(8):
        for item in monkeys[monkey]['start_items']:
            monkeys[monkey]['n_inspections'] += 1
            worry_level = monkeys[monkey]['operation'](item)//3
            pass_to = monkeys[monkey]['test'](worry_level)
            monkeys[pass_to]['start_items'].append(worry_level)
        monkeys[monkey]['start_items'] = []


n_inpections =  [monkeys[i]['n_inspections'] for i in range(8)]
n_inpections.sort()
print(f' Part 1: {n_inpections[-1] * n_inpections[-2]}')



# Part 2:
worry_vector = np.array([2, 7, 3, 17, 11, 19, 5, 13])

monkeys =  deepcopy(monkeys_raw)
for monkey in range(8):
    monkeys[monkey]['start_items'] = [worry_level%worry_vector for worry_level in monkeys[monkey]['start_items']]

rounds = range(10000)
for round in rounds:
    for monkey in range(8):
        for item in monkeys[monkey]['start_items']:
            monkeys[monkey]['n_inspections'] += 1
            worry_level = monkeys[monkey]['operation'](item)%worry_vector
            pass_to = monkeys[monkey]['test'](worry_level[monkey])
            monkeys[pass_to]['start_items'].append(worry_level)
        monkeys[monkey]['start_items'] = []


n_inpections =  [monkeys[i]['n_inspections'] for i in range(8)]
n_inpections.sort()
print(f' Part 2: {n_inpections[-1] * n_inpections[-2]}')



