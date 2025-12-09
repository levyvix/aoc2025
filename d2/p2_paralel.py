from icecream import ic
from pathos.multiprocessing import ProcessPool

content = open(0).read()
ranges = (r.split("-") for r in content.strip().split(","))


def check_palindromes(id: int):
    id_string = str(id)
    n = len(id_string)
    if n <= 1:
        return 0
    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len == 0 and id_string == id_string[:pattern_len] * (
            n // pattern_len
        ):
            return int(id_string)
    return 0


def ids_in_range(start_end):
    s, e = start_end
    return range(int(s), int(e) + 1)


def main():
    with ProcessPool() as pool:
        results = pool.uimap(
            check_palindromes,
            (i for r in ranges for i in ids_in_range(r)),
            chunksize=100000,
        )
    ic(sum(results))


if __name__ == "__main__":
    main()
