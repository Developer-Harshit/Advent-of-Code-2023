def parse_input(file_path):
    f = open(file_path, "r")
    data = f.readlines()
    cards_data = []
    for card in data:
        card = card.strip().split(":")[1].strip().split("|")
        winning_nums = card[0].strip().split(" ")
        user_nums = card[1].strip().split(" ")
        cards_data.append(winning_nums)
        cards_data.append(user_nums)

    return cards_data


input_data = parse_input("input.txt")
open_list = [*range(0, len(input_data), 2)]
lookup_table = {}

closed_list = []
while len(open_list) != 0:
    i = open_list[-1]
    win_numbers = [*input_data[i]]
    elf_numbers = [*input_data[i + 1]]

    points = 0
    closed_list.append(open_list.pop(-1))

    if i not in lookup_table:
        lookup_table[i] = []

        for elf_num in elf_numbers:
            if elf_num in win_numbers and elf_num.isnumeric():

                win_numbers.remove(elf_num)

                points += 1
        for k in range(1, points + 1):
            new_item = i + 2 * k
            if len(input_data) - 1 > new_item:
                lookup_table[i].append(new_item)

                open_list.append(i + 2 * k)
    else:
        for k in lookup_table[i]:
            open_list.append(k)


print(len(closed_list))
