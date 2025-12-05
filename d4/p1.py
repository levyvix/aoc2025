from pathlib import Path
from icecream import ic

grid = [l.strip() for l in (Path(__file__).parent / "r.in").read_text().splitlines()]
row_len = len(grid)
col_len = len(grid[0])

dirs = [-1, 0, 1]
res = 0
for r, rows in enumerate(grid):
    for c, char in enumerate(rows):
        if char == "@":
            roll_count = 0
            for d in dirs:
                for d2 in dirs:
                    if 0 <= (r + d) < row_len and 0 <= (c + d2) < col_len:  # valid id?
                        if grid[r + d][c + d2] == "@":
                            roll_count += 1
            if roll_count <= 4:
                res += 1

ic(res)
