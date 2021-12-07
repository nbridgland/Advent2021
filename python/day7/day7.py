import numpy as np
with open('input.txt') as f:
    data = f.read().split(',')
    data = [int(entry) for entry in data]
    data = np.array(data)


def measure_distance(data, pos):
    return np.abs(data-pos).sum()


def measure_fuel(data, pos):
    distances = np.abs(data-pos)
    return ((distances*(distances+1))/2).sum()


pos = np.median(data)
cost = min(measure_distance(data, np.floor(pos)), measure_distance(data, np.ceil(pos)))
print("Part 1: ", cost)

pos = np.mean(data)
cost = min(measure_fuel(data, np.floor(pos)), measure_fuel(data, np.ceil(pos)))
print("Part 2: ", cost)