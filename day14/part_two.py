filename = "input.txt"


def parse_input():
    f = open(filename)
    data = f.readlines()
    return [list(line.strip()) for line in data]


def get_round_rock(pos_map):
    rocks = []
    for i in range(len(pos_map[0])):
        for j in range(len(pos_map) - 1, -1, -1):
            if pos_map[j][i] == "O":
                rocks.append([i, j])
    return rocks


def roll_north(pos, pos_map):
    x = pos[0]
    y = pos[1]

    for j in range(y - 1, -1, -1):
        val = pos_map[j][x].strip()

        if val != ".":
            pos_map[y][x] = "."
            pos_map[j + 1][x] = "O"
            y = j + 1
            break

        elif j == 0:
            pos_map[y][x] = "."
            pos_map[0][x] = "O"
            y = 0

            break

    pos[1] = y


def roll_west(pos, pos_map):
    x = pos[0]
    y = pos[1]

    for i in range(x - 1, -1, -1):
        val = pos_map[y][i].strip()

        if val != ".":
            pos_map[y][x] = "."
            pos_map[y][i + 1] = "O"
            x = i + 1

            break

        elif i == 0:
            pos_map[y][x] = "."
            pos_map[y][0] = "O"
            x = 0

            break
    pos[0] = x


def roll_south(pos, pos_map):
    x = pos[0]
    y = pos[1]

    for j in range(y + 1, len(pos_map)):
        val = pos_map[j][x].strip()

        if val != ".":
            pos_map[y][x] = "."
            pos_map[j - 1][x] = "O"
            y = j - 1
            break

        elif j == len(pos_map) - 1:
            pos_map[y][x] = "."
            pos_map[j][x] = "O"
            y = j
            break

    pos[1] = y


def roll_east(pos, pos_map):
    x = pos[0]
    y = pos[1]

    for i in range(x + 1, len(pos_map[0])):
        val = pos_map[y][i].strip()

        if val != ".":
            pos_map[y][x] = "."
            pos_map[y][i - 1] = "O"
            x = i - 1
            break

        elif i == len(pos_map[0]) - 1:

            pos_map[y][x] = "."
            pos_map[y][i] = "O"
            x = i
            break

    pos[0] = x


def sort_x(ele):
    return ele[0]


def sort_y(ele):
    return ele[1]


def display(msg=""):
    print(msg)
    for k in input_data:
        print(*k)


def map_to_str(pos_map):
    mystr = ""
    for j in pos_map:
        for i in j:

            mystr += i.strip()

    return mystr


def find_total_load(pos_map):
    total_load = 0
    for j in range(len(pos_map)):
        factor = len(pos_map) - j
        total_load += factor * pos_map[j].count("O")
    return total_load


input_data = parse_input()
rocks_data = get_round_rock(input_data)
initial_map = map_to_str(input_data)
cache_maps = [map_to_str(input_data)]
cache_loads = []
loop_start = None
loop_end = None

loop_count = 1000000000
for k in range(loop_count):

    # north
    rocks_data.sort(key=sort_y)
    for p in rocks_data:
        roll_north(p, input_data)

    # West
    rocks_data.sort(key=sort_x)
    for p in rocks_data:
        roll_west(p, input_data)

    # south
    rocks_data.sort(key=sort_y, reverse=True)
    for p in rocks_data:
        roll_south(p, input_data)

    # east
    rocks_data.sort(key=sort_x, reverse=True)
    for p in rocks_data:
        roll_east(p, input_data)

    # display(str(k + 1) + "th Rotation")
    curr_map = map_to_str(input_data)
    if curr_map in cache_maps:
        loop_start = cache_maps.index(curr_map)

        loop_end = k

        break
    else:
        cache_maps.append(curr_map)
        cache_loads.append(find_total_load(input_data))

# idk how to find the idx of result
####################################
