from icecream import ic
from pathlib import Path

file_name = "r.in"
ranges, products = (Path(__file__).parent / file_name).read_text().split("\n\n")
# [[3,5], ...]
ranges = [[int(r.split("-")[0]), int(r.split("-")[1])] for r in ranges.splitlines()]
products = [p for p in products.splitlines()]

res = 0
for p in products:
    product_id = int(p)
    for init, end in ranges:
        # init, end = int(init), int(end)
        if init <= product_id <= end:
            res += 1
            break

ic(res)
