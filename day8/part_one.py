def parse_data(data):
    table_data = {}

    for line in data:
        line = line.strip()
        if line == "":
            continue
        line = line.split("=")
        key = line[0].strip()

        values = line[1].replace(" ", "").strip("(").strip(")").split(",")
        table_data[key] = values

    return table_data


file_path = "input.txt"
f = open(file_path)


direction_map = {"R": 1, "L": 0}
instructions = f.readline().strip()
network_table = parse_data(f.readlines())
f.close()


current = "AAA"
idx = 0
count = 0
print("starting")

while current != "ZZZ":
    direction = direction_map[instructions[idx]]
    current = network_table[current][direction]
    # print(direction, current)
    count += 1
    idx = (idx + 1) % len(instructions)

print("ended")
print("no. of steps", count)
