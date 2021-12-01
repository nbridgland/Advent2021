with open('day1/input.txt', "r") as f:
    data = f.read().split('\n')

count_increase = 0
last_number = int(data[0])
for number in data[1:]:
    number = int(number)
    if number > last_number:
        count_increase += 1
    last_number = number
print(count_increase)


