from pathlib import Path
from icecream import ic


def main():
    lines = open(0).readlines()

    nzero = 0
    curr = 50
    for line in lines:
        direction, times = line[0], int(line[1:])
        for _ in range(times):
            curr += -1 if direction == "L" else 1
            curr = curr % 100
            if curr == 0:
                nzero += 1
    ic(nzero)


if __name__ == "__main__":
    main()
