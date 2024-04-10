"""
1. find index of Start
2. find path of loop 
3. flood fill along normals
"""

filename = "input.txt"


def parse_input():
    f = open(filename)
    data = f.readlines()
    return [list(line.strip()) for line in data]


def find_start():
    for j in range(len(pipeMap)):
        if "S" in pipeMap[j]:
            return (pipeMap[j].index("S"), j)


offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def within_bounds(x, y):
    return x < width and y < height and x >= 0 and y >= 0


def find_neighbours(x, y):
    result = []

    for off in offsets:
        n = [off[0] + x, off[1] + y]
        if within_bounds(n[0], n[1]):
            result.append(n)
    return result


def flood_fill(idx, bound="#", curr="+"):

    open_set = [idx]

    while open_set:

        i, j = open_set.pop()

        if not within_bounds(i, j):
            continue
        if pipeMap[j][i] not in (bound, curr):
            pipeMap[j][i] = curr
            open_set.extend(find_neighbours(i, j))


def can_go(dir_x, dir_y, rule):
    if rule[2]:
        return dir_x == -rule[0] or dir_y == -rule[1]
    else:
        return abs(dir_x) == rule[0] and abs(dir_y) == rule[1]


def find_valid_neighbours(x, y):

    neighbour_directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    valid = []
    for direction in neighbour_directions:
        nx = x + direction[0]
        ny = y + direction[1]
        if not within_bounds(nx, ny):
            continue

        rule = pipe_rules[pipeMap[ny][nx]]
        if not rule:
            continue

        if can_go(direction[0], direction[1], rule):
            valid.append([nx, ny, *direction])
    return valid


def calculate_directions(dir_x, dir_y, rule):
    if rule[2]:
        return (dir_x + rule[0], dir_y + rule[1])
    else:
        return (dir_x, dir_y)


def display():
    for j in pipeMap:
        print(*j)


def copy():
    res = []
    for j in origianlMap:
        res.append([*j])
    return res


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

origianlMap = parse_input()
pipeMap = parse_input()
width = len(pipeMap[0])
height = len(pipeMap)
start = find_start()

valid_ends = find_valid_neighbours(start[0], start[1])

display()

for end in valid_ends:
    x, y, vx, vy = end

    myPath = [(vx, vy)]
    pipe = origianlMap[y][x]

    while not (x == start[0] and y == start[1]):

        rule = pipe_rules[pipe]
        vx, vy = calculate_directions(vx, vy, rule)
        pipeMap[y][x] = "#"
        x += vx
        y += vy

        pipe = origianlMap[y][x]
        myPath.append((vx, vy))
    pipeMap[start[1]][start[0]] = "#"
    curr = [*start]

    for i in range(len(myPath)):

        dx, dy = myPath[i % len(myPath)]
        x, y = curr

        normal = [-dy + x, dx + y]
        # print(f"normal of {(x,y)} is {normal} in dir of {(dx,dy)}")
        flood_fill(normal)

        curr[0] += dx
        curr[1] += dy
    counter = 0
    for j in pipeMap:
        counter += j.count("+")
    # display()
    print("Inside count", counter)

    pipeMap = parse_input()
