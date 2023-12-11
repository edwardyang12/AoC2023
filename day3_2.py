input = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

input = input.split("\n")[1:-1]

def process_input(input):
    row, col = len(input), len(input[0])
    processed = [["" for _ in range(col)] for _ in range(row)]
    for x in range(row):
        for y in range(col):
            processed[x][y] = input[x][y]
    return processed 

def special(input):
    return input!="." and not input.isnumeric()

input = process_input(input)
row, col = len(input), len(input[0])

# preprocess all numbers by finding the symbol it is connected to (r,c,symbol): [number]
# if exactly 2, multiply them 

total = 0
number = 0
symbol = None
connections = {}
for x in range(row):
    for y in range(col):

        if input[x][y].isnumeric():
            number = number*10 + int(input[x][y])
            input[x][y] = "."
            if x-1>=0 and special(input[x-1][y]):
                symbol=(x-1,y,input[x-1][y])
            if x+1< row and special(input[x+1][y]):
                symbol=(x+1,y,input[x+1][y])
            if y-1>=0 and special(input[x][y-1]):
                symbol=(x,y-1,input[x][y-1])
            if y+1 < col and special(input[x][y+1]):
                symbol=(x,y+1,input[x][y+1])
            if x-1>=0 and y-1>=0 and special(input[x-1][y-1]):
                symbol=(x-1,y-1,input[x-1][y-1])
            if x+1 < row and y+1 < col and special(input[x+1][y+1]):
                symbol=(x+1,y+1,input[x+1][y+1])
            if x-1>=0 and y+1 < col and special(input[x-1][y+1]):
                symbol=(x-1,y+1,input[x-1][y+1])
            if x+1 < row and y-1 >=0 and special(input[x+1][y-1]):
                symbol=(x+1,y-1,input[x+1][y-1])
        else:
            if symbol:
                if symbol in connections:
                    connections[symbol].append(number)
                else:
                    connections[symbol] = [number]
            number = 0
            symbol = None
    if symbol:
        if symbol in connections:
            connections[symbol].append(number)
        else:
            connections[symbol] = [number]
    number = 0
    symbol = None
if symbol:
    if symbol in connections:
        connections[symbol].append(number)
    else:
        connections[symbol] = [number]

for key, value in connections.items():
    if key[2] == '*' and len(value)==2:
        total+= value[0] * value[1]
print(total)