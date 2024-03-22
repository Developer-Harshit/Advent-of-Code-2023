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
# if off[0]+ i > maxi or off[1] + j > maxj:


input_data = parse_input("input.txt")
row_count = len(input_data)
col_count = len(input_data[0])
part_sum = 0


def check_valid(i, j):

    for off in offsets:
        x = off[0] + i
        y = off[1] + j
        if x > col_count - 1 or y > row_count - 1:
            continue
        if not input_data[y][x].isnumeric():
            if not input_data[y][x] == ".":
                return True
    return False


for j in range(row_count):
    part_number = ""
    is_valid = False
    for i in range(col_count):
        letter = input_data[j][i]
        if letter.isnumeric():
            part_number += letter
            if not is_valid:
                is_valid = check_valid(i, j)

        if part_number != "" and (not letter.isnumeric() or i == col_count - 1):

            if is_valid:

                part_sum += int(part_number)

            part_number = ""
            is_valid = False
print(part_sum)
