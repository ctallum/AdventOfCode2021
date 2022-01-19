from region import *
from typing import List

def return_split_bounds(old_region: Region, new_region: Region) -> List[List[List[int]]]:
    split_bounds = []
    non_interact_count = 0

    for axis_idx in range(3):
        l1 = old_region.bounds[axis_idx]
        l2 = new_region.bounds[axis_idx]
        # left overlap
        if l2[0] - l1[0] <= 0 and l2[1] - l1[1] < 0 and l2[1] >= l1[0]:
            split_bounds.append([[l1[0], l2[1]], [l2[1]+1, l1[1]]])
        # right overlap
        elif l2[0] - l1[0] > 0 and l2[1] - l1[1] >= 0 and l1[1] >= l2[0]:
            split_bounds.append([[l1[0], l2[0] - 1], [l2[0], l1[1]]])
        # surounding
        elif l2[0] - l1[0] <= 0 and l2[1] - l1[1] >= 0:
            split_bounds.append([l1])
        # inside
        elif l2[0] - l1[0] > 0 and l2[1] - l1[1] < 0:
            split_bounds.append([[l1[0], l2[0] - 1], l2, [l2[1] + 1, l1[1]]])
        # does not intersect
        else:
            non_interact_count += 1

    return non_interact_count, split_bounds



def add_region(current_regions: List[Region], new_region: Region) -> List[Region]:
    new_regions = []
    for region in current_regions:
        new_regions += xyz_split(region, new_region)
    new_regions.append(new_region)
    return new_regions


def xyz_split(old_region: Region, new_region: Region) -> List[Region]:
    new_regions = []
    non_interactin_count, split_bounds = return_split_bounds(old_region, new_region)

    # if intersections
    if non_interactin_count == 0:      
        for x_bounds in split_bounds[0]:
            for y_bounds in split_bounds[1]:
                for z_bounds in split_bounds[2]:
                    new_regions.append(Region([x_bounds, y_bounds, z_bounds], old_region.state))
        # remove overlap with new_region
        for idx, region in enumerate(new_regions):
            non_interact , _ = return_split_bounds(region, new_region)
            if non_interact == 0:
                new_regions.pop(idx)
                break
    # no overlaping regions
    else:
        new_regions.append(old_region)
    return new_regions



