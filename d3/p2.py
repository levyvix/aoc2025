from icecream import ic
from pathlib import Path

file_name = "real.txt"
contents = (Path(__file__).parent / file_name).read_text().splitlines()

jolts = []
for b in contents:
    bcp = b[:]
    jolt = []
    for i in range(12):
        max_ = -1
        remaining_batteries = bcp[: -(11 - len(jolt))]
        if len(jolt) >= 11:
            remaining_batteries = bcp
        for n in remaining_batteries:
            n = int(n)
            max_ = max(max_, n)
        jolt.append(str(max_))
        index_max = bcp.index(str(max_))
        bcp = bcp[index_max + 1 :]
    jolts.append(jolt)

total = 0
for j in jolts:
    total += int("".join(j))
ic(total)
