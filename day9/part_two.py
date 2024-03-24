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


def has_all_zero(report):
    r_set = set(report)
    return len(r_set) == 1 and report[0] == 0


oasis_reports = parse_input("input.txt")

extrapolation_sum = 0
for report in oasis_reports:

    idx = 0
    predictions = [report]
    # calculating predictions
    while not has_all_zero(predictions[-1]):
        predictions.append([])
        for i in range(len(predictions[idx]) - 1):
            a = predictions[idx][i]
            b = predictions[idx][i + 1]
            c = b - a
            predictions[-1].append(c)
        idx += 1
        print(predictions[-1])

    # extrapolating prediction to get new value
    next_value = 0
    for k in range(len(predictions) - 1, -1, -1):
        next_value = predictions[k][0] - next_value
        # print(next_value, predictions[k][0])

    extrapolation_sum += next_value

print("result->", extrapolation_sum)
