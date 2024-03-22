file_path = "input.txt"


def parse_data(idx, data):
    my_data = data[idx].strip().split(":")[1].strip().split()
    num = ""
    for d in my_data:
        num += str(d)
    return int(num)


def calculate_dist(hold_time, total_time):
    return (total_time - hold_time) * hold_time


f = open(file_path)
data = f.readlines()
time = parse_data(0, data)
dist = parse_data(1, data)


result = 1
left = int(time / 2)
right = left + 1

win_count = 0
# looping middle to left

for j in range(left, -1, -1):
    dist_travelled = calculate_dist(j, time)

    if dist_travelled > dist:
        win_count += 1
    else:
        break

# lopping middle+1 to right

for j in range(right, time + 1):
    dist_travelled = calculate_dist(j, time)

    if dist_travelled > dist:
        win_count += 1
    else:
        break

result *= win_count
print(result)
