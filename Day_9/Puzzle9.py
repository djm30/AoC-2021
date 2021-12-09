from collections import defaultdict
import numpy as np

test_data = "Day_9/testinput.txt"
real_data = "Day_9/input.txt"

file = real_data

def get():
    grid = defaultdict(lambda : float('inf'))
    with open(file, "r") as f:
        for x, line in enumerate(f.read().split("\n")):
            for y, num in enumerate(line):
                grid[(x,y)] = int(num)

        return grid,x,y 

grid,x,y = get()

def get_adajcent(x,y):
    return [grid[(x-1, y)], grid[(x+1, y)], grid[(x, y-1)], grid[(x, y+1)]]


def compare(point, vals):
    if point < min(vals):
        return True
    else: return False

def part1():
    low_points = []
    for i in range(x+1):
        for j in range(y+1):
            if compare(grid[i,j],  get_adajcent(i,j)):
                low_points.append(grid[i,j]+1)
    return sum(low_points)


def part2():
    basins = []
    visited_points = set()
    
    def get_basins(x, y):

        W = (x-1, y)
        E = (x+1, y)
        N = (x, y+1)
        S = (x, y-1)

        cum = 0
        for direction in (N,E,S,W):
            x,y = direction
            if grid[x, y] < 9 and direction not in visited_points:
                visited_points.add(direction)
                cum +=1
                cum += get_basins(x,y)
        return cum

    get_basins(0,0)    
    for i in range(0,x+1):
        for j in range(0, y+1):
            if grid[i,j] == 9 or (i,j) in visited_points:
                continue
            basins.append(get_basins(i,j))
    return np.prod(sorted(basins)[-3:])

print(part1())

print(part2())