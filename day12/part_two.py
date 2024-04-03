import itertools


def parse_input():
    f = open("input.txt")
    data = f.readlines()
    result = []
    for line in data:

        value = line.strip().split()

        result.append(value)
    return result


def repeat_values(value, delimeter="?"):
    value = (value + delimeter) * 5
    return value[:-1]


def parse_duplicate(val):
    val = repeat_values(val, ",")
    val = val.split(",")
    result = []
    for v in val:
        result.append(int(v))
    return result


def count_springs(records):
    counts = []
    for key, group in itertools.groupby(records):
        if key == "#":
            counts.append(sum(1 for _ in group))
    return counts


def check(records, nums):
    if records.count("#") != sum(nums):
        return False
    counts = count_springs(records)
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
    print(records, nums)
    total_matches = 0
    for candidate in candidates:

        if check(candidate, nums):
            total_matches += 1
    return total_matches


arrangements = parse_input()
counter = 0
for rec in arrangements:
    original = repeat_values(rec[0])
    dulicate = parse_duplicate(rec[1])
    sol = solver(original, dulicate)
    counter += sol
    print(sol)
print("Result", counter)
