input = '''
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''
input = input.split("\n")

# value, length
conversion = {
    'one': [1,3],
    'two': [2,3],
    'three':[3,5],
    'four':[4,4],
    'five':[5,4],
    'six':[6,3],
    'seven':[7,5],
    'eight':[8,5],
    'nine':[9,4]
}
start = {
    'o': ['one'],
    't': ['two','three'],
    'f': ['four','five'],
    's': ['six','seven'],
    'e': ['eight'],
    'n': ['nine']
}

def isword(word, index):
    if word[index] in start:
        for potential in start[word[index]]:
            size = conversion[potential][1]
            if index+size<= len(word) and word[index:index+size] in conversion:
                # print(word[index:index+size])
                return word[index:index+size]
    return None

val = 0
for l in input:
    left_string = ""
    right_string = ""
    left = 0
    right = len(l)-1

    while left<=right:
        left_string = l[left]
        if left_string.isdigit():
            left_string = int(left_string)*10
            break
        left_string = isword(l, left)
        if left_string:
            left_string = int(conversion[left_string][0])*10
            break
        left+=1

    while right>=left: 
        right_string = l[right]
        if right_string.isdigit():
            right_string = int(right_string)
            break
        right_string = isword(l, right)
        if right_string:
            right_string = int(conversion[right_string][0])
            break
        right-=1
    if left<=right:
        val += left_string + right_string
        print(left_string, right_string)
print(val)