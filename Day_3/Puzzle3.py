import pandas as pd
from copy import deepcopy

#Reading In
df = []
with open(file="./binary.txt", mode="r") as f:
    for line in f:
        df.append(list(line.replace("\n", "")))

df = pd.DataFrame(df)

#Part One
gamma = "".join([df[col].value_counts().index[0] for col in df.columns])
epsilon = "".join(['0' if c=="1" else '1' for c in gamma])

print(f"Gamma: {gamma}\nEpsilon: {epsilon}\nPart One Answer: {int(gamma,2)*int(epsilon,2)}\n")

#Part Two
def get_co2_o2(val):
    p2 = deepcopy(df)
    tie, ind = val
    for col in df.columns:
        counts = p2[col].value_counts()
        if len(p2.index) == 1: break
        if list(counts)[0] == list(counts)[1]: 
            counts = tie
        else: counts = counts.index[ind]
        p2 = p2[p2[col] == counts]
    return int("".join(p2.astype(str).values.flatten().tolist()), 2)

o2 = get_co2_o2(("1", 0))
co2 = get_co2_o2(("0", 1))

print(f"o2: {o2}\nCo2: {co2}\nPart One Answer: {o2*co2}")

