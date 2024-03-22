f = open("input.txt", "r")
input_data = f.readlines()


final_sum = 0
for seg in input_data:
    nums = 0
    first = 0
    last = 0
    for letter in seg:
        if letter.isnumeric():
            if nums == 0:
                first = int(letter)

            last = int(letter)
            nums += 1
    final_sum += int(str(first) + str(last))

print(final_sum)
