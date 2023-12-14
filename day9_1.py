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

# only need to record differences in last column of each layer and just sum them all up for final prediction
total = 0
for i in input:
    last = [i[-1]]
    differences = i
    while not all_zeros(differences):
        new_array = []
        for index in range(len(differences)-1, 0, -1):
            new_array.append(differences[index]- differences[index-1])
        new_array.reverse()
        last.append(new_array[-1])
        differences= copy.deepcopy(new_array)
    for val in last:
        total+= val 

print(total)
