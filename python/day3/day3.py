import pandas as pd
import os
print(os.getcwd())
with open('input.txt')as f:
    data = f.read().split('\n')

data = pd.DataFrame(data)

for k in range(len(data.iloc[0][0])):
    data['entry_'+str(k)] = data[0].str[k]

gamma = 0
epsilon = 0
power = len(data.iloc[0][0])-1
for k in range(power+1):
    gamma += int(data['entry_'+str(k)].value_counts().index[0])*2**power
    epsilon += int(data['entry_' + str(k)].value_counts().index[1])*2**power
    power -= 1

print("Part 1:", gamma, epsilon, gamma*epsilon)

data_to_filter = data.copy()
entry = 0
while len(data_to_filter) > 1:
    column = 'entry_'+str(entry)
    value_counts = data_to_filter[column].value_counts()
    if len(value_counts) > 1:
        if value_counts[0] == value_counts[1]:
            common_bit = '1'
        else:
            common_bit = value_counts.index[0]
    else:
        common_bit = value_counts.index[0]
    data_to_filter = data_to_filter.loc[data_to_filter[column] == common_bit]
    entry += 1

og_rating_string = data_to_filter.values[0][0]

def convert_string_to_binary(input_string):
    output = 0
    power = len(input_string)-1
    for k in range(power+1):
        output += int(input_string[k])*2**power
        power -= 1
    return output


data_to_filter = data.copy()
entry = 0
while len(data_to_filter) > 1:
    column = 'entry_'+str(entry)
    value_counts = data_to_filter[column].value_counts()
    if value_counts[0] == value_counts[1]:
        common_bit = '0'
    else:
        common_bit = value_counts.index[1]
    data_to_filter = data_to_filter.loc[data_to_filter[column] == common_bit]
    entry += 1

co2_rating_string = data_to_filter.values[0][0]

og_rating = convert_string_to_binary(og_rating_string)
co2_rating = convert_string_to_binary(co2_rating_string)

print("Part 2: ", og_rating, co2_rating, og_rating*co2_rating)
