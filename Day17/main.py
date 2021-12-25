import copy
# get data
with open('input.txt') as f:
    data = f.readline().strip().split(', ')
    data = [a[a.index('=')+1:].split('..') for a in data]
    data = [(int(a[0]),int(a[1])) for a in data]

x_target = data[0]
y_target = data[1]
x_range = list(range(x_target[0],x_target[1]+1))
y_range = list(range(y_target[0],y_target[1]+1))

def simulate_flight(dx0,dy0):
    flight = [[0, dx0, 0, dy0]]
    while True:
        flight = step(flight)
        if break_conditions(flight,x_range,y_range):
            return flight

def break_conditions(flight, x_range,y_range):
    p = flight[-1]
    if p[2] < y_range[0]:
        return True
    if p[0] > x_range[-1]:
        return True
    return False

def step(flight):
    p = copy.deepcopy(flight[-1])
    
    # solve acceleration
    if p[1] > 0: ddx = -1
    elif p[1] < 0: ddx = 1
    else: ddx = 0
    ddy = -1

    # update position
    p[0] += p[1]
    p[2] += p[3]

    # update velocity
    p[1] += ddx
    p[3] += ddy
    
    flight.append(p)
    return flight

def is_valid_flight(flight):
    x_vals = [a[0] for a in flight]
    y_vals = [a[2] for a in flight]    

    x_target_range = x_range
    y_target_range = y_range
    
    for idx,x_val in enumerate(x_vals):
        if x_val in x_target_range and y_vals[idx] in y_target_range:
            return True
    return False

# calculate all possible throws
x_attempt_range = (0,263)
y_attempt_range = (-115,1000)
valid_throws = []

for dx in range(x_attempt_range[0],x_attempt_range[1]+1):
    for dy in range(y_attempt_range[0],y_attempt_range[1]+1):
        result = simulate_flight(dx,dy)
        if is_valid_flight(result):
            valid_throws.append((dx,dy))

# pt1
all_dy = [a[1] for a in valid_throws]
max_dy = max(all_dy)
vertical_throw = simulate_flight(0,max_dy)
max_y = max([a[2] for a in vertical_throw])
print(f'Solution to Part 1: {max_y}')

#pt2
print(f'Solution to Part 2: {len(valid_throws)}')