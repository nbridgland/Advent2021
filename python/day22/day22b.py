with open("input.txt") as f:
    DATA = f.read().split('\n')
    DATA = [entry.split(' ') for entry in DATA]


def parse_cube_range(entry):
    if entry[0] == "on":
        value = 1
    if entry[0] == "off":
        value = 0
    file_string = entry[1]
    xs, ys, zs = file_string.split(',')
    xmin, xmax = xs.split('=')[1].split('..')
    ymin, ymax = ys.split('=')[1].split('..')
    zmin, zmax = zs.split('=')[1].split('..')
    return {'value': value, 'xmin': int(xmin), 'xmax': int(xmax) + 1, 'ymin': int(ymin),
            'ymax': int(ymax) + 1, 'zmin': int(zmin), 'zmax': int(zmax) + 1}


DATA = [parse_cube_range(entry) for entry in DATA]


def get_coords(parsed_entry):
    return parsed_entry['xmin'], parsed_entry['xmax'], parsed_entry['ymin'], parsed_entry['ymax'], parsed_entry['zmin'], \
           parsed_entry['zmax']


def is_overlapping(entry1, entry2):
    xmin, xmax, ymin, ymax, zmin, zmax = get_coords(entry1)
    xmin1, xmax1, ymin1, ymax1, zmin1, zmax1 = get_coords(entry2)
    if xmin <= xmin1 < xmax or xmin1 <= xmin < xmax1:
        if ymin <= ymin1 < ymax or ymin1 <= ymin < ymax1:
            if zmin <= zmin1 < zmax or zmin1 <= zmin < zmax1:
                return True
    return False


def split_instructions(entry1, entry2):
    instruction_set1 = []
    instruction_set2 = []
    xmin, xmax, ymin, ymax, zmin, zmax = get_coords(entry1)
    xmin1, xmax1, ymin1, ymax1, zmin1, zmax1 = get_coords(entry2)
    value = entry1['value']
    value1 = entry2['value']
    # x
    # min
    if xmin < xmin1 < xmax:
        instruction_set1.append(
            {'value': value, 'xmin': xmin, 'xmax': xmin1, 'ymin': ymin, 'ymax': ymax, 'zmin': zmin, 'zmax': zmax})
        xmin = xmin1
    elif xmin1 < xmin < xmax1:
        instruction_set2.append(
            {'value': value1, 'xmin': xmin1, 'xmax': xmin, 'ymin': ymin1, 'ymax': ymax1, 'zmin': zmin1, 'zmax': zmax1})
        xmin1 = xmin
    # max
    if xmin < xmax1 < xmax:
        instruction_set1.append(
            {'value': value, 'xmin': xmax1, 'xmax': xmax, 'ymin': ymin, 'ymax': ymax, 'zmin': zmin, 'zmax': zmax})
        xmax = xmax1
    elif xmin1 < xmax < xmax1:
        instruction_set2.append(
            {'value': value1, 'xmin': xmax, 'xmax': xmax1, 'ymin': ymin1, 'ymax': ymax1, 'zmin': zmin1, 'zmax': zmax1})
        xmax1 = xmax
    # y
    # min
    if ymin < ymin1 < ymax:
        instruction_set1.append(
            {'value': value, 'xmin': xmin, 'xmax': xmax, 'ymin': ymin, 'ymax': ymin1, 'zmin': zmin, 'zmax': zmax})
        ymin = ymin1
    elif ymin1 < ymin < ymax1:
        instruction_set2.append(
            {'value': value1, 'xmin': xmin1, 'xmax': xmax1, 'ymin': ymin1, 'ymax': ymin, 'zmin': zmin1, 'zmax': zmax1})
        ymin1 = ymin
    # max
    if ymin < ymax1 < ymax:
        instruction_set1.append(
            {'value': value, 'xmin': xmin, 'xmax': xmax, 'ymin': ymax1, 'ymax': ymax, 'zmin': zmin, 'zmax': zmax})
        ymax = ymax1
    elif ymin1 < ymax < ymax1:
        instruction_set2.append(
            {'value': value1, 'xmin': xmin1, 'xmax': xmax1, 'ymin': ymax, 'ymax': ymax1, 'zmin': zmin1, 'zmax': zmax1})
        ymax1 = ymax
    # z
    # min
    if zmin < zmin1 < zmax:
        instruction_set1.append(
            {'value': value, 'xmin': xmin, 'xmax': xmax, 'ymin': ymin, 'ymax': ymax, 'zmin': zmin, 'zmax': zmin1})
        zmin = zmin1
    elif zmin1 < zmin < zmax1:
        instruction_set2.append(
            {'value': value1, 'xmin': xmin1, 'xmax': xmax1, 'ymin': ymin1, 'ymax': ymax1, 'zmin': zmin1, 'zmax': zmin})
        zmin1 = zmin
    # max
    if zmin < zmax1 < zmax:
        instruction_set1.append(
            {'value': value, 'xmin': xmin, 'xmax': xmax, 'ymin': ymin, 'ymax': ymax, 'zmin': zmax1, 'zmax': zmax})
        zmax = zmax1
    elif zmin1 < zmax < zmax1:
        instruction_set2.append(
            {'value': value1, 'xmin': xmin1, 'xmax': xmax1, 'ymin': ymin1, 'ymax': ymax1, 'zmin': zmax, 'zmax': zmax1})
        zmax1 = zmax
    instruction_set2.append(
        {'value': value1, 'xmin': xmin, 'xmax': xmax, 'ymin': ymin, 'ymax': ymax, 'zmin': zmin, 'zmax': zmax})
    return instruction_set1, instruction_set2


