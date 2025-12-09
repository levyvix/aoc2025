from icecream import ic
from pathlib import Path

ranges, products = open(0).read().split("\n\n")
# [[3,5], ...]
ranges = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in ranges.splitlines()]
products = [p for p in products.splitlines()]

res = 0
for p in products:
    product_id = int(p)
    for init, end in ranges:
        if init <= product_id <= end:
            res += 1
            break

ic(res)
