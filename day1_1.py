input = '''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''
input = input.split("\n")

val = 0
for l in input:
    left = 0
    right = len(l)-1
    while left<=right and not l[left].isdigit():
        left+=1
    while right>=left and not l[right].isdigit():
        right-=1
    if left<=right:
        val += int(l[left]+l[right])
print(val)