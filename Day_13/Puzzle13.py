from collections import defaultdict
test_data = "Day_13/testinput.txt"
real_data = "Day_13/input.txt"

file = real_data

instructions = []
points = []
data = defaultdict(lambda: ".")
x_max, y_max = 0,0


#Code to print dictionary 
def print_grid():
    for y in range(y_max+1):
        for x in range(x_max+1):
            print(data[(x,y)], end=" ")
        print("\n")


#Reading in
with open(file, "r") as f:
    get_instruction = False
    for line in f.read().strip().split("\n"):
        if get_instruction:
            axis, value = line.split(sep = " ")[-1].split(sep="=")
            instructions.append((axis, int(value)))
        if line == "":
            get_instruction = True
        if not get_instruction:
            x,y = map(int, line.split(","))
            if x > x_max: x_max = x
            if y > y_max: y_max = y
            data[(x,y)] = "#"
            points.append((x,y))
    print(f.read())

#Method to reflect
def reflect(instruction, x_max, y_max):
    axis, value = instruction
    #Dont know if there is a more efficient way that doesnt violete DRY :(
    if axis == "x":
        points_to_reflect = [point for point in points if point[0] > value]
        for p in points_to_reflect:
            axis = p[0]
            new_x = value - abs(axis-value)
            if (new_x, p[1]) not in points:
                points.append((new_x, p[1]))
            points.remove(p)
        x_max = value - 1

    else:
        points_to_reflect = [point for point in points if point[1] > value]
        for p in points_to_reflect:
            axis = p[1]
            new_y = value - abs(axis-value)
            if (p[0], new_y) not in points:
                points.append((p[0], new_y))
            points.remove(p)
        y_max = value -1
    for point in points:
        x,y = point
        data[(x,y)] = "#"
    return x_max, y_max

#Part One, reflecting with first instruction
x_max, y_max = reflect(instructions[0], x_max, y_max)
print(f"Part One: {len(points)}")

#Part Two, reflecting with rest of instructions
for instruction in instructions[1:]:
    x_max, y_max = reflect(instruction, x_max, y_max)

print("Part 2:")
print_grid()