with open('input.txt') as f:
    INSTRUCTIONS = f.read().split('\n')
    INSTRUCTIONS = [instruction.split(' ') for instruction in INSTRUCTIONS]


class Monad:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w


    def inp(self, string):
        exec(f"self.{string} = {int(self.number[self.digit])}")
        self.digit += 1

    def add(self, string1, string2):
        try:
            b = int(string2)
            exec(f"self.{string1} = self.{string1} + {b}")
        except ValueError:
            exec(f"self.{string1} = self.{string1} + self.{string2}")

    def mul(self, string1, string2):
        try:
            b = int(string2)
            exec(f"self.{string1} = self.{string1} * {b}")
        except ValueError:
            exec(f"self.{string1} = self.{string1} * self.{string2}")

    def div(self, string1, string2):
        try:
            b = int(string2)
            exec(f"self.a = self.{string1}")
            if (self.a < 0 < b) or (b < 0 < self.a):
                exec(f"self.{string1} = -(-self.{string1} // {b})")
            else:
                exec(f"self.{string1} = self.{string1} // {b}")
        except ValueError:
            exec(f"self.b = self.{string2}")
            exec(f"self.a = self.{string1}")
            if (self.a < 0 < self.b) or (self.b < 0 < self.a):
                exec(f"self.{string1} = -(-self.{string1} // {b})")
            else:
                exec(f"self.{string1} = self.{string1} // self.{string2}")

    def mod(self, string1, string2):
        try:
            b = int(string2)
            exec(f"self.{string1} = self.{string1} % {b}")
        except ValueError:
            exec(f"self.{string1} = self.{string1} % self.{string2}")

    def eql(self, string1, string2):
        try:
            b = int(string2)
            exec(f"self.{string1} = int(self.{string1} == {b})")
        except ValueError:
            exec(f"self.{string1} = int(self.{string1} == self.{string2})")


CHECKED_HASH = {}


def find_max_number(monad, instructions, inputline):
    #x and y don't matter because they get mulitplied by 0 each round
    hashed = 'z' + str(monad.z) + 'w' + str(monad.w) + 'l' + str(inputline)
    checked = CHECKED_HASH
    if inputline == 14:
        if monad.z > 26:
            return None
        if monad.z % 26 - 13 != monad.w:
            return None
        return 'a'
    if inputline < 5:
        print("W: ",monad.w)
        print("Stored at this inputline: ", len(checked))
        print("Input line", inputline)
    if hashed in checked:
        return None
    for j in range(len(instructions)):
        instruction = instructions[j]
        if instruction[0] == 'inp':
            k = 1
            while k < 10:
                new_monad = Monad(monad.x, monad.y, monad.z, k)
                remaining_digits = find_max_number(new_monad, instructions[j+1:], inputline + 1)
                if remaining_digits is not None:
                    return str(k) + remaining_digits
                k += 1
            checked[hashed] = False
            return None
        elif instruction[0] == 'add':
            monad.add(instruction[1], instruction[2])
        elif instruction[0] == 'mul':
            monad.mul(instruction[1], instruction[2])
        elif instruction[0] == 'div':
            monad.div(instruction[1], instruction[2])
        elif instruction[0] == 'mod':
            monad.mod(instruction[1], instruction[2])
        elif instruction[0] == 'eql':
            monad.eql(instruction[1], instruction[2])
        else:
            raise
    if monad.z == 0:
        return ''
    else:
        checked[hashed] = False
        return None


if __name__ == "__main__":
    monad = Monad(0, 0, 0, 0)
    print(find_max_number(monad, INSTRUCTIONS, 0))


#Code for finding differences in code blocks, for posterity
"""with open('input.txt') as f:
    instruction_blocks = f.read().split('inp w\n')
    instructions = [instruction_block.split('\n') for instruction_block in instruction_blocks]
    instructions = [[instruction.split(' ') for instruction in instruction_block] for instruction_block in instructions]
    instructions = instructions[1:]
common_instructions = {}
for line in range(len(instructions[0])):
    if instructions[0][line] == ['']:
        continue
    common = True
    for k in range(len(instructions)):
        if instructions[k][line] != instructions[0][line]:
            common = False
    if common:
        common_instructions[line] = instructions[0][line]

for k in range(len(instructions[0])):
    if k not in common_instructions:
        print(k)
        for instruction_block in instructions:
            print(instruction_block[k])
        print('\n')"""
