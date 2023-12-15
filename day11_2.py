input = '''
.......#.....#.....................#.............#.................#.........................#..............................................
#.....................#.......#.................................................................................#.......#...................
.......................................................................#.........................#..................................#.......
................................................................#..............#..............................................#.............
.........................................#............................................................#....................................#
.................#..................................................#.......................................................................
...........................#...............................................................................#................................
....#.......#...........................................#..........................#.............................#..........................
....................#.............#........#................................................................................................
...................................................#...................................................#...................#................
.........................#........................................#..................................................#......................
......#..........#...........................................#...........#............#.....................................................
......................................#..........................................#.........................#.....................#..........
.#...................#..................................#.......................................#...........................................
............#.................................#.....................#.......................................................................
............................................................................................................................................
..............................#.....................................................................................#..................#....
....................................................................................#........#......#.......................................
.........................#.........................#............#...........................................#...............................
.#......#.....#.......................#.................#........................................................#.....#....................
...........................................................................#.................................................#..............
...............................................#.......................................#...............#..........................#.........
......................#..................#..................................................................................................
..........................................................................................................................#.................
......#...........................#.........................................................#........................#......................
..............................................................................................................................#.............
..#.......................#.................#............................................................................................#..
..................#....................................................#................#...................................................
....................................................#.....#....................#............................................................
...............................#............................................................................................................
..............................................#...............#..........................................................#...........#......
.#.........#........................#..................................................................#....................................
..........................................................................#.......................#........................................#
...................#......................................................................#.................................................
.............................................................................................................................#..............
.....#......................................................................................................................................
........................................................#........................#..........................................................
.............................#...............#.....................#.....#............#..................#..............................#...
............................................................................................#......#...........#............................
.........................#........#...................................................................................#.....................
...........................................................................................................................................#
.....................................................#.....#.................................................................#..............
#.........................................................................................................#.......................#.........
................#...........................................................#.....................#.........................................
..............................#..............#...................................#.......#...........................#......................
........#................#.........#............................#............................................#.............#.........#......
............................................................................................................................................
.......................................................#...............#.............................#...........................#..........
.............#.................................#............................................................................................
............................................................................................................................................
..#.............................................................................#...........................................#...........#...
............................................................................................................................................
......................................#..........................................................#................#.........................
............................#................#......#......................#...........#....................................................
............................................................................................................................................
....................................................................................................#................#..........#...........
.#............#...................#...............................#........................................#.............................#..
.........#...............................................................#..................................................................
.......................#....................#........#...........................................#..........................................
............................................................#.....................................................#.........................
..............................#.......................................................................#...................#.......#.........
............#.......................#...................#............................#......................................................
...................................................#......................................#..............................................#..
.#................#...................................................#........................#............................................
......#....................................................................#................................#...............................
...............................#....................................................................................#.......................
.........................#.....................#......#.............................................#.................................#.....
............................................................................................................................................
...............#.....................#....................................................#.................................................
..................................................................................................................#.........................
....#......#.....................................#..............................#............................#............#.....#...........
....................#.............................................#....................#.........#.......................................#..
.........................................................#..............#.............................#.....................................
............................#...........#...........................................................................#.......................
............................................................................................................................................
#..................................#...............................................................#..........#.............................
.......#......................................................................................#.................................#.......#...
.....................#....................#...............................#.....#......................................#....................
................................#..........................#......#....................#..........................#.........................
..............#...................................#........................................................................#...............#
....#....................................................................................................#..................................
.......................#....................................................................................................................
......................................#................................#..................#.................................................
.....................................................#............................................#...............................#.........
............................................................................................................................................
............................................................................................................................................
....#.................#..................................#.........................#..........................#.............................
.............#........................................................................................#..................#..................
......................................#............................................................................#........................
.........#....................................................#.........#............................................................#......
.............................................................................................#..............................................
.............................#...........#............................................................................#.....................
#..................#................................................#....................#.......................................#.........#
...................................................................................................#......#.................................
...........#.............................................#...........................#......................................................
....................................#.......................................................................................................
..................................................#..........#.........#......................#.....................#.......................
.#......#....................................#..............................................................#...............................
.............................#.............................................#................................................................
.......................#...............................................................................#....................#...............
....................................................#.....................................#...........................................#.....
................#.....................#..................#.................................................................................#
...#.....#..........................................................#................#......................................................
.............................................#...............#................................#......#......................................
...............................#...............................................#............................................................
.............................................................................................................................#.........#....
.....................#................................................#.................................................#...................
...............#.........................#.......................#..................#.......................................................
.....#......................................................................................................#.......................#.......
....................................#.................#.........................#..................#........................................
........................................................................................................................................#...
.........#..............#.....................................#........................................#.....................#..............
...............................................#...................#........................................................................
......................................#.............#..................................#.....#.......................#......................
............#.....#...............................................................................#.........................................
...#...................................................................................................................................#....
.......................#.........................#..........................................................................................
.........................................................#...........#.........................#........#..........#.............#..........
............................#..............#....................#........................................................#..................
.......#.................................................................#................#.................................................
.................#..................................................................................#........................#...........#..
...................................................#.......#................................................................................
.........................................#......................................#......................................#....................
....................................#...........................................................................#...........................
..............................#.............................................................#...........#.......................#......#....
.........#...............................................#..............#...................................................................
........................#....................#.....................................#........................................................
#...........................................................................................................................................
............................#......................................................................#.......#................................
......................................#.....................................................................................................
.....#............#.........................................#..........................#..........................................#.........
...........................................#......................#..............................................#..........................
..............#..............................................................................#............................#.............#...
..#......#...........................................#..............................#..................#.....#..............................
....................#..........#.....#...............................#......................................................................
............................................................................................................................................
.................................................#..........................................................................................
.............#..........#...............................#...............#.............#..........#.........#........#.......................
............................................#................#.................#............................................................
....................................#....................................................................................#.............#....
'''
    
