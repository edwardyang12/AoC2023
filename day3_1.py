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
# 2d array with each number/ char as a spot
# iteratively traverse through 2d array
# going right to increase number (replace with periods after)
# if there's any symbol in any direction of number then mark boolean as true
# once we hit a non number then we reset everything 
# if boolean add number to sum

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

total = 0
number = 0
symbol = False
for x in range(row):
    for y in range(col):

        if input[x][y].isnumeric():
            number = number*10 + int(input[x][y])
            input[x][y] = "."
            if x-1>=0 and special(input[x-1][y]):
                symbol=True
            if x+1< row and special(input[x+1][y]):
                symbol=True
            if y-1>=0 and special(input[x][y-1]):
                symbol=True
            if y+1 < col and special(input[x][y+1]):
                symbol=True
            if x-1>=0 and y-1>=0 and special(input[x-1][y-1]):
                symbol=True
            if x+1 < row and y+1 < col and special(input[x+1][y+1]):
                symbol=True
            if x-1>=0 and y+1 < col and special(input[x-1][y+1]):
                symbol=True
            if x+1 < row and y-1 >=0 and special(input[x+1][y-1]):
                symbol=True
        else:
            if symbol:
                total += number 
            number = 0
            symbol = False
    if symbol:
        total += number 
    number = 0
    symbol = False
if symbol:
    total += number 
number = 0
symbol = False
print(total)