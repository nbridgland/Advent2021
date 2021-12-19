import ast
import numpy as np

with open('testinput.txt') as f:
    data = f.read().split('\n')
    data = [ast.literal_eval(entry) for entry in data]


class SnailFishNumber:
    def __init__(self, snail_list):
        self.number = snail_list

    def add(self, number):
        self.number = [self.number, number]
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
        for entry in self.number:
            if type(entry) is list:
                for entry1 in entry:
                    if type(entry1) is list:
                        for entry2 in entry1:
                            if type(entry2) is list:
                                for entry3 in entry2:
                                    if type(entry3) is list:
                                        leftindex = entry2.index(entry3) - 1
                                        if leftindex >= 0:
                                            entry2[leftindex] += entry3[0]
                                        elif entry1.index(entry2) > 0:
                                            if type(entry1[entry1.index(entry2)-1]) == list:
                                                entry1[entry1.index(entry2)-1][-1] += entry3[0]
                                            else:
                                                entry1[entry1.index(entry2)-1] += entry3[0]
                                        elif entry.index(entry1) > 0:
                                            if type(entry[entry.index(entry1)-1]) == list:
                                                if type(entry[entry.index(entry1)-1][-1]) == list:
                                                    entry[entry.index(entry1) -1][-1][-1] += entry3[0]
                                                else:
                                                    entry[entry.index(entry1)-1][-1] += entry3[0]
                                            else:
                                                entry[entry.index(entry1)-1] += entry3[0]
                                        elif self.number.index(entry) > 0:
                                            if type(self.number[self.number.index(entry) - 1]) == list:
                                                if type(self.number[self.number.index(entry) - 1][-1]) == list:
                                                    if type(self.number[self.number.index(entry) - 1][-1][-1]) == list:
                                                        self.number[self.number.index(entry) - 1][-1][-1][-1] += entry3[0]
                                                    else:
                                                        self.number[self.number.index(entry) - 1][-1][-1] += entry3[0]
                                                else:
                                                    self.number[self.number.index(entry)-1][-1] += entry3[0]
                                            else:
                                                self.number[self.number.index(entry) -1] += entry3[0]
                                        rightindex = leftindex + 2
                                        if len(entry2) > rightindex:
                                            if type(entry2[rightindex]) == list:
                                                entry2[rightindex][0] += entry3[1]
                                            else:
                                                entry2[rightindex] += entry3[1]
                                        elif len(entry1) > entry1.index(entry2) + 1:
                                            if type(entry1[entry1.index(entry2) + 1]) == list:
                                                if type(entry1[entry1.index(entry2)+1][0]) == list:
                                                    entry1[entry1.index(entry2) + 1][0][0] += entry3[1]
                                                else:
                                                    entry1[entry1.index(entry2) + 1][0] += entry3[1]
                                            else:
                                                entry1[entry1.index(entry2) + 1] += entry3[1]
                                        elif len(entry) > entry.index(entry1) + 1:
                                            if type(entry[entry.index(entry1) + 1]) == list:
                                                if type(entry[entry.index(entry1) + 1][0]) == list:
                                                    if type(entry[entry.index(entry1)+1][0][0]) == list:
                                                        entry[entry.index(entry1) + 1][0][0][0] += entry3[1]
                                                    else:
                                                        entry[entry.index(entry1) + 1][0][0] += entry3[1]
                                                else:
                                                    entry[entry.index(entry1)+1][0] += entry3[1]
                                            else:
                                                entry[entry.index(entry1)+1] += entry3[1]
                                        elif len(self.number) > self.number.index(entry) + 1:
                                            if type(self.number[self.number.index(entry) + 1]) == list:
                                                if type(self.number[self.number.index(entry) + 1][0]) == list:
                                                    if type(self.number[self.number.index(entry) + 1][0][0]) == list:
                                                        if type(self.number[self.number.index(entry) + 1][0][0][0]) == list:
                                                            self.number[self.number.index(entry) + 1][0][0][0][0] += entry3[1]
                                                        else:
                                                            self.number[self.number.index(entry) + 1][0][0][0] += entry3[1]
                                                    else:
                                                        self.number[self.number.index(entry) + 1][0][0] += entry3[1]
                                                else:
                                                    self.number[self.number.index(entry) + 1][0] += entry3[1]
                                            else:
                                                self.number[self.number.index(entry) + 1] += entry3[1]
                                        entry2[leftindex+1] = 0

    @staticmethod
    def split_number(number):
        if type(number) is list:
            entry0, is_split = SnailFishNumber.split_number(number[0])
            if is_split:
                return [entry0, number[1]], True
            else:
                entry1, is_split = SnailFishNumber.split_number(number[1])
                return [entry0, entry1], is_split
        else:
            if number >= 10:
                return [int(np.floor(number/2)), int(np.ceil(number/2))], True
            else:
                return number, False

    def split(self):
        self.number = self.split_number(self.number)[0]

    @staticmethod
    def get_magnitude(number):
        if type(number) == int:
            return number
        else:
            return 3*SnailFishNumber.get_magnitude(number[0]) + 2*SnailFishNumber.get_magnitude(number[1])

    def magnitude(self):
        return self.get_magnitude(self.number)




test = SnailFishNumber([[[[4,3],4],4],[7,[[8,4],9]]])
test.add([1,1])
print("Test Output:", test.number)

part1 = SnailFishNumber(data[0])
for entry in data[1:]:
    part1.add(entry)
    print("Plus ", entry, " equals ", part1.number)
print("Part 1:", part1.magnitude())

#Part 2
max_magnitude = 0
print(len(data))
k = 0
j = 0

for entry in data:
    print(k)
    k+=1
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

