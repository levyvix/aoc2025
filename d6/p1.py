from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

contents = open(0).read().strip().splitlines()
clean_cont = []
for c in contents:
    clean_cont.append(c.strip().split())
res = 0
for numbers in zip(*clean_cont):
    nums, op = numbers[:-1], numbers[-1]
    total = int(nums[0])
    for n in nums[1:]:
        total = eval(f"{total} {op} {n}")
    res += total
ic(res)
