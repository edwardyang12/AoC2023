import re
from functools import cache

input = '''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''

# https://advent-of-code.xavd.id/writeups/2023/day/12/
# https://github.com/xavdid/advent-of-code/blob/main/solutions/2023/day_12/solution.py
# I could've cached my solution for part 1 also if I stored: (subsprings, subrecords)
# TLDR if I made my solution substring the springs instead of increase position index

input = input.split("\n")[1:-1]
multiplier = 5

springs = []
records = []
for i in input:
    s, r = i.split(" ")
    full_s = ""
    for _ in range(multiplier):
        full_s += s + "?"
    s = re.sub('[.]+', '.', full_s[:-1])
    springs.append(s)
    records.append(tuple([int(x) for x in r.split(",")]*multiplier))

@cache
def num_valid_solutions(record: str, groups: tuple[int, ...]) -> int:
    if not record:
        # if there are no more spots to check;
        # our only chance at success is if there are no `groups` left
        return len(groups) == 0

    if not groups:
        # if there are no more groups the only possibility of success is that there are no `#` remaining
        # here, `?` are treated as `.`, so no recursion is necessary
        return "#" not in record

    char, rest_of_record = record[0], record[1:]

    if char == ".":
        # dots are ignores, so keep recursing
        return num_valid_solutions(rest_of_record, groups)

    if char == "#":
        group = groups[0]
        # we're at the start of a group! make sure there are enough here to fill the first group
        # to be valid, we have to be:
        if (
            # long enough to match
            len(record) >= group
            # made of only things that can be `#` (no `.`)
            and all(c != "." for c in record[:group])
            # either at the end of the record (allowed)
            # or the next character isn't also a `#` (would be too big)
            and (len(record) == group or record[group] != "#")
        ):
            return num_valid_solutions(record[group + 1 :], groups[1:])

        return 0

    if char == "?":
        return num_valid_solutions("#" + rest_of_record, groups) + num_valid_solutions(
            "." + rest_of_record, groups
        )

total = 0
for s, r in zip(springs, records):
    total += num_valid_solutions(s, r)

print(total)