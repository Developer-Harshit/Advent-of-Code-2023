from collections import deque


directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
filename = "input.txt"


def parse_input():
    lookup = {"0": "R", "1": "D", "2": "L", "3": "U"}
    with open(filename) as f:

        data = f.readlines()
        result = []
        for d in data:
            hexColor = d.strip().split("#")[1]

            mydir = lookup[hexColor[-2]]
            mydist = int(hexColor[:5], 16)

            result.append((mydir, mydist))
        return result


def det(v1, v2):
    return v1[0] + v2[1] - v1[1] - v2[0]


input_data = parse_input()

# finding vertices coords
vertices = [(0, 0)]
vert_count = 0
for i in range(len(input_data)):
    vel, dist = input_data[i]
    vert_count += dist
    px, py = vertices[i]
    vx, vy = directions[vel]
    vertices.append((px + vx * dist, py + vy * dist))


# A function to find area by  the Shoelace algorithm
def areaInside(vertices):
    n = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0, n - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]

    area = abs(sum1 - sum2) / 2
    return area


# find area using picks theorem
def picksArea(B, I):

    return B / 2 + I - 1


print("area", picksArea(vert_count, areaInside(vertices) + 2))
