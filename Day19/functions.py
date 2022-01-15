from typing import List, Tuple, Set
from scanner import Scanner

# calculate manhatan distance between to points


def dist(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def format_data(raw_data: List[str]) -> List[List[int]]:
    '''
    Format data to usable format
    '''
    data = []
    scanner_count = 0
    for coordinate in raw_data:
        if coordinate[0:2] == '--':
            scanner_count += 1
            data.append([])
        elif coordinate != '':
            data[scanner_count - 1].append(coordinate)

    # convert all scanner data into integers
    data = [[[int(a) for a in coord.split(',')]
             for coord in scanner] for scanner in data]
    return data


def add_global_points(
        coord_array: List[Tuple[int]], coordinates: List[List[int]]) -> List[Tuple[int]]:
    '''
    Add new coordinate point to global array if it is not already in it
    '''
    for coord in coordinates:
        coord = tuple(coord)
        if coord not in coord_array:
            coord_array.append(coord)
    return coord_array


def make_global_network(coord_array: List[List[int]]) -> List[Set[Tuple[int]]]:
    '''
    Calculate a set of coordinate distances from every point to every other point
    '''
    network = []
    for coord in coord_array:
        coord_network = set()
        for other_coord in coord_array:
            coord_network.add(tuple([a - other_coord[idx]
                                     for idx, a in enumerate(coord)]))
        network.append(coord_network)

    return network


def solve_beacon(scanner: Scanner,
                 global_points: List[List[int]],
                 global_network: List[Set[Tuple[int]]]) -> tuple:
    '''
    Attempt to solve each beacon using the global network as reference
    '''
    if not scanner.solved:
        solve_tranformation(scanner, global_points, global_network)
        if scanner.solved:
            global_points = add_global_points(
                global_points, scanner.solved_coords)
            global_network = make_global_network(global_points)
    return global_points, global_network


def solve_tranformation(scanner,
                        global_points: List[List[int]],
                        global_network: List[Set[Tuple[int]]]) -> None:
    '''
    Try to find overlaping structures. If the network overlaps by at least 12 points,
    solve scanner position and calculate all it's readings with respect to the global frame.
    '''
    threshold = 12
    for tranformation, sub_network in enumerate(scanner.network):
        for idx1, coord1 in enumerate(global_network):
            for idx2, coord2 in enumerate(sub_network):
                if len((coord1.intersection(coord2))) >= threshold:
                    reference_coord = global_points[idx1]
                    new_coord = scanner.coordinates_varaitions[tranformation][idx2]
                    scanner.location = tuple(
                        [a - new_coord[idx] for idx, a in enumerate(reference_coord)])
                    scanner.solved_tranform = tranformation
                    scanner.get_solved_coords()
                    scanner.solved = True


def all_scanners_solved(scanners: List[Scanner]) -> bool:
    '''
    Check if all the scanners have been solved
    '''
    for scanner in scanners:
        if not scanner.solved:
            return False
    return True
