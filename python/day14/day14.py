with open('input.txt') as f:
    data = f.read().split('\n')
    INPUT = data[0]
    RULES = {entry[0]: entry[1] for entry in [entry.split( ' -> ' ) for entry in data[2:]]}


def add_dict_elem(dict, pair, n):
    if pair in dict:
        dict[pair] += n
    else:
        dict[pair] = n
    return dict


PAIR_DICT = {}
for k in range(len(INPUT) - 1):
    pair = INPUT[k:k + 2]
    PAIR_DICT = add_dict_elem(PAIR_DICT, pair, 1)

def iterate(pair_dict, rules):
    new_dict = {}
    for pair in pair_dict:
        if pair in rules:
            new_letter = rules[pair]
            add_dict_elem(new_dict, pair[0] + new_letter, pair_dict[pair])
            add_dict_elem(new_dict, new_letter + pair[1], pair_dict[pair])
    return new_dict

#Change for Part 1
for k in range(40):
    PAIR_DICT = iterate(PAIR_DICT, RULES)


def find_letter_frequency(pair_dict, input):
    alpha_dict = {}
    for pair in pair_dict:
        add_dict_elem(alpha_dict, pair[0], pair_dict[pair])
        add_dict_elem(alpha_dict, pair[1], pair_dict[pair])
    #fix first/last
    add_dict_elem(alpha_dict, input[0], 1)
    add_dict_elem(alpha_dict, input[-1], 1)
    for alpha in alpha_dict:
        alpha_dict[alpha] /= 2
    return alpha_dict


letter_frequency = find_letter_frequency(PAIR_DICT, INPUT)

print(max(letter_frequency.values()), min(letter_frequency.values()), max(letter_frequency.values()) - min(letter_frequency.values()))


