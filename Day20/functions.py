from typing import List, Tuple
import numpy as np
Image = np.ndarray


def bin2int(bin_list: List[int]) -> int:
    '''
    Take a list of 1 and 0 representing a binary number and convert into an integer
    '''
    sum = 0
    for idx, val in enumerate(reversed(bin_list)):
        sum += val * 2**idx
    return sum


def convolve(image: Image, coord: Tuple[int, int]) -> List[int]:
    '''
    From the image, take a 3x3 sample from top left starting at coord, create binary
    list of sample
    '''
    x_start = coord[0]
    y_start = coord[1]
    sample = image[y_start:y_start + 3, x_start: x_start + 3]
    bin_list = list(sample[0, :]) + list(sample[1, :]) + list(sample[2, :])
    return bin2int(bin_list)


def step(image: Image, algorithm: List[int]) -> Image:
    '''
    Preform 1 image enhancement algorithm pass
    '''
    image = np.pad(image, pad_width=2, mode='edge')
    new_x_size, new_y_size = np.shape(image)
    new_x_size -= 2
    new_y_size -= 2
    new_image = np.zeros((new_x_size, new_x_size), dtype=int)

    for x in range(0, len(image) - 2):
        for y in range(0, len(image) - 2):
            bin_value = convolve(image, (x, y))
            new_value = algorithm[bin_value]
            new_image[y, x] = new_value
    return new_image


def count_lit_pixels(image: Image) -> int:
    ''''
    Take a numpy array and count how many of the values are 1
    '''
    count = 0
    for row in image:
        for pixel in row:
            if pixel == 1:
                count += 1
    return count
