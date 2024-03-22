def parse_input(file_path):
    f = open(file_path, "r")
    data = f.readlines()
    part_data = []
    for line in data:
        line = line.strip()
        line_data = []
        for word in line:
            line_data.append(word)

        part_data.append(line_data)

    return part_data


# if off[0]+ i > maxi or off[1] + j > maxj:


offsets = [
    [-1, +0],
    [+1, +0],
    [+0, -1],
    [+0, +1],
    [-1, -1],
    [+1, +1],
    [+1, -1],
    [-1, +1],
]
input_data = parse_input("input.txt")
# y
row_count = len(input_data)
# x
col_count = len(input_data[0])


def find_part_from_range(gear_range):
    j = gear_range[0]
    part_number = ""
    for i in range(gear_range[1], gear_range[2] + 1):
        part_number += input_data[j][i]
    return int(part_number)


def find_part_range(x, y):
    part_range = [y]
    for i in range(x - 1, -1, -1):
        if not input_data[y][i].isnumeric():
            part_range.append(i + 1)
            break
        elif i == 0:
            part_range.append(i)
            break

    for i in range(x + 1, col_count):
        if not input_data[y][i].isnumeric():
            part_range.append(i - 1)
            break
        elif i == col_count - 1:
            part_range.append(i)
            break

    return part_range


# print(input_data[122][87])
# pr = find_part_range(87, 122)
# print(find_part_from_range(pr))


def find_gear_ratio(x, y):
    parts_range = []

    for off in offsets:
        i = x + off[0]
        j = y + off[1]
        letter = input_data[j][i]

        if not letter.isnumeric():
            continue
        p_range = find_part_range(i, j)
        print(p_range, letter)

        if p_range not in parts_range:
            parts_range.append(p_range)

            if len(parts_range) > 2:
                return 0

    if len(parts_range) != 2:

        return 0

    gear_ratio = 1
    for p_range in parts_range:

        gear_ratio *= find_part_from_range(p_range)
    return gear_ratio


gear_ratio_sum = 0
for j in range(row_count):
    for i in range(col_count):
        if input_data[j][i] == "*":
            gear_ratio_sum += find_gear_ratio(i, j)
print(gear_ratio_sum)