def separate_instructions(data):
    print(f"Length: {len(data)}")
    k = 0
    while k < len(data):
        if k % 1000 == 0:
            print(k)
        j = k + 1
        while j < len(data):
            if is_overlapping(data[k], data[j]):
                changed = True
                new_k_instructions, new_j_instructions = split_instructions(data[k], data[j])
                data = data[:j] + new_j_instructions + data[j + 1:]
                data = data[:k] + new_k_instructions + data[k + 1:]
                j += len(new_j_instructions) + len(new_k_instructions) - 2
                if len(new_k_instructions) == 0: #deal with issue requiring rework
                    if k > 0:
                        k -= 1
                    if j > k + 1:
                        j -= 1
            j += 1
        k += 1
    return data


def is_initialization_param(params):
    for param in params:
        if not -50 <= param <= 50:
            return False
    return True


def initialize(cube, data):
    for entry in data:
        value = entry['value']
        params = get_coords(entry)
        if is_initialization_param(params):
            xmin, xmax, ymin, ymax, zmin, zmax = params
            cube[xmin + 50:xmax + 50, ymin + 50:ymax + 50, zmin + 50:zmax + 50] = value

def find_overlapping_regions(data):
    regions = []
    checked = [0 for _ in range(len(data))]
    for k in range(len(data)):
        if checked[k] == 1:
            continue
        checked[k] = 1
        region = [k]
        last_len = 0
        while len(region) > last_len:
            last_len = len(region)
            for j in range(len(data)):
                if checked[j] == 1:
                    continue
                for i in region:
                    if is_overlapping(data[i], data[j]):
                        region.append(j)
                        checked[j] = 1
                        break
        regions.append(region)
    return regions


if __name__ == "__main__":
    regions = find_overlapping_regions(DATA)
    count_lit = 0
    for region in regions:
        print(region)
        separated_instructions = separate_instructions([DATA[i] for i in range(len(DATA)) if i in region])
        for entry in separated_instructions:
            if entry['value'] == 0:
                continue
            count_lit += (entry['xmax'] - entry['xmin']) * (entry['ymax'] - entry['ymin']) * (entry['zmax'] - entry['zmin'])
        print(count_lit)