from region import *
from functions import *


with open('input.txt') as f:
    raw_data = [a.strip() for a in f.readlines()]
    state_data = [a[1].replace('n','1').replace('f','0') for a in raw_data]
    state_data = [int(a) for a in state_data]
    cuboid_data = [a.split('=')[1:] for a in raw_data]
    cuboid_data = [[a[:-2] if a in line[:2] else a for a in line] for line in cuboid_data]
    cuboid_data = [[a.split('..') for a in line] for line in cuboid_data]
    cuboid_data = [[[int(a) for a in axis] for axis in line] for line in cuboid_data]

# populate a list of region objects
initial_regions = []
for idx, new_region in enumerate(cuboid_data):
    initial_regions.append(Region(cuboid_data[idx], state_data[idx]))

# Part 1
final_regions = []
for new_region in initial_regions[0:20]:
    final_regions = add_region(final_regions, new_region)

count = 0
for region in final_regions:
    if region.state == 1:
        count += region.area

print(f'Solution to part 1: {count}')

# Part 2
final_regions = []
for new_region in initial_regions:
    final_regions = add_region(final_regions, new_region)

count = 0
for region in final_regions:
    if region.state == 1:
        count += region.area


print(f'Solution to part 2: {count}')
