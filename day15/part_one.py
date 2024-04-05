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
    return curr_value


def parse_input():
    f = open(filename)
    data = f.readline()
    f.close()
    return data.split(",")


input_data = parse_input()
hash_sum = sum(hash(goo) for goo in input_data)
print("result", hash_sum)
