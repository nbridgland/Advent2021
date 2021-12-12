with open('input.txt') as f:
    data = f.read().split('\n')
    paths = [entry.split('-') for entry in data]

start_paths = [entry for entry in paths if entry[0] == 'start']

def count_paths_to_end(location, visited_small):
    forward_paths = [entry for entry in paths if entry[0] == location]
    back_paths = [entry for entry in paths if entry[1] == location]
    possible_paths = 0
    if location == location.lower():
        visited_small.append(location)
    for path in forward_paths:
        if path[1] in visited_small:
            continue
        elif path[1] == 'end':
            possible_paths += 1
        else:
            possible_paths += count_paths_to_end(path[1], visited_small.copy())
    for path in back_paths:
        if path[0] in visited_small:
            continue
        elif path[0] == 'end':
            possible_paths += 1
        else:
            possible_paths += count_paths_to_end(path[0], visited_small.copy())
    return possible_paths


print("Part 1: ", count_paths_to_end('start', []))

def count_paths_to_end_2(location, visited_small, visited_small_twice=False):
    if location == location.lower():
        if location in visited_small:
            return count_paths_to_end(location, visited_small)
        else:
            visited_small.append(location)
    forward_paths = [entry for entry in paths if entry[0] == location]
    back_paths = [entry for entry in paths if entry[1] == location]
    possible_paths = 0
    for path in forward_paths:
        if path[1] == "start":
            continue
        elif path[1] == 'end':
            possible_paths += 1
        else:
            possible_paths += count_paths_to_end_2(path[1], visited_small.copy())
    for path in back_paths:
        if path[0] == "start":
            continue
        elif path[0] == 'end':
            possible_paths += 1
        else:
            possible_paths += count_paths_to_end_2(path[0], visited_small.copy())
    return possible_paths


print("Part 2: ", count_paths_to_end_2('start', []))