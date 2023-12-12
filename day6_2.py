input = '''
Time:        55     99     97     93
Distance:   401   1485   2274   1405
'''

input = input.split("\n")[1:]

times = input[0].split(":")[1].strip()
times = int(times.replace(" ", ""))
distances = input[1].split(":")[1].strip()
distances = int(distances.replace(" ", ""))

# go from each side because we know ones in the center would fs work
# could prolly do binary search for more optimal find
def winners(time, distance):
    l = 0
    r = time
    while l*(time-l)<= distance:
        l+=1
    while r*(time-r)<= distance:
        r-=1
    return r-l+1

print(winners(times, distances))