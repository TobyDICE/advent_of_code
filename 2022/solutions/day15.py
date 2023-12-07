import numpy as np

# Read in beacon report:
f = open("../inputs/day15.txt", "r")

report_raw = [line.strip('\n') for line in f]

def isdigit_or_minus(char):
    return char.isdigit() or char == '-'

def parse_report(report_line):
    equals_split = report_line.split('=')[1:]

    locs = [''.join([i for i in j if isdigit_or_minus(i)]) for j in equals_split]
    locs = [int(loc) for loc in locs]

    return [[locs[0], locs[1]], [locs[2], locs[3]]]

def get_manhattan(loc1, loc2):
    x_dist = np.abs(loc1[0] - loc2[0])
    y_dist = np.abs(loc1[1] - loc2[1])
    return x_dist + y_dist



report = []
for line in report_raw:
    report.append(parse_report(line))

for line in report:
    line.append(get_manhattan(line[0], line[1]))


# Iterate through the report, fill in values if we can:
yth = 2000000
yth = 10

def check_where_we_can_rule_out(sensor_coord, reach, yth_row_number):

    # Check vertical distance from yth row:
    v_dist = np.abs(sensor_coord[1] - yth_row_number) 
    if v_dist > reach:

        return [sensor_coord[0], sensor_coord[0]]

    else:

        left_reach = sensor_coord[0] - (reach - v_dist)
        right_reach = (sensor_coord[0] + (reach - v_dist)+1)
        
        return [left_reach, right_reach]


places_we_cant_rule_out = set([i[1][0] for i in report if i[1][1] == yth])

places_to_rule_out = []
for line in report:
    places_to_rule_out.append(check_where_we_can_rule_out(line[0], line[2], yth))



rule_out = []
for coords in places_to_rule_out:
    rule_out += list(range(coords[0], coords[1]))

rule_out = set(rule_out)
print(len(rule_out - places_we_cant_rule_out))


beacons = {}
for i in range(2000):
    if i%1000 == 0:
        print(i)
    places_we_cant_rule_out = set([i[1][0] for i in report if i[1][1] == i])

    places_to_rule_out = []
    for line in report:
        places_to_rule_out.append(check_where_we_can_rule_out(line[0], line[2], i))

        rule_out = []
    for coords in places_to_rule_out:
        rule_out += list(range(coords[0], coords[1]))

    rule_out = set(rule_out)
    
    if set(range(20)) - rule_out - places_we_cant_rule_out:
        beacons[i] = set(range(20)) - rule_out - places_we_cant_rule_out

    
