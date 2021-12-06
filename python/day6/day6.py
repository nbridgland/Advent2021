import pandas as pd

with open('input.txt') as f:
    data = f.read().split(',')
    data = [int(i) for i in data]
    data = pd.Series(data)
input_counts = data.value_counts()
lantern_fish_counts = {k:0 for k in range(9)}

for entry in input_counts.index:
    lantern_fish_counts[entry] = input_counts[entry]

for k in range(80):
    save = lantern_fish_counts[0]
    for i in range(1, 9):
        lantern_fish_counts[i-1] = lantern_fish_counts[i]
    lantern_fish_counts[8] = save
    lantern_fish_counts[6] += save

total_fish = sum(lantern_fish_counts.values())
print("Total fish after 80 days:", total_fish)

for k in range(256-80):
    save = lantern_fish_counts[0]
    for i in range(1, 9):
        lantern_fish_counts[i-1] = lantern_fish_counts[i]
    lantern_fish_counts[8] = save
    lantern_fish_counts[6] += save

total_fish = sum(lantern_fish_counts.values())
print("Total fish after 256 days:", total_fish)
