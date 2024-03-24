def parse_input(file_path):
    f = open(file_path)
    data = f.readlines()
    f.close()
    result = []
    for k in data:
        k = k.strip().split(" ")
        line = []

        for i in range(len(k)):

            line.append(int(k[i]))

        result.append(line)

    return result


oasis_reports = parse_input("input.txt")

extrapolation_sum = 0
for report in oasis_reports:
    idx = 0
    level = 0
    predictions = [[report.pop()]]
    # calculating predictions
    while predictions[-1][0] != 0:
        predictions[0].append(report.pop())

        predictions.append([])
        for i in range(level + 1):
            a = predictions[i][-1]
            b = predictions[i][-2]
            c = b - a

            predictions[i + 1].append(c)
        idx += 1
        level += 1
    # extrapolating prediction to get new value
    next_value = 0
    for k in range(len(predictions) - 2, -1, -1):
        next_value = next_value + predictions[k][0]
        # print(next_value, predictions[k][0])

    extrapolation_sum += next_value

print("result->", extrapolation_sum)
