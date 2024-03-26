# visualizing the input as 1-D array whose element can be accessed by
# idx = y * width + x


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


def find_valid_neighbours(x, y):

    neighbour_directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
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

# find valid ends
valid_ends = find_valid_neighbours(start_x, start_y)

steps_map = {str(index(start_x, start_y)): 0}
for end in valid_ends:
    x = end[0]
    y = end[1]
    vx = end[2]
    vy = end[3]
    pipe = get(x, y)
    steps = 1
    while pipe != "S":

        idx = str(index(x, y))
        if idx not in steps_map:
            steps_map[idx] = steps

        else:
            steps_map[idx] = min(steps_map[idx], steps)

        rule = pipe_rules[pipe]
        vx, vy = calculate_directions(vx, vy, rule)
        x += vx
        y += vy
        pipe = get(x, y)

        steps += 1

print(max(steps_map.values()))
print(len(steps_map.values()))
