import numpy as np

with open('input.txt') as f:
    data = f.read().split('\n')
    cave_map = np.array([[int(k) for k in row] for row in data])
    cave_map[0,0] = 0 #no cost to entering top left corner, since start there

print(cave_map)
print(cave_map.shape)
path_info = np.zeros(shape=cave_map.shape)

array_max = cave_map.shape[0]-1
path_info[array_max, array_max] = cave_map[array_max][array_max]
# Assume square
for i in range(array_max-1, -1, -1):
    # Assume always best to move right or down
    for j in range(array_max, i, -1):
        if j == array_max:
            path_info[i, j] = cave_map[i, j] + path_info[i+1, j]
            path_info[j, i] = cave_map[j, i] + path_info[j, i+1]
        else:
            path_info[i, j] = cave_map[i, j] + min(path_info[i+1, j], path_info[i, j + 1])
            path_info[j, i] = cave_map[j, i] + min(path_info[j+1, i], path_info[j, i + 1])
    path_info[i, i] = cave_map[i, i] + min(path_info[i+1, i], path_info[i, i+1])
print(path_info)



#Part 2
with open('input.txt') as f:
    data = f.read().split('\n')
    cave_map = np.array([[int(k) for k in row] for row in data])

small_cave_map = cave_map - 1
tile_size = cave_map.shape[0]
cave_map = np.zeros(shape=(5*tile_size, 5*tile_size))
for k in range(5):
    for j in range(5):
        cave_map[k*tile_size:(k+1)*tile_size, j*tile_size:(j+1)*tile_size] = (small_cave_map+j+k) % 9
cave_map = cave_map + 1
cave_map[0, 0] = 0

print(cave_map)
print(cave_map.shape)
path_info = np.zeros(shape=cave_map.shape)

#Don't assuming best to move right or down
def in_map(x,y):
    if x < 0 or y < 0:
        return False
    if x > array_max or y > array_max:
        return False
    return True

def update(info, x, y):
    if in_map(x-1, y):
        if cave_map[x-1, y] + info[x, y] < info[x-1, y]:
            info[x-1, y] = cave_map[x-1, y] + info[x, y]
            info = update(info, x-1, y)
    if in_map(x+1, y):
        if cave_map[x+1, y] + info[x, y] < info[x+1, y]:
            info[x+1, y] = cave_map[x+1, y] + info[x, y]
            info = update(info, x+1, y)
    if in_map(x, y-1):
        if cave_map[x, y-1] + info[x, y] < info[x, y-1]:
            info[x, y-1] = cave_map[x, y] + info[x, y-1]
            info = update(info, x, y-1)
    if in_map(x, y+1):
        if cave_map[x, y + 1] + info[x, y] < info[x, y + 1]:
            info[x, y + 1] = cave_map[x, y] + info[x, y + 1]
            info = update(info, x, y + 1)
    return info


array_max = cave_map.shape[0]-1
path_info[array_max, array_max] = cave_map[array_max][array_max]
for i in range(array_max-1, -1, -1):
    for j in range(array_max, i, -1):
        if j == array_max:
            path_info[i, j] = cave_map[i, j] + path_info[i+1, j]
            path_info[j, i] = cave_map[j, i] + path_info[j, i+1]
        else:
            path_info[i, j] = cave_map[i, j] + min(path_info[i+1, j], path_info[i, j + 1])
            if path_info[i, j] + cave_map[i+1, j] < path_info[i+1, j]:
                path_info[i+1, j] = path_info[i, j] + cave_map[i+1, j]
                path_info = update(path_info, i+1, j)
            if path_info[i, j] + cave_map[i, j+1] < path_info[i, j+1]:
                path_info[i, j+1] = path_info[i, j] + cave_map[i, j+1]
                path_info = update(path_info, i, j+1)
            path_info[j, i] = cave_map[j, i] + min(path_info[j+1, i], path_info[j, i + 1])
            if path_info[j, i] + cave_map[j+1, i] < path_info[j+1, i]:
                path_info[j+1, i] = path_info[j, i] + cave_map[j+1, i]
                path_info = update(path_info, j+1, i)
            if path_info[j, i] + cave_map[j, i+1] < path_info[j, i+1]:
                path_info[j, i+1] = path_info[j, i] + cave_map[j, i+1]
                path_info = update(path_info, j, i+1)
    path_info[i, i] = cave_map[i, i] + min(path_info[i+1, i], path_info[i, i+1])


print(path_info)
