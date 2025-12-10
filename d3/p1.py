from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

content = open(0).read()
batteries = [line for line in content.strip().splitlines()]

max_b = 0
for b in batteries:
    ints_b = list(map(int, b))
    tens = max(ints_b[:-1])
    ones = max(ints_b[ints_b.index(tens) + 1 :])
    max_b += tens * 10 + ones


ic(max_b)
