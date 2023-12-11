input = '''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''

input = input.split("\n")[1:-1]

comparison = [12,13,14]

# output hashmap of game id: [max of each color]
# [r,g,b]
def process_input(input):
    max_cubes = {}
    for i in input:
        id, all_hand = i.split(": ")
        id = int(id.split(" ")[1])
        max_color = [0, 0, 0]
        for hand in all_hand.split("; "):
            for color in hand.split(", "):
                val, color = color.split(" ")
                if color == "blue":
                    max_color[2] = max(max_color[2],int(val))
                elif color == "red":
                    max_color[0] = max(max_color[0],int(val))
                else:
                    max_color[1] = max(max_color[1],int(val))
        max_cubes[id] = max_color 
    return max_cubes 

max_cubes = process_input(input)
total = 0
for id, max_color in max_cubes.items():
    possible = True
    for index, val in enumerate(max_color):
        if val>comparison[index]:
            possible = False 
    if possible:
        total+=id 
print(total)