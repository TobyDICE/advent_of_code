f = open("../inputs/day13.txt", "r")

signal_full = [line.strip('\n') for line in f]
signal_full = [line for line in signal_full if line != '']

signal_left = [eval(signal_full[i]) for i in range(len(signal_full)) if i%2 ==0]
signal_right = [eval(signal_full[i]) for i in range(len(signal_full)) if (i+1)%2 ==0]

def is_pair_correctly_ordered(signal1, signal2):

    if type(signal1) == type(signal2) == int:
        if signal1 != signal2:
            return signal1 < signal2
    
    if (type(signal1) == int) & (type(signal2) == list):
        signal1 = [signal1]
        return is_pair_correctly_ordered(signal1, signal2)

    if (type(signal2) == int) & (type(signal1) == list):
        signal2 = [signal2]
        return is_pair_correctly_ordered(signal1, signal2)

    if type(signal1) == type(signal2) == list:
        s1_length = len(signal1)
        s2_length = len(signal2)
        for pair in zip(signal1, signal2):
            res = is_pair_correctly_ordered(pair[0], pair[1]) 
            if res in [True, False]:
                return res
                
        if s1_length < s2_length:
            return True

        if s1_length > s2_length:
            return False
    


indexer = {}

for i in range(len(signal_left)):
    indexer[i+1] = is_pair_correctly_ordered(signal_left[i], signal_right[i])

print(f'Part 1: {sum([index for index in indexer if indexer[index]])}')


# Part 2:
signal_full = signal_left + signal_right


less_than_2 = [signal for signal in signal_full if is_pair_correctly_ordered(signal, [2])]
less_than_6 = [signal for signal in signal_full if is_pair_correctly_ordered(signal, [6])]


print(f'Part 2: {(len(less_than_2) + 1) * (len(less_than_6)+2)}')






