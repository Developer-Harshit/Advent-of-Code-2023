def parse_input(file_path):
    f = open(file_path)
    data = f.readlines()
    f.close()

    for i in range(len(data)):
        data[i] = list(data[i].strip())

    return data


def expand_galaxies(image, galaxies, amount):
    amount = amount - 1

    # expanding im x direction
    i = len(image[0]) - 1

    while i > -1:

        j = 0
        has_galaxy = False
        while j < len(image):
            if image[j][i] == "#":
                has_galaxy = True

                break
            j += 1
        if not has_galaxy:
            for key in galaxies:
                pos = galaxies[key]
                if pos[0] > i:
                    pos[0] = pos[0] + amount

        i -= 1

    j = len(image) - 1
    # expanding in y direction
    while j > -1:
        line = image[j]
        if "#" not in line:
            for key in galaxies:
                pos = galaxies[key]
                if pos[1] > j:
                    pos[1] = pos[1] + amount

        j -= 1


def find_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


image_map = parse_input("input.txt")

# numbering galaxies
galaxies = {}
idx = 0

for j in range(len(image_map)):
    for i in range(len(image_map[0])):
        if image_map[j][i] == "#":
            galaxies[str(idx)] = [i, j]
            idx += 1

expand_amount = 1000000
expand_galaxies(image_map, galaxies, expand_amount)
count = 0

g_keys = list(galaxies.keys())
distance_sum = 0
for i in range(len(g_keys)):
    pos1 = galaxies[g_keys[i]]
    for j in range(i + 1, len(g_keys)):
        pos2 = galaxies[g_keys[j]]
        distance_sum += find_distance(pos1, pos2)

        count += 1


print("result->", distance_sum)
