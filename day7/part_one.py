# this is rather a sorting problem
strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def calculate_card_count(hand):
    hand_set = set(hand)
    card_count = []
    for ele in hand_set:
        card_count.append(hand.count(ele))
    return card_count


# 0
def check_five_kind(card_count):
    return len(card_count) == 1


# 1
def check_four_kind(card_count):
    return max(card_count) == 4


# 2
def check_full_house(card_count):
    return len(card_count) == 2 and max(card_count) == 3


# 3
def check_three_kind(card_count):
    return len(card_count) == 3 and max(card_count) == 3


# 4
def check_two_pair(card_count):
    return len(card_count) == 3 and card_count.count(2) == 2


# 5
def check_one_pair(card_count):
    return len(card_count) == 4


# 6
def check_high_card(card_count):
    return len(card_count) == 5


def parse_input(file_path):
    f = open(file_path)
    data = f.readlines()
    f.close()
    input_data = []
    for line in data:
        input_data.append(line.strip().split())
    return input_data


input_data = parse_input("input.txt")

sorted_by_type = [[], [], [], [], [], [], []]
# pass 1
for hand_data in input_data:
    card_count = calculate_card_count(hand_data[0])

    if check_five_kind(card_count):
        sorted_by_type[0].append(hand_data)
    elif check_four_kind(card_count):
        sorted_by_type[1].append(hand_data)
    elif check_full_house(card_count):
        sorted_by_type[2].append(hand_data)
    elif check_three_kind(card_count):
        sorted_by_type[3].append(hand_data)
    elif check_two_pair(card_count):
        sorted_by_type[4].append(hand_data)
    elif check_one_pair(card_count):
        sorted_by_type[5].append(hand_data)
    elif check_high_card(card_count):
        sorted_by_type[6].append(hand_data)
    else:
        print("error in sorting by type")

# pass 2
sorted_by_strength = []


def calculate_strength(hand_data, idx):
    return strengths[hand_data[0][idx]]


def merge_lists(left_sublist, right_sublist):
    i, j = 0, 0
    result = []
    while i < len(left_sublist) and j < len(right_sublist):
        for idx in range(0, 5):
            left_strength = calculate_strength(left_sublist[i], idx)
            right_strength = calculate_strength(right_sublist[j], idx)

            if left_strength < right_strength:
                result.append(left_sublist[i])

                i += 1
                break
            elif left_strength > right_strength:

                result.append(right_sublist[j])
                j += 1
                break

    result += left_sublist[i:]
    result += right_sublist[j:]

    return result


def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        midpoint = int(len(input_list) / 2)
        left_sublist = merge_sort(input_list[:midpoint])
        right_sublist = merge_sort(input_list[midpoint:])
        return merge_lists(left_sublist, right_sublist)


for i in range(len(sorted_by_type)):
    card_list = sorted_by_type[i]
    sorted_by_strength = merge_sort(card_list) + sorted_by_strength

total_winning = 0
for i in range(1, len(sorted_by_strength) + 1):

    total_winning += int(sorted_by_strength[i - 1][1]) * i

print(total_winning)
