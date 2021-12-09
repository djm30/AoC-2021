import numpy as np

test_data = "Day_9/testinput.txt"
real_data = "Day_9/input.txt"

file = real_data

grid = np.array([list(map(int,list(x))) for x in open(file, "r").read().split("\n")])
x_max,y_max = grid.shape
grid = np.pad(grid, ((1,1),(1,1)), "maximum")


def get_neighbours(x,y):
    return [grid[x+1,y], grid[x-1, y], grid[x,y+1], grid[x, y-1]]

def compare(point, neighbours):
    return point < min(neighbours)

def part1():
    low_points = []
    low_points_index = []
    for x in range(1, x_max+1):
        for y in range(1, y_max+1):
            if compare(grid[x,y], get_neighbours(x,y)):
                low_points.append(grid[x,y]+1)
                low_points_index.append((x,y))
    return low_points, low_points_index

def part2(low_points_index : list):
    basins = []
    visited_points = set()

    def get_basins(x,y):

        UP = (x+1, y)
        RIGHT = (x, y+1)
        DOWN = (x-1, y)
        LEFT = (x, y-1)

        count = 0
        for direction in [UP, DOWN, LEFT, RIGHT]:
            x,y = direction
            if grid[x,y] < 9 and direction not in visited_points:
                visited_points.add(direction)
                count +=1
                count += get_basins(x,y)
        return count
    for point in low_points_index:
        x,y = point
        basins.append(get_basins(x,y))
    return np.prod(sorted(basins)[-3:])


low_points, low_points_index = part1()
print(sum(low_points))
print(part2(low_points_index))