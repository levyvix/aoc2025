from pathlib import Path

file_name = "test.txt"
contents = (Path(__file__).parent / file_name).read_text().splitlines()

for b in contents:
    bcp = b[:]
    jolt = []
    for i in range(12):
        max_ = -1
        remaining_batteries = bcp[: -(12 - len(jolt))] if len(bcp) < 11 else bcp
        for n in remaining_batteries:
            n = int(n)
            max_ = max(max_, n)
        jolt.append(str(max_))
        index_max = bcp.index(str(max_))
        bcp = bcp[index_max + 1 :]
