"""
# Rules

if s == '.' 
    continue 

if s in splitter 
    if check( splitter[s] ,dir)
        continue
    else 
        split()
        
if s in mirror
    sign = mirror[s]
    dir = rotate(dir,sign)    
"""

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
closed_set = [(0, 0, 1, 0)]
open_set = [(0, 0, 1, 0)]
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

result = []
for k in closed_set:
    ele = (k[0], k[1])
    if ele not in result:
        result.append(ele)
print("energized Tile Count->", len(result))
