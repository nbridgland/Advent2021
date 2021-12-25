import numpy as np

def parse_input(char):
    if char == '>':
        return 1
    elif char == 'v':
        return -1
    elif char == '.':
        return 0
    raise


def step(sea_map):
    changed = False
    new_map = np.zeros(shape=sea_map.shape, dtype=int)
    for k in range(sea_map.shape[1]):
        for j in range(sea_map.shape[0]):
            if sea_map[j][k] == 1:
                if sea_map[j][(k+1) % sea_map.shape[1]] == 0:
                    new_map[j][(k+1) % sea_map.shape[1]] = 1
                    changed = True
                else:
                    new_map[j][k] = 1
    for k in range(sea_map.shape[1]):
        for j in range(sea_map.shape[0]):
            if sea_map[j][k] == -1:
                if (sea_map[(j+1) % sea_map.shape[0]][k] > -1) and (new_map[(j+1) % new_map.shape[0]][k] == 0):
                    new_map[(j+1) % sea_map.shape[0]][k] = -1
                    changed = True
                else:
                    new_map[j][k] = -1
    return new_map, changed

if __name__ == "__main__":
    with open('input.txt') as f:
        current_map = f.read().split('\n')
        current_map = np.array([[parse_input(k) for k in line] for line in current_map])
    changed = True
    steps = 0
    while changed:
        current_map, changed = step(current_map)
        steps += 1
        if steps % 100 == 0:
            print(steps)
    print(steps)