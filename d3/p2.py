from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

contents = open(0).read().splitlines()

jolts = []
for b in contents:
    bcp = b[:]
    jolt = []
    for i in range(12):
        max_ = -1
        remaining_batteries = bcp[: -(11 - len(jolt))]
        if len(jolt) >= 11:
            remaining_batteries = bcp
        max_ = max(remaining_batteries)
        jolt.append(max_)
        index_max = bcp.index(max_)
        bcp = bcp[index_max + 1 :]
    jolts.append(jolt)

total = 0
for j in jolts:
    total += int("".join(j))
ic(total)
