from icecream import ic
from pathlib import Path

file_name = "r.in"
contents = (Path(__file__).parent / file_name).read_text().strip().splitlines()
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
