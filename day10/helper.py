def can_go(dir_x, dir_y, rule):
    if rule[2]:
        return dir_x == -rule[0] or dir_y == -rule[1]
    else:
        return abs(dir_x) == rule[0] and abs(dir_y) == rule[1]


def calculate_directions(dir_x, dir_y, rule):
    if rule[2]:
        return (dir_x + rule[0], dir_y + rule[1])
    else:
        return (dir_x, dir_y)


def index(x, y):
    return y * width + x


def get(x, y):
    return pipe_map[y * width + x]


def set(x, y, val):
    global pipe_map
    idx = index(x, y)
    pipe_map = pipe_map[:idx] + val + pipe_map[idx + 1 :]


def display():
    for j in range(height):
        print(pipe_map[j * width : (j + 1) * width])


def find_valid_neighbours(x, y):

    valid = []
    for direction in neighbour_directions:

        n_x = x + direction[0]
        n_y = y + direction[1]
        if n_x < 0 or n_y < 0 or n_x > width - 1 or n_y > height - 1:
            continue

        rule = pipe_rules[get(n_x, n_y)]
        if not rule:
            continue

        if can_go(direction[0], direction[1], rule):
            valid.append([n_x, n_y, *direction])
    return valid


file_path = "input.txt"
f = open(file_path)
data = f.readlines()

f.close()

pipe_rules = {
    "|": (0, 1, False),
    "-": (1, 0, False),
    "L": (1, -1, True),
    "J": (-1, -1, True),
    "7": (-1, 1, True),
    "F": (1, 1, True),
    "S": False,
    ".": False,
}
neighbour_directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]
# stuffs
height = len(data)
width = len(data[0].strip())
pipe_map = ""
start_x = None
start_y = None
for y in range(len(data)):
    line = data[y].strip()
    pipe_map += line
    if "S" in line:
        start_x = line.index("S")
        start_y = y
x, y, vx, vy = find_valid_neighbours(start_x, start_y)[0]
pipe = get(x, y)
walk_path = [(start_x, start_y)]
while pipe != "S":
    walk_path.append([x, y])
    rule = pipe_rules[pipe]
    vx, vy = calculate_directions(vx, vy, rule)
    set(x, y, "#")
    x += vx
    y += vy
    pipe = get(x, y)
walk_path.append([start_x, start_y])
set(start_x, start_y, "#")
for j in range(height):
    for i in range(width):
        if get(i, j) == "#":
            continue
        else:
            set(i, j, "-")

import json

f = open("data.json", "w")
data = {"map": pipe_map, "height": height, "width": width, "loop": walk_path}
json.dump(data, f)
f.close()
