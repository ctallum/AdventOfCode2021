from region import Region
from typing import List

def calc_intersection(old_region: Region, new_region: Region) -> List[List[List[int]]]:
    split_bounds = []
    does_intersect = True

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
            does_intersect = False

    return does_intersect, split_bounds


def add_region(current_regions: List[Region], new_region: Region) -> List[Region]:
    new_regions = []
    for region in current_regions:
        new_regions += xyz_split(region, new_region)
    new_regions.append(new_region)
    return new_regions


def xyz_split(old_region: Region, new_region: Region) -> List[Region]:
    new_regions = []
    does_intersect, split_bounds = calc_intersection(old_region, new_region)

    # if overlaping regions
    if does_intersect:      
        for x_bounds in split_bounds[0]:
            for y_bounds in split_bounds[1]:
                for z_bounds in split_bounds[2]:
                    # create a new region that is a partial of original region
                    potential_region = Region([x_bounds, y_bounds, z_bounds], old_region.state)
                    is_duplicate_region, _ = calc_intersection(potential_region, new_region)
                    if not is_duplicate_region:
                        new_regions.append(potential_region)
    # no overlaping regions
    else:
        new_regions.append(old_region)
    return new_regions
