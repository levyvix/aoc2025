from pathlib import Path

from icecream import ic

curr_dir = Path(__file__).parent
r = True

if r:
    file = curr_dir / "real.txt"
else:
    file = curr_dir / "test.txt"

batteries = [line for line in file.read_text().strip().splitlines()]

max_b = 0
for b in batteries:
    ints_b = list(map(int, b))
    tens = max(ints_b[:-1])
    ones = max(ints_b[ints_b.index(tens) + 1 :])
    max_b += tens * 10 + ones


ic(max_b)
