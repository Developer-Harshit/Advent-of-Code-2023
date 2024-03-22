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
points_sum = 0
for i in range(0, len(input_data), 2):
    win_numbers = input_data[i]
    elf_numbers = input_data[i + 1]

    points = 0
    for elf_num in elf_numbers:
        if elf_num in win_numbers and elf_num.isnumeric():

            win_numbers.remove(elf_num)

            if points == 0:
                points = 1
            else:
                points = points + points

    points_sum += points
print(points_sum)
