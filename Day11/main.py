import numpy as np
import scipy.signal
import copy
# get all data
with open('input.txt') as f:
    data = f.readlines()
    for idx,line in enumerate(data):
        data[idx] = list(line.strip())
    data = [[int(num) for num in line] for line in data]
    data = np.array(data)

def step(fish_array):
    done = False
    
    # increment all octopus by 1
    fish_array += 1
    blinked_fish = np.zeros(np.shape(fish_array))
    new_flashes = 0
    while not done:
        done = True
        blinking_fish = np.zeros(np.shape(fish_array))      

        # find all octopus that should flash  
        mask = np.where(fish_array > 9)
        if np.size(mask):
            mask = list(zip(mask[0], mask[1]))
            for loc in mask:
                # mark each NEW flashing octopus in a new array
                if blinked_fish[loc[0]][loc[1]] == 0:
                    blinking_fish[loc[0]][loc[1]] = 1
                    blinked_fish[loc[0]][loc[1]] = 1

            # convolutional array to figure out which spaces each new flash will affect
            expand_array = scipy.signal.convolve2d(blinking_fish, np.ones((3,3)), mode='same').astype(int)
            new_flashes += np.sum(blinking_fish)
            # add the cascade flash to all the surrounding octopus
            fish_array += expand_array     

        # if no new octopus are flashing, step is done  
        done = not np.any(blinking_fish)

    # reset all octopus at 9 to zero
    mask = np.where(fish_array > 9)
    if np.size(mask):
        mask = list(zip(mask[0], mask[1]))
        for loc in mask:
            fish_array[loc[0]][loc[1]] = 0

    return fish_array, new_flashes
        
# part 1
def part1(data):
    data = copy.deepcopy(data)
    count = 0
    for _ in range(100):
        data,new_flashes = step(data)
        count += new_flashes
    return int(count)

print(f'Solution to Part1: {part1(data)}')

# part 2
def part2(data):
    data = copy.deepcopy(data)
    done = False
    sync_time = 0
    while not done:
        data,_ = step(data)
        sync_time += 1
        if np.sum(data) == 0:
            done = True
    return sync_time

print(f'Solution to Part2: {part2(data)}')


