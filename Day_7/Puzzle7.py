test_data = "testinput.txt"
real_data = "input.txt"

file = real_data

data = list((map(int, open(file, mode="r").read().replace("\n", "").split(sep=","))))

curr_sum, fuel_cost = 0,10**100000
for pos in data:
    for i in range(len(data)):
        curr_sum += abs(data[i]-pos)
    if fuel_cost  > curr_sum:
        fuel_cost = curr_sum
    curr_sum = 0
        
print(f"Part 1: {fuel_cost}")

curr_sum, fuel_cost = 0, 10**100000
possible_pos = list(range(min(data), max(data)+1))

for i in possible_pos:
    for pos in data:
        n = abs(i-pos)
        curr_sum += int((n*(n+1))/2)
    if fuel_cost > curr_sum:
        fuel_cost = curr_sum
    curr_sum = 0

print(f"Part 2: {fuel_cost}")


