from functools import cache
from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

grid = [line for line in open(0).read().splitlines()]
# find S
S = (0, 0)
for r, rows in enumerate(grid):
    for c, chat in enumerate(rows):
        if grid[r][c] == "S":
            S = r, c


@cache
def solve(r, c):
    if r >= len(grid):
        return 1
    cell = grid[r][c]
    if cell in ".S":
        return solve(r + 1, c)
    elif cell == "^":
        return solve(r, c - 1) + solve(r, c + 1)


ic(solve(*S))
