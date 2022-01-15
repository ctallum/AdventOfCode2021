from scanner import Scanner
from functions import *


with open('input.txt') as f:
    raw_data = [a.strip() for a in f.readlines()]

# format data into usable format
data = format_data(raw_data)

# create a list of scanner objects
scanners = []
for scanner_number, coordinate_set in enumerate(data):
    if scanner_number == 0:
        scanners.append(Scanner(coordinate_set, origin=True))
    else:
        scanners.append(Scanner(coordinate_set, origin=False))

# initalize global points and network between all points
global_points = []
global_points = add_global_points(global_points, scanners[0].coordinates)
global_network = make_global_network(global_points)

# solve each scanner
while not all_scanners_solved(scanners):
    for scanner in scanners:
        global_points, global_network = solve_beacon(
            scanner, global_points, global_network)

# part 1
print(f'Solution to part 1: {len(global_points)}')

# part 2
max_dist = 0
for scanner1 in scanners:
    for scanner2 in scanners:
        max_dist = max(max_dist, dist(scanner1.location, scanner2.location))

print(f'Solution to part 2: {max_dist}')
