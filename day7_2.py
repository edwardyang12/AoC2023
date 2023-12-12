input = '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''

strength = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")
types = "five, four, full, three, two, one, high".split(", ")
positions = {x:i for i, x in enumerate(strength)}
input = input.split("\n")[1:-1]
hands = [] 
values = {}

for i in input:
    hand, value = i.split(" ")
    hands.append(hand)
    values[hand] = int(value)

def frequency(hand):
    freq = {}
    for i in hand:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq


def place(hand, tree):
    current = tree
    for index, i in enumerate(hand):
        if index == len(hand)-1:
            current[positions[i]] = hand
        else:
            if current[positions[i]] == []:
                current[positions[i]] = [[] for _ in range(len(strength))]
            current = current[positions[i]]
    return tree

mapping = {x: [[]]*len(strength) for x in types}

# dictionary of {type: [tree]} where tree are in order also
# tree -> [[tree]] do for all 5 characters
# find where to map particular hand (guarantee no repeat)
# afterward deserialize by converting dictionary into list

for i in hands:
    occurrences = frequency(i)
    if "J" in occurrences.keys():
        if len(occurrences.values()) == 1 or len(occurrences.values()) == 2 : # five of a kind or four or full
            mapping['five'] = place(i, mapping['five'])
        elif len(occurrences.values()) == 5: # high card
            mapping['one'] = place(i, mapping['one'])
        elif len(occurrences.values()) == 3: # three or two 
            if 3 in occurrences.values(): # three
                mapping['four'] = place(i, mapping['four'])
            else:
                if occurrences["J"]==2:
                    mapping['four'] = place(i, mapping['four'])
                else:
                    mapping['full'] = place(i, mapping['full'])
        else: # one
            mapping['three'] = place(i, mapping['three'])
    else:
        if len(occurrences.values()) == 1: # five of a kind
            mapping['five'] = place(i, mapping['five'])
        elif len(occurrences.values()) == 5: # high card
            mapping['high'] = place(i, mapping['high'])
        elif len(occurrences.values()) == 2: # four or full
            if 4 in occurrences.values(): # four
                mapping['four'] = place(i, mapping['four'])
            else:
                mapping['full'] = place(i, mapping['full'])
        elif len(occurrences.values()) == 3: # three or two 
            if 3 in occurrences.values(): # three
                mapping['three'] = place(i, mapping['three'])
            else:
                mapping['two'] = place(i, mapping['two'])
        else: # one
            mapping['one'] = place(i, mapping['one'])

ordered = []
def dfs(tree, ordered):
    for i in tree:
        if type(i) == str:
            ordered.append(i)
        elif i != []:
            dfs(i, ordered)
            
for i in types:
    tree = mapping[i]
    dfs(tree, ordered)

ordered.reverse()
print(ordered)

total = 0
for index, hand in enumerate(ordered):
    total += (index+1)*values[hand]
print(total)
