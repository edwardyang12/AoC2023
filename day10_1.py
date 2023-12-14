import copy 
import math

input = '''
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
'''

# input = '''
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# '''

input = input.split("\n")[1:-1]
start = None
grid_string = []
grid_result = []

for x in range(len(input)):
    row = []
    for y in range(len(input[0])):
        row.append(input[x][y])
        if input[x][y] == "S":
            start = (x, y)
    grid_string.append(copy.deepcopy(row))
    grid_result.append([float(math.inf) for _ in range(len(row))])

# pipe transforms direction
direction_transform = {
    ('J', 'E'): 'N',
    ('J', 'S'): 'W',
    ('|', 'S'): 'S',
    ('|', 'N'): 'N',
    ('-', 'E'): 'E',
    ('-', 'W'): 'W',
    ('L', 'S'): 'E',
    ('L', 'W'): 'N',
    ('7', 'N'): 'W',
    ('7', 'E'): 'S',
    ('F', 'N'): 'E',
    ('F', 'W'): 'S'
}

direction_available = {}
for tile, dir in direction_transform.keys():
    if dir not in direction_available:
        direction_available[dir] = [tile]
    else:
        direction_available[dir].append(tile)

direction_coords = {
    'S': (1, 0),
    'N': (-1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

# DFS from starting point on 2D array
# min at each step 

stack = [(start, 0, 'N'), (start, 0, 'S'), (start, 0, 'E'), (start, 0, 'W')] # (position, number, direction)

while stack: 
    pos, count, dir = stack.pop()
    grid_result[pos[0]][pos[1]] = min(count, grid_result[pos[0]][pos[1]])
    row, col = pos[0] + direction_coords[dir][0], pos[1] + direction_coords[dir][1]
    if grid_string[row][col] in direction_available[dir]:
        # print(grid_string[row][col], row, col)
        new_dir = direction_transform[(grid_string[row][col], dir)]
        # print(new_dir)
        stack.append(((row, col), count+1, new_dir))
largest = 0
for x in range(len(grid_result)):
    for y in range(len(grid_result[0])):
        if grid_result[x][y] != math.inf:
            largest = max(largest, grid_result[x][y])

print(largest)