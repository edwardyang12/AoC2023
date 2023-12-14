input = '''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''

input = input.split("\n")[1:-1]
turns = [x for x in input[0]]
path = input[2:]
directions = {}
for i in path:
    id, options = i.split(" = ")
    l, r = options.split(", ")
    directions[id] = (l[1:], r[:-1])

steps = 0
current = "AAA"
while current != "ZZZ":
    for dir in turns:
        if current == "ZZZ":
            break
        if dir == "L":
            current = directions[current][0]
        else:
            current = directions[current][1]
        steps+=1

print(steps)