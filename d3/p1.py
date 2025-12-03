from icecream import ic
from pathlib import Path

curr_dir = Path(__file__).parent
r = True

if r:
    file = curr_dir / "real.txt"
else:
    file = curr_dir / "test.txt"

batteries = [line for line in file.read_text().strip().split("\n")]

max_b = []
for b in batteries:
    curr_max = -1
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            combined_number = "".join([b[i], b[j]])

            curr_max = max(curr_max, int(combined_number))

    max_b.append(curr_max)
ic(sum(max_b))
