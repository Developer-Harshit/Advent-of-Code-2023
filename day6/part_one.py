file_path = "input.txt"


def parse_data(idx, data):
    my_data = data[idx].strip().split(":")[1].strip().split()
    for i in range(len(my_data)):
        my_data[i] = int(my_data[i])
    return my_data


def calculate_dist(hold_time, total_time):
    return (total_time - hold_time) * hold_time


f = open(file_path)
data = f.readlines()
time_data = parse_data(0, data)
dist_data = parse_data(1, data)

# looping by time and dist list - length of either will work
result = 1
for i in range(len(time_data)):
    time = time_data[i]
    dist = dist_data[i]
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
