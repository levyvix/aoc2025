from icecream import ic

with open("r1.txt") as f:
    lines = f.readlines()
nzero = 0
curr = 50
for l in lines:
    direction, times = l[0], l[1:]
    if direction == "L":
        curr = (curr - int(times)) % 100
    else:
        curr = (curr + int(times)) % 100
    ic(curr)
    if curr == 0:
        nzero += 1
print(nzero)
