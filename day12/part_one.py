import itertools


def parse_input():
    f = open("input.txt")
    data = f.readlines()
    result = []
    for line in data:
        value = line.strip().split()
        result.append(value)
    return result


def parse_duplicate(val):
    value = val.split(",")
    result = []
    for v in value:
        result.append(int(v))
    return result


def count_springs(records):
    counts = []
    # print("rec", records)
    for key, group in itertools.groupby(records):
        if key == "#":
            counts.append(sum(1 for _ in group))
        # print("group", list(group))

    return counts


def check(records, nums):
    counts = count_springs(records)
    # print("check", counts, nums)
    return nums == counts


def generate_possibilities(records):
    gen = []
    for letter in records:
        if letter == "?":
            gen.append("#.")
        else:
            gen.append(letter)
    # print("generator", len(gen))
    return itertools.product(*gen)


def solver(records, nums):
    candidates = generate_possibilities(records)
    # print((list(candidates)[2]))
    # print(records)
    total_matches = 0
    for candidate in candidates:

        if check(candidate, nums):
            total_matches += 1
    return total_matches


arrangements = parse_input()
counter = 0
for rec in arrangements:
    dulicate = parse_duplicate(rec[1])
    counter += solver(rec[0], dulicate)
print("Result", counter)
