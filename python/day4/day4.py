import numpy as np
with open('input.txt') as f:
    data = f.read().split('\n\n')


class BingoBoard:
    def __init__(self, grid):
        grid = grid.split('\n')
        self.grid = np.array([[int(i) for i in row.split(' ') if i != ""] for row in grid])
        self.marked_grid = np.zeros(self.grid.shape)
        self.won = False

    def mark_number(self, number):
        for col in range(self.grid.shape[0]):
            for row in range(self.grid.shape[0]):
                if self.grid[row][col] == number:
                    self.marked_grid[row][col] = 1
                    self.won = self.is_won()

    def is_won(self):
        if (self.marked_grid.sum(axis=1) == 5).any():
            return True
        if (self.marked_grid.sum(axis=0) == 5).any():
            return True
        return False

# Part 1
boards = [BingoBoard(grid) for grid in data[1:]]
numbers = [int(i) for i in data[0].split(',')]

won = False
for number in numbers:
    if won:
        break
    for board in boards:
        if won:
            break
        board.mark_number(number)
        if board.won:
            won = True
            sum_unmarked = (board.grid*(1-board.marked_grid)).sum()
            print("Part 1: ", number, sum_unmarked, number*sum_unmarked)
            break

# Part 2
boards = [BingoBoard(grid) for grid in data[1:]]
numbers = [int(i) for i in data[0].split(',')]
for number in numbers:
    for board in boards:
        if board.won:
            continue
        board.mark_number(number)
        if board.won:
            sum_unmarked = (board.grid*(1-board.marked_grid)).sum()
            print(number, sum_unmarked, number*sum_unmarked)