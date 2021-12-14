import numpy as np
with open('input.txt') as f:
    data = f.read().split('\n')
    points = [[int(x) for x in row.split(',')] for row in data[:908]]
    points = [(point[0], point[1]) for point in points]
    instructions = [instruction[11:].split('=') for instruction in data[909:]]


start_shape = (max([point[0] for point in points])+1, max([point[1] for point in points])+1)
start_paper = np.zeros(shape=start_shape)
for point in points:
    start_paper[point] = 1

start_paper = start_paper.transpose()


def fold_paper(paper, instruction):
    shape = paper.shape
    if instruction[0] == 'x':
        fold = int(instruction[1])
        if fold != (shape[1] - 1) / 2:
            print(f"Error: got instruction {instruction} with array shape {paper.shape}")
            raise
        output = np.zeros((shape[0], fold))
        for x in range(output.shape[0]):
            for y in range(output.shape[1]):
                if paper[x][y] == 1:
                    output[x][y] = paper[x][y]
                if paper[x][y + fold + 1] == 1:
                    output[x][fold - (y+1)] = 1
    elif instruction[0] == 'y':
        fold = int(instruction[1])
        if fold != (shape[0]-1)/2:
            print(f"Error: got instruction {instruction} with array shape {paper.shape}")
            raise
        output = np.zeros((fold, shape[1]))
        for x in range(output.shape[0]):
            for y in range(output.shape[1]):
                if paper[x][y] == 1:
                    output[x][y] = paper[x][y]
                if paper[x+fold+1][y] == 1:
                    output[fold-(x+1)][y] = 1
    else:
        print(f"Error!: Received instruction {instruction}")
        raise
    return output

paper = start_paper
for instruction in instructions:
    print(instruction)
    if instruction[0] == 'y':
        if paper.shape[0] % 2 == 0:
            new_paper = np.zeros((paper.shape[0]+1, paper.shape[1]))
            new_paper[:-1, :] = paper
            paper = new_paper
    if instruction[1] == 'x':
        if paper.shape[1] % 2 == 0:
            new_paper = np.zeros((paper.shape[0], paper.shape[1]+1))
            new_paper[:, :-1] = paper
            paper = new_paper
    paper = fold_paper(paper, instruction)
    print(paper.sum())
print(paper)
