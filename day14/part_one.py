filename = "input.txt"


def parse_input():
    f = open(filename)
    data = f.readlines()
    return [list(line.strip()) for line in data]


def get_round_rock(pos_map):
    rocks = {}
    for i in range(len(pos_map[0])):
        rocks[str(i)] = []
        for j in range(len(pos_map) - 1, -1, -1):
            if pos_map[j][i] == "O":
                rocks[str(i)].append((i, j))
    return rocks


def roll_rock(x, y, pos_map):

    for j in range(y - 1, -1, -1):
        val = pos_map[j][x].strip()

        if val != ".":
            pos_map[y][x] = "."
            pos_map[j + 1][x] = "O"
            break

        elif j == 0:
            pos_map[y][x] = "."
            pos_map[0][x] = "O"
            break


def display(pos_map):
    for k in pos_map:
        print(*k)


input_data = parse_input()
rocks_data = get_round_rock(input_data)
for key in rocks_data:
    rocks = rocks_data[key]
    while len(rocks) > 0:
        rock_pos = rocks.pop()
        roll_rock(rock_pos[0], rock_pos[1], input_data)

# Counting weight of rocks row wise
total_load = 0
for j in range(len(input_data)):
    factor = len(input_data) - j
    total_load += factor * input_data[j].count("O")
print("Total load", total_load)
