import re
from collections import namedtuple


filepath = "./directions.txt"
Location = namedtuple("Location", "horizontal depth")

class Location():

    def __init__(self):
        self.horizontal = 0
        self.depth = 0

    @property
    def horizontal(self):
        return self.horizontal

    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = value

    @property
    def depth(self):
        return self.depth

    @depth.setter
    def depth(self, value):
        self._depth = value
    
    def increment_horizontal(self, increment):
        self.horizontal = self.horizontal + increment

    def increment_depth(self, increment):
        self.depth = self.depth + increment

    def __repr__(self):
        return str((self.horizontal, self.depth))

    def final_result(self):
        return self.horizontal * self.depth
        
class Location2():
    def __init__(self):
        self.aim = 0
        self.horizontal = 0
        self.depth = 0

    @property
    def aim(self):
        return self.aim
    
    @aim.setter
    def aim(self, value):
        self._aim = value
    
    @property
    def horizontal(self):
        return self.horizontal
    
    @horizontal.setter
    def horizontal(self, value):
        self._horizontal = value

    @property
    def depth(self):
        return self.depth
    
    @depth.setter
    def depth(self, value):
        self._depth = value

    def increment_aim(self, value):
        self.aim = self.aim + value

    def move_forward(self, value):
        self.horizontal = self.horizontal + value
        self.depth = self.depth + (self.aim * value)

    def __repr__(self):
        return str((self.horizontal, self.depth, self.aim))

    def final_result(self):
        return self.depth * self.horizontal


def read_from_file():
    directions = []
    pattern = r"(forward|up|down)\s(\d*)"
    with open(filepath, mode="r") as f:
        for line in f:
            match = re.match(pattern=pattern, string=line)
            directions.append({
                "direction" : match.group(1),
                "value" : int(match.group(2))
            })
    return directions
            

def apply_direction_part_one(directions, location):
    direction = directions["direction"]
    value = directions["value"]
    if direction == "forward":
        location.increment_horizontal(value)
    elif direction == "up":
        location.increment_depth(-value)
    elif direction == "down":
        location.increment_depth(value)


def apply_direction_part_two(directions, location):
    direction = directions["direction"]
    value = directions["value"]
    if direction == "forward":
        location.move_forward(value)
    elif direction == "up":
        location.increment_aim(-value)
    elif direction == "down":
        location.increment_aim(value)
    print(location)

def main():
    directions = read_from_file()
    location = Location()
    map(lambda x: apply_direction_part_one(x, location), directions)
    print(location)
    print(location.final_result())

    print("\n+----------------------------+\n")

    location = Location2()
    map(lambda x: apply_direction_part_two(x, location), directions)
    print(location)
    print(location.final_result())

if __name__ == "__main__":
    main()