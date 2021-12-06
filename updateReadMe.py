import re

lines = open("README.md", mode="r").readlines()


pattern = r"-(\d{1,2})-"

curr_day = int(re.findall(pattern ,str(lines[2]))[0])
next_day = "-" + str(curr_day+1) + "-"
total_stars =  "-" + str((curr_day+1) * 2) + "-"

lines[2] = re.sub(pattern, next_day ,lines[2])
lines[3] = re.sub(pattern, total_stars ,lines[3])
lines[4] = re.sub(pattern, next_day ,lines[4])

open("README.md", mode="w").write("".join(lines))

print("README Updated")