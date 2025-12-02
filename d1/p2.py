from pathlib import Path
from icecream import ic

r = True
if r:
    file = Path(__file__).parent / "r1.txt"
else:
    file = Path(__file__).parent / "t1.txt"
with open(file) as f:
    lines = f.readlines()
nzero = 0
curr = 50
for line in lines:
    direction, times = line[0], int(line[1:])
    for _ in range(times):
        curr += -1 if direction == "L" else 1
        curr = curr % 100
        if curr == 0:
            nzero += 1
ic(nzero)
