from os import sep
import numpy as np

# input = "testinput.txt"
input = "input.txt"

class Line():
    def __init__(self, coord_1 : tuple, coord_2: tuple) -> None:
        self.x1 = coord_1[0]
        self.y1 = coord_1[1]
        self.x2 = coord_2[0] 
        self.y2 = coord_2[1]
    
    def get_max_x(self):
        return max([self.x1, self.x2])

    def get_max_y(self):
        return max([self.y1, self.y2])

    def get_line_coords(self):
        if self.x1 == self.x2:
            if self.y2 > self.y1:
                return (self.x1 ,np.arange(self.y1, self.y2 + 1))
            else: return (self.x1, np.arange(self.y2, self.y1 + 1))
                
        if self.y1 == self.y2:
            if self.x2 > self.x1:
                return (np.arange(self.x1, self.x2+1), self.y1)
            else: return (np.arange(self.x2, self.x1+1), self.y1)
        else: 
            dx = np.sign(self.x2 - self.x1)
            dy = np.sign(self.y2 -self.y1)
            x_vals = np.arange(self.x1, self.x2+dx, step=dx)
            y_vals = np.arange(self.y1, self.y2+dy, step=dy)
            return [tuple((x_vals[i], y_vals[i])) for i in range(len(x_vals))]

    def get_straight_coords(self):
        if self.x1 == self.x2:
            if self.y2 > self.y1:
                return (self.x1 ,np.arange(self.y1, self.y2 + 1))
            else: return (self.x1, np.arange(self.y2, self.y1 + 1))
                
        if self.y1 == self.y2:
            if self.x2 > self.x1:
                return (np.arange(self.x1, self.x2+1), self.y1)
            else: return (np.arange(self.x2, self.x1+1), self.y1)
        else: return -1


    def __repr__(self) -> str:
        return f"({self.x1}, {self.y1}) -> ({self.x2}, {self.y2})"

lines = []
with open(file=input, mode="r") as f:
    lines = [[tuple(map(int ,cord.split(sep=","))) for cord in l.split(sep="->")] for l in f.readlines()]
    lines = [Line(l[0], l[1]) for l in lines]

# max_x = max([l.get_max_x() for l in lines])
# max_y = max([l.get_max_y() for l in lines])

class Grid():
    def __init__(self) -> None:
        self.grid = np.zeros((1000, 1000))

    def get_grid(self):
        return self.grid
    
    def __repr__(self) -> str:
        return str(self.grid)

    def draw_line(self, coords: tuple) -> None:
        x, y = coords
        if isinstance(x, np.ndarray):
            for x_val in x:
                self.grid[y, x_val] = self.grid[y, x_val] + 1
        else:
            for y_val in y:
                self.grid[y_val, x] = self.grid[y_val, x] + 1
        return 1


    def draw_line2(self, coords: tuple) -> None:
        if isinstance(coords, tuple):
            x, y = coords
            if isinstance(x, np.ndarray):
                for x_val in x:
                    self.grid[y, x_val] = self.grid[y, x_val] + 1
            elif isinstance(y, np.ndarray):
                for y_val in y:
                    self.grid[y_val, x] = self.grid[y_val, x] + 1
        else:
            for coord in coords:
                self.grid[coord[1], coord[0]] = self.grid[coord[1], coord[0]] + 1


grid = Grid()

for line in lines:
    if not (isinstance(line.get_straight_coords(), int)):
        grid.draw_line(line.get_straight_coords())

print(grid.get_grid()[grid.get_grid() > 1].size)



grid = Grid()

for line in lines:
    if line.get_line_coords() != None:
        grid.draw_line2(line.get_line_coords())
print(grid.get_grid()[grid.get_grid() > 1].size)
