from icecream import ic


def main():
    with open("r1.txt") as f:
        lines = f.readlines()
    nzero = 0
    curr = 50
    for line in lines:
        direction, times = line[0], line[1:]
        if direction == "L":
            curr = (curr - int(times)) % 100
        else:
            curr = (curr + int(times)) % 100
        if curr == 0:
            nzero += 1
    ic(nzero)


if __name__ == "__main__":
    main()
