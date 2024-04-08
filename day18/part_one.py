from collections import deque


directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
filename = "input.txt"
dig_plan = deque([deque(["#"])])
dig_path = []
width, height = 1, 1
idx = [0, 0]


def parse_input():

    with open(filename) as f:

        data = f.readlines()
        result = []
        for d in data:
            d = d.strip().split()
            result.append((d[0], int(d[1])))
        return result


def count(v="#"):
    counter = 0
    for k in dig_plan:
        counter += k.count(v)
    return counter


def dig(m1, m2, sign):
    if m1[1] == m1[1]:

        j = m1[1]
        for i in range(m1[0], m2[0] + 1):
            dig_plan[j][i] = "#"

    if m1[0] == m1[0]:

        i = m1[0]
        for j in range(m1[1], m2[1] + 1):

            dig_plan[j][i] = "#"


def display():
    print("-" * width)

    for j in dig_plan:
        for i in j:
            print(i, end=" ")
        print()


# Digging boundary
input_data = parse_input()
for d in input_data:
    prev = [idx[0], idx[1]]
    dig_dir = directions[d[0]]
    dig_path.extend([dig_dir] * d[1])
    idx[0] += dig_dir[0] * d[1]
    idx[1] += dig_dir[1] * d[1]

    if d[0] == "L" and idx[0] < 0:
        dX = abs(idx[0])
        for j in range(height):
            dig_plan[j].extendleft(["."] * dX)
        idx[0] = 0
        prev[0] += dX

    if d[0] == "R" and idx[0] >= width:
        dX = (idx[0] + 1) - width
        for j in range(height):
            dig_plan[j].extend(["."] * dX)

    if d[0] == "U" and idx[1] < 0:
        dY = abs(idx[1])
        for _ in range(dY):
            dig_plan.extendleft([deque(["."] * (width))])
        idx[1] = 0
        prev[1] += dY

    if d[0] == "D" and idx[1] >= height:
        dY = (idx[1] + 1) - height
        for _ in range(dY):
            dig_plan.extend([deque(["."] * (width))])

    width = len(dig_plan[0])
    height = len(dig_plan)

    if prev[0] > idx[0] or prev[1] > idx[1]:
        dig(idx, prev, -1)
    else:
        dig(prev, idx, 1)

display()


# filling boundary and stuff
offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
print("Boundary=", count())


def find_neighbours(x, y):
    result = []
    for off in offsets:
        n = [off[0] + x, off[1] + y]
        if n[0] < width and n[1] < height and n[0] >= 0 and n[1] >= 0:
            result.append(n)
    return result


def flood_fill(idx, old=".", curr="+"):

    open_set = [idx]

    while open_set:
        i, j = open_set.pop()
        if dig_plan[j][i] == old:
            dig_plan[j][i] = curr
            open_set.extend(find_neighbours(i, j))


curr = [idx[0], idx[1]]
for i in range(len(dig_path)):
    dx, dy = dig_path[i]
    x, y = curr
    normal = (-dy + x, dx + y)

    flood_fill(normal)

    curr[0] += dx
    curr[1] += dy
display()
print("Result=", count("#") + count("+"))
