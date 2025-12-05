from icecream import ic
from pathlib import Path

file_name = "r.in"
ranges, products = (Path(__file__).parent / file_name).read_text().split("\n\n")
ranges = [r for r in ranges.splitlines()]
products = [p for p in products.splitlines()]

res = 0
for p in products:
    product_id = int(p)
    for r in ranges:
        init, end = r.split("-")
        if product_id > int(init) and product_id <= int(end):
            res += 1
            break

ic(res)
