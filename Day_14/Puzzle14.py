from collections import defaultdict
from typing import Counter

test_data = "Day_14/testinput.txt"
real_data = "Day_14/input.txt"

file = real_data

mapping = defaultdict(lambda: None)
count = defaultdict(lambda: 0)
char_count = defaultdict(lambda: 0)

initial_input = []

#Reading in
with open(file, "r") as f:
    initial_input = list(f.readline().replace("\n", "").strip())
    f.readline()
    for line in f.readlines():
        char, char_map = line.replace("\n", "").split(" -> ")
        mapping[char] = char_map

#Inital pattern counts
for i in range(len(initial_input)-1):
    pattern = initial_input[i] + initial_input[i+1]
    count[pattern] +=1

#Initial char counts
for char in initial_input:
    char_count[char] += 1



#Number of steps for respective part
# n_steps  = 10
n_steps  = 40

#Iterating through each part
for _ in range(n_steps):
    new_counts = []
    for key, value in count.items():
        # NN -> NC, CN
        middle_char = mapping[key]
        first_key = key[0] + middle_char
        second_key = middle_char + key[1]
        new_counts.append((first_key, value))
        new_counts.append((second_key, value))
        char_count[middle_char] += value
    count = defaultdict(lambda: 0)
    for key, value in new_counts:
        count[key] += value

#Getting most and least common character
most_char = max(char_count.keys(), key=(lambda k: char_count[k]))
least_char = min(char_count.keys(), key=(lambda k: char_count[k]))

#Displaying output
print(f"Maximum Value: {most_char} , {char_count[most_char]}")
print(f"Minimum Value: {least_char} , {char_count[least_char]}")
print(f"Answer: {char_count[most_char] - char_count[least_char]}")