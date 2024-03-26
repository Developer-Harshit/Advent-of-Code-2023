import json

import helper

offsets = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]


def parse_data(file_path):
    f = open(file_path)
    data = json.load(f)
    return data


def display():
    for j in range(height):
        print(pipe_map[j * width : (j + 1) * width])


def get(x, y):
    return pipe_map[y * width + x]


def set(x, y, val):
    global pipe_map
    idx = y * width + x
    pipe_map = pipe_map[:idx] + val + pipe_map[idx + 1 :]


def not_valid(kx, ky):

    return kx < 0 or ky < 0 or kx > width - 1 or ky > height - 1


def find_neighbours(kx, ky):
    result = []
    for off in offsets:
        nx = kx + off[0]
        ny = ky + off[1]
        if not_valid(kx, ky):
            continue
        result.append([nx, ny])
    return result


new_value = "I"
loop_value = "#"
out_value = "-"


def flood_fill(kx, ky):
    if not_valid(kx, ky):
        return
    pipe = get(kx, ky)
    if pipe == loop_value or pipe == new_value:
        return

    set(kx, ky, new_value)

    open_set = find_neighbours(kx, ky)
    while len(open_set) != 0:

        curr = open_set.pop()
        if not_valid(curr[0], curr[1]):
            continue
        curr_pipe = get(curr[0], curr[1])
        if curr_pipe == loop_value or curr_pipe == new_value:
            continue
        set(curr[0], curr[1], new_value)
        neighbours = find_neighbours(curr[0], curr[1])
        for neighbour in neighbours:
            if neighbour not in open_set:
                open_set.append(neighbour)


data = parse_data("data.json")
height = data["height"]
width = data["width"]
pipe_map = data["map"]
loop = data["loop"]


for i in range(len(loop) - 1):
    x, y = loop[i]
    px, py = loop[i + 1]
    # calculating normal
    ny = x - px
    nx = py - y

    flood_fill(px + nx, py + ny)


# display()
print("result->", pipe_map.count(new_value))
