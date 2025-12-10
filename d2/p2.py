from icecream import ic
import sys

ic.configureOutput(outputFunction=lambda s: print(s, file=sys.stderr))

content = open(0).read()
ranges = content.split(",")


def check_palindromes(id: str):
    if len(id) <= 1:
        return False
    n = len(id)
    for pattern_len in range(1, n // 2 + 1):
        if n % pattern_len == 0:
            pattern = id[:pattern_len]
            if pattern * (n // pattern_len) == id:
                return True
    return False


invalidIds = 0
for r in ranges:
    init, end = r.split("-")
    for id in range(int(init), int(end) + 1):
        # check palindrome
        if check_palindromes(str(id)):
            invalidIds += id
ic(invalidIds)
