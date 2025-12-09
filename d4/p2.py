from icecream import ic

grid = [list(line.strip()) for line in open(0).read().splitlines()]
row_len = len(grid)
col_len = len(grid[0])

dirs = [-1, 0, 1]
res = 0
while True:
    changed = False
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@":
                roll_count = 0
                for d in dirs:
                    for d2 in dirs:
                        if (
                            0 <= (r + d) < row_len and 0 <= (c + d2) < col_len
                        ):  # valid id?
                            if grid[r + d][c + d2] == "@":
                                roll_count += 1
                if roll_count <= 4:
                    res += 1
                    grid[r][c] = "."
                    changed = True
    if not changed:
        break

ic(res)
