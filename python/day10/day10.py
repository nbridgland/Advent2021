with open('input.txt') as f:
    data = f.read().split('\n')
    print(data)

char_pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}

score = 0
for line in data:
    print(line)
    open_chars = []
    for char in line:
        if char in char_pairs:
            open_chars.append(char)
        else:
            if char == char_pairs[open_chars[-1]]:
                open_chars.pop()
            else:
                score += score_dict[char]
                break
print("Part 1: ", score)


# Part 2
score_dict = {')': 1, ']': 2, '}': 3, '>': 4}

scores = []
for line in data:
    open_chars = []
    uncorrupted = True
    for char in line:
        if char in char_pairs:
            open_chars.append(char)
        else:
            if char == char_pairs[open_chars[-1]]:
                open_chars.pop()
            else:
                uncorrupted = False
                break
    if uncorrupted:
        score = 0
        while len(open_chars) > 0:
            score = 5*score + score_dict[char_pairs[open_chars.pop()]]
        if score > 0:
            scores.append(score)

import pandas as pd
print("Part 2: ", pd.Series(scores).median())
