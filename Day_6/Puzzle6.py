test_data = "testinput.txt"
real_data = "input.txt"

file = real_data

fish = [0,0,0,0,0,0,0,0,0]

data = list((map(int, open(file, mode="r").read().replace("\n", "").split(sep=","))))
for lantern in data:
    fish[lantern] +=1
    
num_days = 256

for _ in range(num_days):
    zero_val = fish[0]
    for i in range(len(fish)-1):
        fish[i] = fish[i+1]
    fish[6] = fish[6] + zero_val
    fish[8] = zero_val

print(f"Day: {num_days} Fish Count: {sum(fish)}")

#Takes 0.0355004000011831 to run!