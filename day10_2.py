import copy 
import math

input = '''
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
'''

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
# based on part 1 solution
# flood fill and remaining inf are total

stack = [(start, 'N'), (start, 'S'), (start, 'E'), (start, 'W')] # (position, number, direction)

while stack: 
    pos, dir = stack.pop()
    grid_result[pos[0]][pos[1]] = 1
    row, col = pos[0] + direction_coords[dir][0], pos[1] + direction_coords[dir][1]
    if grid_string[row][col] in direction_available[dir]:
        new_dir = direction_transform[(grid_string[row][col], dir)]
        stack.append(((row, col), new_dir))


grid_result.insert(0, [math.inf for _ in range(len(grid_result[0]))])
grid_result.append([math.inf for _ in range(len(grid_result[0]))])
for i in range(len(grid_result)):
    grid_result[i].insert(0, math.inf)
    grid_result[i].append(math.inf)

# add borders to start flood fill
stack = [(0, x) for x in range(len(grid_result[0]))]
stack += [(len(grid_result)-1, x) for x in range(len(grid_result[0]))]
stack += [(x, 0) for x in range(len(grid_result))]
stack += [(x, len(grid_result[0])) for x in range(len(grid_result))]

valid_dir = direction_coords.values()

crawl = [] # places that are can be between pipes
# flood fill
while stack:
    pos = stack.pop()
    for dir in valid_dir:
        row, col = pos[0] + dir[0], pos[1] + dir[1]
        if row < 0 or row >= len(grid_result):
            continue 
        elif col < 0 or col >= len(grid_result[0]):
            continue 

        if grid_result[row][col] == math.inf:
            grid_result[row][col] = 0
            stack.append((row, col))
        elif grid_result[row][col] == 1:
            if grid_string[row-1][col-1] == "J" and (grid_string[row-1][col] == "|" or grid_string[row-1][col] == "|") and dir == (-1,0): # up pipe 
                while grid_string

# remove borders of flood fill 
grid_result = grid_result[1:-1]
for i in range(len(grid_result)):
    grid_result[i] = grid_result[i][1:-1]

print(grid_result)