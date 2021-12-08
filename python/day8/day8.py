with open('input.txt') as f:
    data = f.read().split('\n')
    inputs = [entry.split(' | ')[0].split(' ') for entry in data]
    outputs = [entry.split(' | ')[1].split(' ') for entry in data]
print(outputs)

part_1_count = 0
for output in outputs:
    for entry in output:
        n = len(entry)
        if n in [2, 3, 4, 7]:
            part_1_count += 1
print("Part 1: ", part_1_count)


def build_hash_table(input_entry):
    output = {}
    for entry in input_entry:
        if len(entry) == 2:
            output[entry] = 1
            output[1] = entry
        if len(entry) == 4:
            output[entry] = 4
            output[4] = entry
        if len(entry) == 3:
            output[entry] = 7
            output[7] = entry
        if len(entry) == 7:
            output[entry] = 8
    output[6] = []
    output[5] = []
    for entry in input_entry:
        if len(entry) == 6:
            output[6].append(entry)
            if check_overlap(entry, output[1]) != 2:
                output[entry] = 6
            elif check_overlap(entry, output[4]) == 4:
                output[entry] = 9
            else:
                output[entry] = 0
        if len(entry) == 5:
            output[5].append(entry)
            if check_overlap(entry, output[1]) == 2:
                output[entry] = 3
            elif check_overlap(entry, output[4]) == 3:
                output[entry] = 5
            else:
                output[entry] = 2
    return output

def check_overlap(string_1, string_2):
    count_common = 0
    for char1 in string_1:
        for char2 in string_2:
            if char1 == char2:
                count_common += 1
    return count_common

part_2_sum = 0
num_reference = list(range(10))
for k in range(len(inputs)):
    hash_info = build_hash_table(inputs[k])
    power = len(outputs[k])-1
    for entry in outputs[k]:
        if len(entry) == 2:
            part_2_sum += 1*10**power
        elif len(entry) == 4:
            part_2_sum += 4*10**power
        elif len(entry) == 3:
            part_2_sum += 7*10**power
        elif len(entry) == 7:
            part_2_sum += 8*10**power
        else:
            for key in hash_info[len(entry)]:
                if check_overlap(entry, key) == len(entry):
                    part_2_sum += hash_info[key]*10**power
        power -= 1
print("Part 2: ", part_2_sum)