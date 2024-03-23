def find_lcm(nums):
    result = [*nums]
    while len(result) > 1:
        n = lcm_of_two(result.pop(), result.pop())
        result.append(n)
    return result[0]


def lcm_of_two(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num2, num1 * num2 + 1, num2):
        if x % num1 == 0:
            return x


def parse_data(data):
    table_data = {}

    start_keys = []

    for line in data:
        line = line.strip()
        if line == "":
            continue
        line = line.split("=")
        key = line[0].strip()
        if key[2] == "A":
            start_keys.append(key)

        values = line[1].replace(" ", "").strip("(").strip(")").split(",")
        table_data[key] = values

    return table_data, start_keys


file_path = "input.txt"
f = open(file_path)


direction_map = {"R": 1, "L": 0}
instructions = f.readline().strip()
network_table, current_keys = parse_data(f.readlines())

step_counts = []


f.close()
print("starting")
for i in range(len(current_keys)):
    idx = 0
    steps = 0
    current = current_keys[i]
    while not current[2] == "Z":
        direction = direction_map[instructions[idx]]
        current = network_table[current][direction]
        idx = (idx + 1) % len(instructions)
        steps += 1
    step_counts.append(steps)


print("ended")


print("no. of steps", step_counts)
result = find_lcm(step_counts)
print(result)
