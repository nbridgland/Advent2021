import numpy as np

with open('input.txt') as f:
    data = f.read().split('\n')
    data = np.array([[int(char) for char in entry] for entry in data])

def gen_adjacent_coordinates(x, y, max_x, max_y):
    adjacent_coordinates = [[(a, b) for a in range(x-1, x+2) if 0 <= a < max_x] for b in range(y - 1, y + 2) if 0 <= b < max_y]
    adjacent_coordinates = [[entry for entry in row if entry != (x,y)] for row in adjacent_coordinates]
    return adjacent_coordinates

#Part 1:
max_x = data.shape[0]
max_y = data.shape[1]
risk = 0
for x in range(max_x):
    for y in range(max_y):
        coords = gen_adjacent_coordinates(x, y, max_x, max_y)
        is_low = True
        for row in coords:
            for coord in row:
                if data[coord] <= data[(x, y)]:
                    is_low = False
                    continue
        if is_low:
            risk += 1 + data[(x, y)]
print("Part 1: ", risk)


# Part 2
basin_map = np.where(data < 9, 1, 0).astype('float64')

def find_first_corner(basin_map):
    for x in range(max_x):
        for y in range(max_y):
            if basin_map[(x, y)]:
                return x, y
    return None


def gen_basin_adjacent_coordinates(x, y, max_x, max_y):
    possibles = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [coord for coord in possibles if 0 <= coord[0] < max_x and 0 <= coord[1] < max_y]

def gen_basin_mask(start_coord, max_x, max_y):
    output = np.zeros((max_x, max_y))
    output[start_coord] = 1
    size = 0
    while output.sum() > size:
        size = output.sum()
        xs, ys = np.where(output > 0)
        for k in range(len(xs)):
            coords_to_check = gen_basin_adjacent_coordinates(xs[k], ys[k], max_x, max_y)
            for entry in coords_to_check:
                if data[entry] < 9:
                    output[entry] = 1
    return output





def check_adjacent_coords(coords, basin_mask):
    for coord in coords:
        if data[coord] < 9:
            basin_mask[coord] = 1
    return basin_mask


max1 = 0
max2 = 0
max3 = 0
basin_map = np.where(data < 9, 1, 0).astype('float64')
k = 0
while basin_map.sum() > 0:
    coord = find_first_corner(basin_map)
    mask = gen_basin_mask(coord, max_x, max_y)
    basin_map -= mask
    if mask.sum() > max1:
        max3 = max2
        max2 = max1
        max1 = mask.sum()
    elif mask.sum() > max2:
        max3 = max2
        max2 = mask.sum()
    elif mask.sum() > max3:
        max3 = mask.sum()
    k += 1
print("Part 2: ", max1*max2*max3)
