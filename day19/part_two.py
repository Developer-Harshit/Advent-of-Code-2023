from helper import *

filename = "input.txt"


def parse_input():
    f = open(filename)
    data = f.readlines()
    i = 0

    workflows = {}
    while i < len(data):
        line = data[i].strip()
        if line == "":
            break
        key, conditions = line.split("{")

        conditions = conditions[:-1].split(",")

        workflows[key] = ([], conditions.pop())
        for k in range(len(conditions)):
            ele, res = conditions[k].split(":")
            name, operator, num = ele[0], ele[1], int(ele[2:])

            workflows[key][0].append((name, operator, num, res))
            # conditions[k] = conditions[k].split(":")

        i += 1
    f.close()
    return workflows


minNum = 1
maxNum = 4000


def count_ranges(ranges, dest="in"):
    if dest == "R":
        return 0
    if dest == "A":
        result = 1
        for key in "xmas":
            start, stop = ranges[key]
            result *= stop - start + 1
        return result
    conditions, fallback = workflows[dest]
    total_count = 0
    for name, op, num, res in conditions:
        start, stop = ranges[name]
        if op == "<":
            ori_part = (start, min(num - 1, stop))
            not_part = (max(num, start), stop)

        else:
            ori_part = (max(num + 1, start), stop)
            not_part = (start, min(num, stop))
        if ori_part[0] <= ori_part[1]:
            newRange = dict(ranges)
            newRange[name] = ori_part
            total_count += count_ranges(newRange, res)

        if not_part[0] <= not_part[1]:
            ranges = dict(ranges)
            ranges[name] = not_part
        else:
            break
    else:
        total_count += count_ranges(ranges, fallback)
    return total_count


workflows = parse_input()
myRange = {key: (1, 4000) for key in "xmas"}
k = count_ranges(myRange, "in")
print(k)
