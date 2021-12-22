from itertools import product

# get data
with open('input.txt') as f:
    raw_data = [a.strip() for a in f.readlines()]
    start_string = raw_data[0]
    raw_data = [(a.replace(' -> ','')) for a in raw_data[2:]]
    new_pairs = {a[0:2]: (a[0]+a[2],a[2]+a[1]) for a in raw_data}

# create dictionaries
letter_count = {letter: 0 for letter in set("".join(raw_data))}
pair_count = {"".join(p): [0,0] for p in product("".join(raw_data), repeat=2)}

# populate dictionaries
for idx in range(len(start_string)-1):
    pair_count[start_string[idx:idx+2]][0] += 1

for letter in start_string:
    letter_count[letter] += 1

def step(n_iters):
    for _ in range(n_iters):

        for pair in pair_count.keys():
            if pair_count[pair][0] > 0:
                pair_count[pair][1] -= pair_count[pair][0]
                pair_count[new_pairs[pair][1]][1] += pair_count[pair][0]
                pair_count[new_pairs[pair][0]][1] += pair_count[pair][0]
                letter_count[new_pairs[pair][0][1]] += pair_count[pair][0]
        
        for pair in pair_count.keys():
            if pair_count[pair][1]:
                pair_count[pair][0] += pair_count[pair][1]
                pair_count[pair][1] = 0
    
    count = sorted(letter_count.values())
    return count[-1] - count[0]

# part 1
part1_answer = step(10)
print(f'Solution to Part 1: {part1_answer}')

# part 2
part2_answer = step(40)
print(f'Solution to Part 2: {part2_answer}')
