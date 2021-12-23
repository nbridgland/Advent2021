import numpy as np

with open("testinput2.txt") as f:
    DATA = f.read().split('\n')
    DATA = [entry.split(' ') for entry in DATA]


def parse_cube_range(file_string):
    xs, ys, zs = file_string.split(',')
    xmin, xmax = xs.split('=')[1].split('..')
    ymin, ymax = ys.split('=')[1].split('..')
    zmin, zmax = zs.split('=')[1].split('..')
    return int(xmin), int(xmax), int(ymin), int(ymax), int(zmin), int(zmax)


def is_initialization_param(params):
    for param in params:
        if not -50 <= param <= 50:
            return False
    return True


def initialize(cube, data):
    for entry in data:
        flag = entry[0]
        params = parse_cube_range(entry[1])
        if is_initialization_param(params):
            xmin, xmax, ymin, ymax, zmin, zmax = params
            if flag == 'on':
                cube[xmin + 50:xmax + 51, ymin + 50:ymax + 51, zmin + 50:zmax + 51] = 1
            if flag == 'off':
                cube[xmin + 50:xmax + 51, ymin + 50:ymax + 51, zmin + 50:zmax + 51] = 0


if __name__ == "__main__":
    initialization_cube = np.zeros(shape=(101, 101, 101))
    initialize(initialization_cube, DATA)
    print(initialization_cube.sum())
