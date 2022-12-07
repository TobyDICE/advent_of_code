f = open("../inputs/day7.txt", "r")

commands = [line.strip('\n') for line in f ]

def get_current_dir_from_string(full_repo, loc_string):
    current_repo = full_repo['/']
    for command in [dir for dir in loc_string.split('/') if dir != '']:
        current_repo = current_repo[command]
    return current_repo

repo = current = {}
loc_string = ''
for command in commands:
    if command[:4] == '$ cd':
        if command != '$ cd ..':
            loc_string += command[5:] + '/'
            current[command[5:]] = {}
            current = current[command[5:]]
        else:
            loc_string = '/'.join(loc_string.split('/')[:-2]) + '/'
            current = get_current_dir_from_string(repo, loc_string)
    else:
        if command[4:] == '$ ls':
            pass
        
        elif command[:3] == 'dir':
            current[command[4:]] = {}

        elif command.split(' ')[0].isdigit():
            current[command.split(' ')[1]] = int(command.split(' ')[0])


sizes = []


def recursively_get_values(place_in_repo):

    # recursive case:
    if type(place_in_repo) == dict:

        global sizes
        size = sum(
            [recursively_get_values(place_in_repo[key]) for key in place_in_repo.keys()]
            )
        sizes.append(size)
        return size
    
    # base case:
    if type(place_in_repo) == int:
         return place_in_repo
        

recursively_get_values(repo)

print(f'Answer 1: {sum([size for size in sizes if size < 100000])}')

total_space = 70000000
required = 30000000
available = total_space - max(sizes)
to_free = required - available

print(f'Answer 2: {min([num for num in sizes if num > to_free])}')
