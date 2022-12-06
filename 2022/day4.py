def does_a_list_contain_the_other(list1, list2, fully = True):
    if fully:
        return all([
            item in list2 for item in list1])|all([
                item in list1 for item in list2])
    else:
        return any([
            item in list2 for item in list1])|any([
                item in list1 for item in list2])


def convert_allocations_to_lists(allocation):
    range_start, range_end = allocation.split('-')
    return list(range(int(range_start), int(range_end)+1, 1))


f = open("day4.txt", "r")
allocations = [line.strip('\n') for line in f]

answer1 = sum(
    [does_a_list_contain_the_other(
    convert_allocations_to_lists(
        i.split(',')[0],
    ),
    convert_allocations_to_lists(
        i.split(',')[1],
    )
)
    for i in allocations]
)

print(answer1)

answer2 = sum(
    [does_a_list_contain_the_other(
    convert_allocations_to_lists(
        i.split(',')[0],
    ),
    convert_allocations_to_lists(
        i.split(',')[1],
    ),

    False
)
    for i in allocations]
)

print(answer2)