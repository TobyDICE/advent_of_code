f = open("../inputs/day13test.txt", "r")

signal_full = [line.strip('\n') for line in f]
signal_full = [line for line in signal_full if line != '']

signal_left = [eval(signal_full[i]) for i in range(len(signal_full)) if i%2 ==0]
signal_right = [eval(signal_full[i]) for i in range(len(signal_full)) if (i+1)%2 ==0]

def is_pair_correctly_ordered(signal1, signal2):
    print(f'Comparing {signal1} with {signal2}')

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
        results = []
        for i in range(min(s1_length, s2_length)):
            res = is_pair_correctly_ordered(signal1[i], signal2[i]) 
            if res in [True, False]:
                return res

            
            
        if s1_length < s2_length:
            return True

        if s1_length > s2_length:
            return False
    


indexer = {}

for i in range(len(signal_left)):
    indexer[i+1] = is_pair_correctly_ordered(signal_left[i], signal_right[i])

sum([index for index in indexer if indexer[index]])








indexer