import numpy as np

with open('input.txt') as f:
    data = f.read().split('\n')
    data = np.array([[int(entry) for entry in row] for row in data])

def iterate_step(array):
    flashed = []
    array = array + 1
    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            if array[x, y] > 9:
                if (x,y) not in flashed:
                    flashed.append((x,y))
                    flashed, array = flash(array, (x, y), flashed)
    for entry in flashed:
        array[entry] = 0
    return array, len(flashed)

def gen_adjacent_coordinates(x, y, max_x, max_y):
    adjacent_coordinates = [[(a, b) for a in range(x-1, x+2) if 0 <= a < max_x] for b in range(y - 1, y + 2) if 0 <= b < max_y]
    adjacent_coordinates = [[entry for entry in row if entry != (x,y)] for row in adjacent_coordinates]
    return adjacent_coordinates

def flash(array, coord, flashed):
    coords_list = gen_adjacent_coordinates(coord[0], coord[1], array.shape[0], array.shape[1])
    for row in coords_list:
        for entry in row:
            array[entry] += 1
            if array[entry] > 9:
                if entry not in flashed:
                    flashed.append(entry)
                    flashed, array = flash(array, entry, flashed)
    return flashed, array

total_flashes = 0
for i in range(100):
    data, flashes = iterate_step(data)
    print(data)
    total_flashes += flashes
print("Part 1: ", total_flashes)

with open('input.txt') as f:
    data = f.read().split('\n')
    data = np.array([[int(entry) for entry in row] for row in data])

flashes = 0
steps = 0
while flashes != data.shape[0]*data.shape[1]:
    data, flashes = iterate_step(data)
    steps += 1
print("Part 2:", steps)