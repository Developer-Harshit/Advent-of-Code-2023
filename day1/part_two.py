f = open("input.txt", "r")
input_data = f.readlines()

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
final_sum = 0
for seg in input_data:
    num_count = 0
    first = 0
    last = 0

    mystr = ""
    for letter in seg:
        if not (letter.isalpha() or letter.isnumeric()):
            continue
        if letter.isnumeric():
            if num_count == 0:
                first = int(letter)
            last = int(letter)
            num_count += 1
            continue

        mystr += letter
        for i in range(len(numbers)):
            word = numbers[i]
            if word in mystr:
                if num_count == 0:
                    first = i + 1
                last = i + 1
                num_count += 1
                mystr = mystr[-1]

    final_sum += int(str(first) + str(last))

print(final_sum)
