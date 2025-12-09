from icecream import ic

content = open(0).read()

ranges = content.split(",")

invalidIds = 0
for r in ranges:
    init, end = r.split("-")
    for id in range(int(init), int(end) + 1):
        # check palindrome
        idString = str(id)
        if len(idString) > 1 and len(idString) % 2 == 0:
            mid = len(idString) // 2
            first_part, sec_part = idString[:mid], idString[mid:]
            if first_part == sec_part:
                invalidIds += id
ic(invalidIds)
