from icecream import ic

content = open(0).read()
tiles = [list(map(int, line.split(","))) for line in content.splitlines()]

ans = 0
for i, (x1, y1) in enumerate(tiles):
    for j, (x2, y2) in enumerate(tiles):
        if i < j:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            ans = max(ans, area)
ic(ans)

