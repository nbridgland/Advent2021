import numpy as np
with open('input.txt') as f:
    data = f.read().split('\n')


def translate_pixel(char):
    if char == '#':
        return 1
    if char == '.':
        return 0


IMAGE_DICTIONARY = [translate_pixel(char) for char in data[0]]
NUM_ENHANCEMENTS = 50
FLIP_EDGES = True

base_image = np.array([[translate_pixel(char) for char in entry] for entry in data[2:]])

expansion = 4*NUM_ENHANCEMENTS+4
IMAGE = np.zeros((base_image.shape[0]+expansion, base_image.shape[1]+expansion))

IMAGE[2*NUM_ENHANCEMENTS+2:-2*NUM_ENHANCEMENTS-2, 2*NUM_ENHANCEMENTS+2:-2*NUM_ENHANCEMENTS-2] = base_image


def process(image, edges, image_dictionary=IMAGE_DICTIONARY):
    output_image = np.zeros(shape=image.shape)
    for column in range(1, image.shape[1] - 1):
        k = 2
        row0 = (image[0, column-1:column+2]*np.array([4,2,1])).sum()
        row1 = (image[1, column-1:column+2]*np.array([4,2,1])).sum()
        row2 = (image[k, column-1:column+2]*np.array([4,2,1])).sum()
        output_image[k-1, column] = image_dictionary[int(row2 + 8*row1 + 64*row0)]
        while k < image.shape[0]:
            row0 = row1
            row1 = row2
            row2 = (image[k, column-1:column+2]*np.array([4,2,1])).sum()
            output_image[k - 1, column] = image_dictionary[int(row2 + 8 * row1 + 64 * row0)]
            k += 1
    if FLIP_EDGES:
            output_image[0, :] = edges
            output_image[-1, :] = edges
            output_image[:, 0] = edges
            output_image[:, -1] = edges
    return output_image


for k in range(NUM_ENHANCEMENTS):
    print(k)
    IMAGE = process(IMAGE, ((k+1) % 2))

print(IMAGE.sum())