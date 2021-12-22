import numpy as np
import copy

def parse_data(input_file) -> np.array:
    with open (input_file,'r') as f:
        data = f.readlines()
        data = [line.strip() for line in data]
        data = np.array([[int(num) for num in line] for line in data])
        data = np.pad(data, pad_width=1, mode='constant',
                constant_values=9)
    return data


def solve_part1(data):
    local_mins = []

    for row in range(1,len(data)-1):
        for col in range(1,len(data)-1):
            if (data[row][col] < data[row + 1][col] and 
                    data[row][col] < data[row - 1][col] and 
                    data[row][col] < data[row][col + 1] and 
                    data[row][col] < data[row][col - 1]):
                local_mins.append(data[row][col])

    local_mins = np.array(local_mins) + 1

    part1_answer = np.sum(local_mins)
    
    return part1_answer


def solve_part2(data):
    basin_locs = []
    for row in range(1,len(data)-1):
        for col in range(1,np.size(data,1)-1):
            if (data[row][col] < data[row + 1][col] and 
                    data[row][col] < data[row - 1][col] and 
                    data[row][col] < data[row][col + 1] and 
                    data[row][col] < data[row][col - 1]):
                basin_locs.append([row, col])
    
    basin_locs = np.array(basin_locs)
    
    basin_sizes = []

    def find_basin_area(data:np.array, loc:tuple, searched:np.array, size:int) -> int:
        new_size = copy.deepcopy(size)

        searched[loc[0]][loc[1]] = 1
        size += 1

        if data[loc[0]+1][loc[1]] != 9 and searched[loc[0] + 1][loc[1]] != 1:
            size += find_basin_area(data, (loc[0]+1,loc[1]), searched, new_size)
        if data[loc[0]-1][loc[1]] != 9 and searched[loc[0] - 1][loc[1]] != 1:
            size += find_basin_area(data, (loc[0] - 1,loc[1]), searched, new_size)
        if data[loc[0]][loc[1]+1] != 9 and searched[loc[0]][loc[1] + 1] != 1:
            size += find_basin_area(data, (loc[0],loc[1] + 1), searched, new_size)
        if data[loc[0]][loc[1]-1] != 9 and searched[loc[0]][loc[1] - 1] != 1:
            size += find_basin_area(data, (loc[0],loc[1] - 1), searched, new_size) 
        
        return size

    for loc in basin_locs:
        basin_sizes.append(find_basin_area(data,(loc[0],loc[1]), searched=np.zeros(np.shape(data)), size=0))

    sorted_basins = sorted(basin_sizes,reverse=True)

    answer = sorted_basins[0] * sorted_basins[1] * sorted_basins[2]
        
    return answer

    
data = parse_data('input.txt')

print(solve_part1(data))
print(solve_part2(data))