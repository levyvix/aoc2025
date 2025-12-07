from collections import deque
from icecream import ic
from pathlib import Path

file_name = "r.in"
grid = [line for line in (Path(__file__).parent / file_name).read_text().splitlines()]
# find S
sr, sc = 0, 0
for r, rows in enumerate(grid):
    for c, chat in enumerate(rows):
        if grid[r][c] == "S":
            sr, sc = r, c


Q = deque([(sr, sc)])
seen = set()
p = 0


def add(r, c):
    if (r, c) in seen:
        return

    Q.append((r, c))
    seen.add((r, c))


while Q:
    nr, nc = Q.popleft()
    if not (0 <= nr < len(grid) and (0 <= nc < len(grid[0]))):
        continue
    cell = grid[nr][nc]
    if cell in ".S":
        add(nr + 1, nc)
    elif cell == "^":
        p += 1
        if (nr + 1, nc - 1) not in seen:
            add(nr + 1, nc - 1)
        if (nr + 1, nc + 1) not in seen:
            add(nr + 1, nc + 1)
ic(p)
