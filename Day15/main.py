import math
import numpy as np

# get input data
with open('input.txt') as f:
    data =[list(line.strip()) for line in f.readlines()]
    data = [[int(a) for a in line] for line in data]


def find_next_vertex(shortest_dist,visited):
    min_value = math.inf
    best_loc = ()
    for i,row in enumerate(shortest_dist):
        for j,val in enumerate(row):
            if val < min_value and not visited[i][j]:
                min_value = val
                best_loc = (i,j)
    return best_loc
    
def dijkstras(data, start, end):    
    visited = np.zeros(np.shape(data), dtype=bool)
    shortest_dist = math.inf * np.ones(np.shape(data))

    shortest_dist[start] = 0

    data = np.pad(data, pad_width=1, mode='constant',
               constant_values=0)
    
    count = 1
    while np.any(~visited):
        print(f'Status: {count/(np.size(data,1)**2)}')
        count +=1 
        #find vertex with smallest known distance from start
        cur_vertex = find_next_vertex(shortest_dist,visited)
        visited[cur_vertex] = True
    
        # find distances to all adjacent node
        if data[(cur_vertex[0],cur_vertex[1]+1)]:
            possible_shortest = shortest_dist[cur_vertex] + data[(cur_vertex[0],cur_vertex[1]+1)]
            if possible_shortest < shortest_dist[(cur_vertex[0]-1,cur_vertex[1])]:
                shortest_dist[(cur_vertex[0]-1,cur_vertex[1])] = possible_shortest

        if data[(cur_vertex[0]+2,cur_vertex[1]+1)]:
            possible_shortest = shortest_dist[cur_vertex] + data[(cur_vertex[0]+2,cur_vertex[1]+1)]
            if possible_shortest < shortest_dist[(cur_vertex[0]+1,cur_vertex[1])]:
                shortest_dist[(cur_vertex[0]+1,cur_vertex[1])] = possible_shortest

        if data[(cur_vertex[0]+1,cur_vertex[1])]:
            possible_shortest = shortest_dist[cur_vertex] + data[(cur_vertex[0]+1,cur_vertex[1])]
            if possible_shortest < shortest_dist[(cur_vertex[0],cur_vertex[1]-1)]:
                shortest_dist[(cur_vertex[0],cur_vertex[1]-1)] = possible_shortest

        if data[(cur_vertex[0]+1,cur_vertex[1]+2)]:
            possible_shortest = shortest_dist[cur_vertex] + data[(cur_vertex[0]+1,cur_vertex[1]+2)]
            if possible_shortest < shortest_dist[(cur_vertex[0],cur_vertex[1]+1)]:
                shortest_dist[(cur_vertex[0],cur_vertex[1]+1)] = possible_shortest

    print(f'Shortest path: {shortest_dist[end]}')
    return shortest_dist[end]
        
# part 1        
dijkstras(data,(0,0),(-1,-1))

# part 2
new_data = np.zeros(np.multiply(5,np.shape(data)))

data_height = np.size(data,0)
data_width = np.size(data,1)


for row in range(5):
    for col in range(5):
        offset = row + col
        temp_data = np.array(data) + offset

        for a,data_row in enumerate(temp_data):
            for b,data_col in enumerate(data_row):
                if data_col > 9:
                    temp_data[(a,b)] -= 9
        
        
        y_range = (row*data_height, (row+1)*data_height)
        x_range = (col*data_width, (col+1)*data_width)

        new_data[y_range[0]:y_range[1],x_range[0]:x_range[1]] = temp_data


pt2_answer = dijkstras(new_data,(0,0),(-1,-1))



        
        






