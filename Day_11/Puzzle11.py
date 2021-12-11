import numpy as np

test_data = "Day_11/testinput.txt"
real_data = "Day_11/input.txt"

file = real_data

grid = np.array([list(map(int,list(x))) for x in open(file, "r").read().split("\n")])
x_max,y_max = grid.shape
grid = np.pad(grid, (1,1),constant_values=-1000 )

sum_score = 0

def get_surrounding(x,y):
    return [
        (x-1,y-1), (x-1, y), (x-1, y+1),
        (x, y-1),          (x, y+1),
        (x+1, y-1), (x+1, y), (x+1, y+1)
        ]

simultaneous = 0

ndays = 1000

for i in range(ndays):
    #Part 2 - Set ndays to 100 and comment out if statement to get part 1
    if len(grid[grid==0]) == 100:
        simultaneous = i
        break
    grid = grid+1
    flashed = set()
    while True:
        for ix in range(1, x_max+1):
            for iy in range(1, y_max+1):
                if grid[ix, iy] > 9 and (ix, iy) not in flashed:
                    grid[ix, iy] = 0
                    sum_score+=1
                    flashed.add((ix,iy))
                    for x,y in get_surrounding(ix, iy):
                        if not (x,y) in flashed:
                            grid[x,y]+=1
        if not len(grid[grid>9]):
            break
        


print(f"Part One: {sum_score}")
print(f"Part Two: {simultaneous}")