multiplier = 1000000 - 1

# this took too damn long to debug!!!
def findClosest(arr, target, left = True):
    n = len(arr)
    # Corner cases
    if (target <= arr[0]):
        return -1
    if (target >= arr[n - 1]):
        return n -1
 
    # Doing binary search
    i = 0; j = n; mid = 0
    while (i < j): 
        mid = (i + j) // 2
 
        if (arr[mid] == target):
            return mid
 
        # If target is less than array 
        # element, then search in left
        if (target < arr[mid]):
 
            # If target is greater than previous
            # to mid, return closest of two
            if (mid > 0 and target > arr[mid - 1]):
                return mid-1
 
            # Repeat for left half 
            j = mid
         
        # If target is greater than mid
        else :
            if (mid < n - 1 and target < arr[mid + 1]):
                return mid
                 
            # update i
            i = mid + 1
         
    # Only single element left after search
    return mid
    
input = input.split("\n")[1:-1]

rows = len(input)
col = len(input[0])

galaxies = []
for x in range(len(input)):
    for y in range(len(input[0])):
        if input[x][y] == "#":
            galaxies.append((x,y))

space_x = []
for x in range(len(input)):
    empty = True
    for y in range(len(input[0])):
        if input[x][y] == "#":
            empty = False
            break 
    if empty:
        space_x.append(x)

space_y = []
for y in range(len(input[0])):
    empty = True
    for x in range(len(input)):
        if input[x][y] == "#":
            empty = False
            break 
    if empty:
        space_y.append(y)

# just simple manhattan distance
distances = 0
for x in range(len(galaxies)):
    for y in range(x+1,len(galaxies)):
        x_galaxies = 0 
        y_galaxies = 0
        
        if galaxies[x][0] > galaxies[y][0]:
            x_galaxies = findClosest(space_x, galaxies[x][0], False) - findClosest(space_x, galaxies[y][0], True)
        else:
            x_galaxies = findClosest(space_x, galaxies[y][0], False) - findClosest(space_x, galaxies[x][0], True) 

        if galaxies[x][1] > galaxies[y][1]:
            y_galaxies = findClosest(space_y, galaxies[x][1], False) - findClosest(space_y, galaxies[y][1], True)
        else:
            y_galaxies = findClosest(space_y, galaxies[y][1], False) - findClosest(space_y, galaxies[x][1], True) 

        distances+= abs(galaxies[x][0]- galaxies[y][0]) + x_galaxies * multiplier + abs(galaxies[x][1]- galaxies[y][1]) + y_galaxies * multiplier
print(distances)

# distances = 0
# for x in range(len(galaxies)):
#     for y in range(x+1,len(galaxies)):
#         x_galaxies = 0 
#         y_galaxies = 0
#         for r in space_x:
#             if (galaxies[y][0] < r < galaxies[x][0]) or (galaxies[x][0] < r < galaxies[y][0]):
#                 x_galaxies += 1

#         for r in space_y:
#             if (galaxies[y][1] < r < galaxies[x][1]) or (galaxies[x][1] < r < galaxies[y][1]):
#                 y_galaxies += 1

#         distances+= abs(galaxies[x][0]- galaxies[y][0]) + x_galaxies * multiplier + abs(galaxies[x][1]- galaxies[y][1]) + y_galaxies * multiplier

# print(distances)