with open('python/day2/input.txt') as f:
    data = f.read().split('\n')
horizontal = 0
depth = 0
aim = 0
for entry in data:
    if entry.startswith('forward'):
        horizontal += int(entry.split(' ')[1])
    if entry.startswith('up'):
        depth -= int(entry.split(' ')[1])
    if entry.startswith('down'):
        depth += int(entry.split(' ')[1])

print(horizontal, depth, horizontal * depth)

horizontal = 0
depth = 0
aim = 0

for entry in data:
    if entry.startswith('forward'):
        horizontal += int(entry.split(' ')[1])
        depth += aim*int(entry.split(' ')[1])
    if entry.startswith('up'):
        aim -= int(entry.split(' ')[1])
    if entry.startswith('down'):
        aim += int(entry.split(' ')[1])

print(horizontal, depth, horizontal * depth)


