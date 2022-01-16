from functions import *
import numpy as np

with open('input.txt') as f:
    data = [a.strip().replace('.', '0').replace('#', '1')
            for a in f.readlines()]

algorithm = [int(a) for a in data[0]]
image = data[2:]
image = np.array([[int(a) for a in row] for row in image])

image = np.pad(image, pad_width=1, mode='constant')

# part 1
for _ in range(2):
    image = step(image, algorithm)
print(f'Solution to part 1: {count_lit_pixels(image)}')

# part 2
for _ in range(50):
    image = step(image, algorithm)
print(f'Solution to part 2: {count_lit_pixels(image)}')
