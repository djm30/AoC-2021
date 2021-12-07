test_data = "testinput.txt"
real_data = "input.txt"

file = real_data

data = list((map(int, open(file, mode="r").read().replace("\n", "").split(sep=","))))

distances = []
sum_distance = 10**100000
for pos in data:
    for i in range(len(data)):
        distances.append(abs(data[i]-pos))
    if sum_distance  > sum(distances):
        sum_distance = sum(distances)
    distances = []  
        
print(f"Part 1: {sum_distance}")


fuel_cost = []
sum_cost = 10**100000
possible_pos = list(range(min(data), max(data)+1))

for i in possible_pos:
    for pos in data:
        n = abs(i-pos)
        n = int((n*(n+1))/2)
        fuel_cost.append(n)
    if sum_cost > sum(fuel_cost):
        sum_cost = sum(fuel_cost)
    fuel_cost = []

print(f"Part 2: {sum_cost}")


