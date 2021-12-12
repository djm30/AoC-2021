from enum import Enum
import numpy as np
from typing import List

test_data = "Day_12/testinput.txt"
real_data = "Day_12/input.txt"


#     start
#     /   \
# c--A-----b--d
#     \   /
#      end

# start,A,b,A,c,A,end
# start,A,b,A,end
# start,A,b,end
# start,A,c,A,b,A,end
# start,A,c,A,b,end
# start,A,c,A,end
# start,A,end
# start,b,A,c,A,end
# start,b,A,end
# start,b,end

class Size(Enum):
    SMALL = 0
    BIG = 1

file = real_data


class Point():
    def __init__(self, name : str, size : Size ) -> None:
        self.name = name
        self.size = size
        self.connected = []
    
    def __eq__(self, __o: object) -> bool:
        return self.name == __o

    def add_point(self, point : object) -> None:
        if point != "start":
            self.connected.append(point)

    def __repr__(self) -> str:
        return self.name


points = []

def get_point(point_name: str) -> Point:
    for point in points:
        if point.name == point_name:
            return point

#Reading in
lines = open(file, "r").read().split("\n")

#Adding points
counter = 0
for line in lines:
    p1, p2 = line.split(sep="-")
    for point in [p1, p2]:
        #Creating and adding points to points list
        if point not in points:
            if point.lower() != point:
                points.append(Point(point, Size.BIG))
            else:
                if point in ["start", "end"]:
                    points.append(Point(point, Size.BIG))
                else:
                    points.append(Point(point, Size.SMALL))
    #Adding connections between points
    get_point(p1).add_point(get_point(p2))
    get_point(p2).add_point(get_point(p1))
    
start = get_point("start")
end = get_point("end")

paths = []
#Part One
def get_path(point : Point, current_path : List):
    path = []
    path.extend(current_path)
    if not(point.size == Size.SMALL and point in path):
        path.append(point)
        if(path[-1] == "end"):
            if path not in paths:
                paths.append(path)
        else:
            for p in point.connected:
                get_path(p, path)
    
get_path(start, [])
print(f"Part One: {len(paths)}")


#Part 2

paths = []

def get_path(point : Point, current_path : List, first_small_cave):
    path = []
    path.extend(current_path)

    if not first_small_cave:
        for p in path:
            if p.size == Size.SMALL:
                if path.count(p) >= 2:
                    first_small_cave = True


    if not first_small_cave or not (point.size == Size.SMALL and  point in path):
        path.append(point)
        if(path[-1] == "end"):
            if path not in paths:
                paths.append(path)
        else:
            for p in point.connected:
                get_path(p, path, first_small_cave)

get_path(start, [], False)
print(f"Part Two: {len(paths)}")