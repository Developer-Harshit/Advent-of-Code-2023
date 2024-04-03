filename = "input.txt"


def parse_input():
    f = open(filename)  # array of {width,height,pattern}
    data = f.readlines()
    result = []
    height = 0
    curr = {"height": 0, "width": 0, "pattern": ""}
    for i in range(len(data)):
        line = (data[i]).strip()
        if line == "":
            result.append(curr)
            curr = {"height": 0, "width": 0, "pattern": ""}
            continue
        curr["width"] = len(line)
        curr["height"] += 1
        curr["pattern"] += line
    result.append(curr)
    return result


def index(i, j, pdata):
    return i + j * pdata["width"]


def display(pdata):
    pattern = pdata["pattern"]
    for j in range(pdata["height"]):
        for i in range(pdata["width"]):
            idx = index(i, j, pdata)
            print(pattern[idx], end="")
        print()


def reflect_vertical(pdata):
    width = pdata["width"]
    height = pdata["height"]
    pattern = pdata["pattern"]

    for mpos in range(width):
        left = mpos
        right = left + 1
        is_reflecting = False

        while left >= 0 and right < width:

            # FINDING RHS AND LHS
            RHS = pattern[right::width]
            LHS = pattern[left::width]
            if LHS != RHS:
                is_reflecting = False

                break
            is_reflecting = True
            left -= 1
            right += 1
        if is_reflecting:

            return mpos + 1
    return 0


def reflect_horizontal(pdata):
    width = pdata["width"]
    height = pdata["height"]
    pattern = pdata["pattern"]

    for mpos in range(height):
        left = mpos
        right = left + 1
        is_reflecting = False

        while left >= 0 and right < height:

            # FINDING RHS AND LHS
            RHS = pattern[right * width : (right + 1) * width]
            LHS = pattern[left * width : (left + 1) * width]

            if LHS != RHS:
                is_reflecting = False
                break
            is_reflecting = True
            left -= 1
            right += 1
        if is_reflecting:

            return mpos + 1
    return 0


input_data = parse_input()
result = 0
for pattern_data in input_data:
    v_value = reflect_vertical(pattern_data)
    h_value = reflect_horizontal(pattern_data)
    result += v_value + h_value * 100
print("Result", result)
