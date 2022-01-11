import ast
from snailfish_math import Number
import copy

with open('input.txt') as f:
    data = [ast.literal_eval(a.strip()) for a in f.readlines()]

# Part 1
data1 = copy.deepcopy(data)

while len(data1) > 1:
    fish_sum = Number([data1[0], data1[1]]).value
    data1[0:2] = [fish_sum]

print(f'Answer to part 1: {Number(data1[0]).magnitude}')


# Part 2
data2 = copy.deepcopy(data)
a = ((x, y) for x in data2 for y in data2)
max_sum = 0
for num1, num2 in a:
    if num1 != num2:
        magnitude = Number([num1, num2]).magnitude
        max_sum = max(magnitude, max_sum)

print(f'Answer to part2: {max_sum}')
