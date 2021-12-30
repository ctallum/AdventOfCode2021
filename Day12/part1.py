# import libraries
import copy

# get data
with open('input.txt') as f:
    data = [a.strip().split('-') for a in f.readlines()]

def is_small_cave(cave_name: str):
    '''
    Returns if a cave is small or not
    '''
    return cave_name.islower()

def clean_paths(current_paths: dict, cave: str) -> dict:
    '''
    Remove all instances of the small cave from dictionary. Prevents
    traveling to the cave in the future. 
    '''
    paths = current_paths
    # remove key of small cave
    paths.pop('cave', None)
    # remove all values of small cave
    for _, values in paths.items():
        if cave in values: values.remove(cave)  
    
    return paths
    
def explore(current_node: str, current_paths: dict, path_count: int) -> int:
    '''
    Finds how many unique paths there are through a network of caves, visiting small caves only once.
    '''
    paths = copy.deepcopy(current_paths)
    count = copy.deepcopy(path_count)
    # clean paths if node is a small cave
    if is_small_cave(current_node):
        paths = clean_paths(paths, current_node)

    # if we have reached end, add one to the path count and return
    if current_node == 'end':
        return count + 1
    else:
        further_paths = 0
        for next_node in paths[current_node]:
            further_paths += explore(next_node, paths, count)
        return count + further_paths

# starting point
start_node = 'start'

# make master dictionary
paths = {}
for pair in data:
    if pair[0] not in paths:
        paths[pair[0]] = [pair[1]]
    else:
        paths[pair[0]].append(pair[1])
    if pair[1] not in paths:
        paths[pair[1]] = [pair[0]]
    else:
        paths[pair[1]].append(pair[0])

# initial path count
path_count = 0

answer = explore('start',paths,path_count)
print(f'Solution to Part 1: {answer} unique paths')