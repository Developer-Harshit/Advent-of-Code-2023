f = open("input.txt", "r")

# parsing seed data
seed_list = f.readline().strip().split(":")[1].strip().split(" ")


# parsing map sdata
data = f.readlines()
almanac_maps = []

m_count = 0
for line in data:
    line = line.strip()
    if ":" in line:
        almanac_maps.append([])
        continue
    if len(line) > 2:
        map_range = line.split(" ")
        if len(map_range) == 3:
            m_count += 1
            map_range[0] = int(map_range[0])
            map_range[1] = int(map_range[1])
            map_range[2] = int(map_range[2])
            almanac_maps[-1].append(map_range)


# [
#     [[dest, src, range]],
#     [[dest, src, range]],
# ]
def find_mapped_value(value, map_ranges):
    # [
    #     [dest, src, range],
    # ]
    for map_range in map_ranges:
        target = map_range[0]
        src = map_range[1]
        r = map_range[2]
        if value < src or value > src + r:
            continue
        return target + (value - src)
    return value


location_list = []

for seed in seed_list:
    seed_location = int(seed)
    for almanac_map in almanac_maps:
        seed_location = find_mapped_value(seed_location, almanac_map)
    location_list.append(seed_location)

print(min(location_list))
