import numpy as np

with open('input.txt') as f:
    data = f.read().split('\n')
    data = [[tuple([int(coordinate) for coordinate in point.split(',')]) for point in entry.split(' -> ')] for entry in data]
    data = np.array(data)


class Line:
    def __init__(self, points):
        self.x_0 = points[0][0]
        self.x_1 = points[1][0]
        self.y_0 = points[0][1]
        self.y_1 = points[1][1]
        self.direction = 'diagonal'
        if self.x_0 == self.x_1:
            self.direction = 'vertical'
        if self.y_0 == self.y_1:
            self.direction = 'horizontal'

    def draw(self, grid):
        if self.direction == 'vertical':
            for k in range(self.y_0, self.y_1+1):
                grid[self.x_0, k] += 1
            for k in range(self.y_1, self.y_0+1):
                grid[self.x_0, k] += 1
        if self.direction == 'horizontal':
            for k in range(self.x_0, self.x_1+1):
                grid[k, self.y_0] += 1
            for k in range(self.x_1, self.x_0+1):
                grid[k, self.y_0] += 1
        if self.direction == 'diagonal':
            if self.x_0 < self.x_1 and self.y_0 < self.y_1:
                for k in range(0, self.x_1 - self.x_0 + 1):
                    grid[self.x_0 + k, self.y_0 + k] += 1
            elif self.x_0 < self.x_1 and self.y_0 > self.y_1:
                for k in range(0, self.x_1 - self.x_0 + 1):
                    grid[self.x_0 + k, self.y_0 - k] += 1
            elif self.x_0 > self.x_1 and self.y_0 > self.y_1:
                for k in range(0, self.x_0 - self.x_1 + 1):
                    grid[self.x_0 - k, self.y_0 - k] += 1
            elif self.x_0 > self.x_1 and self.y_0 < self.y_1:
                for k in range(0, self.x_0 - self.x_1 + 1):
                    grid[self.x_0 - k, self.y_0 + k] += 1
        return grid

grid_size = data.max()+1
grid = np.zeros(shape=(grid_size, grid_size))

for entry in data:
    print(entry)
    line = Line(entry)
    grid = line.draw(grid)
    print(grid)

print(grid.transpose())

print((grid > 1).sum())
