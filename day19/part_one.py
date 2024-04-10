filename = "input.txt"


def parse_input():
    f = open(filename)
    data = f.readlines()
    i = 0

    workflows = {}
    while i < len(data):
        line = data[i].strip()
        if line == "":
            i += 1
            break
        key, conditions = line.split("{")
        conditions = conditions[:-1].split(",")
        conditions[-1] = "True:" + conditions[-1]
        for k in range(len(conditions)):
            conditions[k] = conditions[k].split(":")
        workflows[key] = conditions
        i += 1
    parts = []
    while i < len(data):
        line = data[i].strip()[1:-1].split(",")

        parts.append("\n".join(line))

        i += 1

    f.close()
    return (workflows, parts)


def execute_condition(key, x, m, a, s):
    if key == "A":
        return True
    elif key == "R":
        return False
    conditions = workflows[key]

    for cnd in conditions:

        k = eval(cnd[0])

        if k:
            return execute_condition(cnd[1], x, m, a, s)


workflows, parts = parse_input()

parts_sum = 0
for p in parts:
    exec(p)

    if execute_condition("in", x, m, a, s):
        parts_sum += x + m + a + s
print("Result", parts_sum)
