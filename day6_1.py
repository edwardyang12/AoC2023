input = '''
Time:        55     99     97     93
Distance:   401   1485   2274   1405
'''

input = input.split("\n")[1:]

times = input[0].split(":")[1].strip()
times = times.split(" ")
times = [int(time) for time in times if time]
distances = input[1].split(":")[1].strip()
distances = distances.split(" ")
distances = [int(distance) for distance in distances if distance]

# go from each side because we know ones in the center would fs work
def winners(time, distance):
    l = 0
    r = time
    while l*(time-l)<= distance:
        l+=1
    while r*(time-r)<= distance:
        r-=1
    return r-l+1

total = 1
for time, distance in zip(times, distances):
    total *= winners(time, distance)

print(total)