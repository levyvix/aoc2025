from icecream import ic

contents = open(0).read().splitlines()
line_number = len(contents)
col_number = len(contents[0]) - 1
contents, ops = [c for c in contents], contents[-1].split()


def operate(numbers, op):
    n = numbers[0]
    for i in numbers[1:]:
        n = eval(f"{n} {op} {i}")
    return n


op_count = 1
num_list = []
last = False
total = 0
for c in range(col_number, -1, -1):
    num = ""
    for r in range(line_number):
        number = contents[r][c]

        if number in ("+", "-", "*"):
            # this is the last number
            last = True
            break

        num += number
    if num.strip() == "":
        continue
    num_list.append(int(num))
    if last:
        total += operate(num_list, ops[-op_count])
        op_count += 1
        num_list = []
        last = False
ic(total)

