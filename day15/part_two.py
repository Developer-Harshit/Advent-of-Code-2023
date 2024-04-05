multiplier = 17
dividor = 256
filename = "input.txt"


def hash(mystr):
    curr_value = 0
    for k in mystr:
        code = ord(k)
        curr_value += code
        curr_value *= multiplier
        curr_value = curr_value % dividor
    return str(curr_value)


def parse_input():
    f = open(filename)
    data = f.readline()
    f.close()
    return data.split(",")


def remove_label(arr, slabel):
    new_arr = []
    for ele in arr:
        if ele[0] == slabel:
            continue
        new_arr.append(ele)

    return new_arr


def find_label(arr, slabel):
    idx = -1
    for i in range(len(arr)):
        if arr[i][0] == slabel:
            idx = i
            break

    return idx


input_data = parse_input()
hash_map = {}
for i in range(256):
    hash_map[str(i)] = []
for v in input_data:
    if "=" in v:
        label, focal_length = v.split("=")
        hash_value = hash(label)
        idx = find_label(hash_map[hash_value], label)
        if idx < 0:
            hash_map[hash_value].append([label, focal_length])
        else:
            hash_map[hash_value][idx][1] = focal_length
    else:
        label = v[:-1]
        hash_value = hash(label)

        hash_map[hash_value] = remove_label(hash_map[hash_value], label)

power_sum = 0
for k in hash_map:
    labels = hash_map[k]
    for i in range(len(labels)):
        focal_length = labels[i][1]
        power_sum += (int(k) + 1) * (i + 1) * int(focal_length)
    if labels:
        print(f"Box {k}", *labels)
print("Sum of Focusing Power->", power_sum)
