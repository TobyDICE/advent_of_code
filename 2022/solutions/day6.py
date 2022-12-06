f = open("../inputs/day6.txt", "r")

raw_signal = ''.join(f)

def find_first_unique_window(signal, n_unique_characters_needed):
    characters_counted = 0
    n_windows = len(signal) - n_unique_characters_needed

    for char in range(n_windows):
        if len(
            set(
                [char for char in signal[:n_unique_characters_needed]]
                )) == n_unique_characters_needed:
            return characters_counted + n_unique_characters_needed
        else:
            signal = signal[1:]
            characters_counted +=1



print(f'Part 1 answer: {find_first_unique_window(raw_signal, 4)}')
print(f'Part 1 answer: {find_first_unique_window(raw_signal, 14)}')