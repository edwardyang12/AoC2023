import copy

input = '''
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''

input = input.split("\n")[1:-1]
input = [[int(val) for val in x.split(" ")] for x in input]

def all_zeros(history):
    for i in history:
        if i != 0:
            return False 
    return True

# only need to record differences in first column of each layer and add them while flipping sign each time
total = 0
for i in input:
    first = [i[0]]
    differences = i
    while not all_zeros(differences):
        new_array = []
        for index in range(len(differences)-1, 0, -1):
            new_array.append(differences[index]- differences[index-1])
        new_array.reverse()
        first.append(new_array[0])
        differences= copy.deepcopy(new_array)
    diff = 0
    flip = 1
    for val in first:
        diff += flip * val 
        flip *= -1
    total += diff

print(total)