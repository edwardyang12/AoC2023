import math

input = '''
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

input = input.split("\n")[1:-1]
seeds = [int(x) for x in input[0].split(": ")[1].split(" ")]
input = input[2:]

# process input into map, "mapping" {(source, destination): [(source, destination, range)]}
# "connections" {source: destination}
ranges = []
mapping = {}
connections = {}
map = None
for line in input:
    if len(line)==0:
        mapping[map] = ranges
    elif "map" in line:
        ranges = [] 
        source, destination = line.split(" ")[0].split("-to-")
        map = (source, destination)
        connections[source] = destination 
    else:
        destination, source, range = line.split(" ")
        ranges.append((int(source), int(destination), int(range)))
mapping[map] = ranges

lowest = float(math.inf)

for i in seeds:
    curr = "seed"
    source = i 
    while(curr!="location"):
        conn = (curr, connections[curr])
        ranges = mapping[conn]

        for r in ranges:
            if source>=r[0] and source<=r[0]+r[2]:
                source = source-r[0]+r[1]
                break
        curr = connections[curr]
    lowest = min(lowest, source)
print(lowest)