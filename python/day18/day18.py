import ast
import numpy as np

with open('input.txt') as f:
    data = f.read().split('\n')
    data = [ast.literal_eval(entry) for entry in data]


def parse_number_list(snail_fish_entry, path = ''):
    if type(snail_fish_entry) == list:
        output = []
        output = output + parse_number_list(snail_fish_entry[0], path=path + 'l')
        output = output + parse_number_list(snail_fish_entry[1], path=path + 'r')
    else:
        output = [{'value': snail_fish_entry, 'path': path}]
    return output


class SnailFishNumber:
    def __init__(self, snail_list):
        self.number = parse_number_list(snail_list)

    @staticmethod
    def increase_depth(number, direction):
        for item in number:
            item['path'] = direction + item['path']
        return number

    def add(self, add_number):
        add_snail_fish_number = parse_number_list(add_number)
        self.number = SnailFishNumber.increase_depth(self.number, 'l') + SnailFishNumber.increase_depth(add_snail_fish_number, 'r')
        self.reduce()

    def reduce(self):
        current = self.number.copy()
        self.explode()
        self.split()
        new = self.number.copy()
        while current != new:
            current = new
            self.explode()
            self.split()
            new = self.number.copy()

    def explode(self):
        k = 0
        while k < len(self.number):
            if len(self.number[k]['path']) > 4:
                # should be first of pair that's too deep:
                if k > 0:
                    self.number[k-1]['value'] += self.number[k]['value']
                if len(self.number) > k + 2:
                    self.number[k+2]['value'] += self.number[k+1]['value']
                self.number = self.number[:k] + [{'value': 0, 'path': self.number[k]['path'][:-1]}] + self.number[k+2:]
            k += 1

    def split(self):
        for k in range(len(self.number)):
            if self.number[k]['value'] >= 10:
                old_value = self.number[k]
                new_pair = [{'value': int(np.floor(old_value['value'] / 2)), 'path': old_value['path'] + 'l'},
                            {'value': int(np.ceil(old_value['value'] / 2)), 'path': old_value['path'] + 'r'}]
                self.number = self.number[:k] + new_pair + self.number[k+1:]
                break

    def magnitude(self):
        output = 0
        for item in self.number:
            value = item['value']
            for char in item['path']:
                if char == 'l':
                    value *= 3
                else:
                    value *= 2
            output += value
        return output

test = SnailFishNumber([[[[4,3],4],4],[7,[[8,4],9]]])
test.add([1,1])
print("Test Output:", test.number)

part1 = SnailFishNumber(data[0])
for entry in data[1:]:
    part1.add(entry)
    print("Plus ", entry, " equals ", part1.number)

print("Part1 value: ", part1.number)
print("Part 1: ", part1.magnitude())

#Part 2
max_magnitude = 0
for entry in data:
    for entry1 in data:
        sum1 = SnailFishNumber(entry)
        sum2 = SnailFishNumber(entry1)
        sum1.add(entry1)
        sum1mag = sum1.magnitude()
        sum2.add(entry)
        sum2mag = sum2.magnitude()
        if sum1mag > max_magnitude:
            max_magnitude = sum1mag
        if sum2mag > max_magnitude:
            max_magnitude = sum2mag

print("Part 2: ", max_magnitude)
