with open('day1/input.txt', "r") as f:
    data = f.read().split('\n')

count_increase = 0

clean_data = [int(item) for item in data]

last_sum = sum(clean_data[0:3])
for k in range(1, len(clean_data)-2):
    current_sum = sum(clean_data[k:k+3])
    if current_sum > last_sum:
        count_increase += 1
    last_sum = current_sum
print(count_increase)


