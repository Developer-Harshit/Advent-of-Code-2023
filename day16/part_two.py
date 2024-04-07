filename = "input.txt"


def parse_input():
    with open(filename) as f:
        data = f.readlines()
        return [line.strip() for line in data]


def is_empty(rule, dx, dy):
    return rule == "." or (rule == "|" and dx == 0) or (rule == "-" and dy == 0)


def not_valid(x, y):
    return x < 0 or y < 0 or x >= len(layout_map[0]) or y >= len(layout_map)


mirror_rule = {"/": -1, "\\": +1}
layout_map = parse_input()
width = len(layout_map[0])
height = len(layout_map)


tile_left = 110 * 4


def find_count(a, b, da, db):

    open_set = [(a, b, da, db)]
    closed_set = [(a, b, da, db)]
    while len(open_set) > 0:

        x, y, dx, dy = open_set.pop()

        # if not within bounds
        if not_valid(x, y):
            continue
        elif (x, y, dx, dy) not in closed_set:
            closed_set.append((x, y, dx, dy))

        # get instructionm
        instruction = layout_map[y][x]
        # if empty space or empty splitter
        if is_empty(instruction, dx, dy):
            x += dx
            y += dy
            ele = (x, y, dx, dy)

            if ele not in closed_set:
                open_set.append(ele)

        elif instruction in mirror_rule:
            sign = mirror_rule[instruction]
            dx, dy = sign * dy, sign * dx
            x += dx
            y += dy
            ele = (x, y, dx, dy)
            if ele not in closed_set:
                open_set.append(ele)
        else:
            for sign in [-1, 1]:
                x1, y1, dx1, dy1 = x, y, dx, dy
                dx1, dy1 = sign * dy1, sign * dx1
                x1 += dx1
                y1 += dy1
                ele = (x1, y1, dx1, dy1)
                if ele not in closed_set:
                    open_set.append(ele)
    final_set = []
    for pos in closed_set:
        ele = (pos[0], pos[1])
        if ele not in final_set:
            final_set.append(ele)

    global tile_left
    print("Current count =", len(final_set), "and", tile_left, "tiles left")
    tile_left -= 1
    return len(final_set)


max_count = 0
for y in range(0, height):
    # top left to down moving right
    max_count = max(find_count(0, y, 1, 0), max_count)

    # top right to down  moving left
    max_count = max(find_count(width - 1, y, -1, 0), max_count)


for x in range(0, width):
    # down left to right moving up
    max_count = max(find_count(x, height - 1, 0, -1), max_count)

    # top left to right moving down
    max_count = max(find_count(x, 0, 0, 1), max_count)
print("MAx-count=", max_count)
