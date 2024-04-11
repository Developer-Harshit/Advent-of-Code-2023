from collections import deque

low, high = False, True
flipflop, conjunction = "%", "&"
filename = "input.txt"


def find_lcm(nums):
    result = [*nums]
    while len(result) > 1:
        n = lcm_of_two(result.pop(), result.pop())
        result.append(n)
    return result[0]


def lcm_of_two(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num2, num1 * num2 + 1, num2):
        if x % num1 == 0:
            return x


def parse_input():
    f = open(filename)
    data = f.read().splitlines()
    f.close()
    configs = {}
    conjs = []
    for i in range(len(data)):
        src, dest = data[i].split(" -> ")
        if src[0] == flipflop:

            configs[src[1:]] = [dest.split(", "), "%", False]

        elif src[0] == conjunction:

            configs[src[1:]] = [dest.split(", "), "&", {}]
            conjs.append(src[1:])

        else:

            configs[src] = [dest.split(", "), "broadcaster"]
            continue
    for c in conjs:
        memories = configs[c][2]
        for key in configs:
            if key == c:
                continue
            destData = configs[key][0]
            if c in destData:
                memories[key] = False

    return configs


def press_button(mystopper):

    open_set = deque([("button", low, "broadcaster")])

    while len(open_set):
        sender, pulse, src = open_set.pop()

        if sender == mystopper:

            if pulse == high:
                return True
        if src not in configs:
            continue
        module = configs[src]

        if module[1] == flipflop:
            if pulse != low:
                continue
            module[2] = not module[2]

            if module[2]:
                pulse = high

            destData = module[0]
            for dest in destData:

                open_set.appendleft((src, pulse, dest))

        elif module[1] == conjunction:
            destData, _, memories = module

            memories[sender] = pulse
            pulse = high

            if sum(memories.values()) == len(memories):
                pulse = low

            for dest in destData:

                open_set.appendleft((src, pulse, dest))

            pass
        else:
            destData = module[0]
            for dest in destData:

                open_set.appendleft((src, low, dest))


cList = []
for k in ["tr", "dr", "nh", "xm"]:

    configs = parse_input()
    counter = 1
    while 1:
        if press_button(k):
            break
        else:
            counter += 1
    cList.append(counter)

print("Result->", find_lcm(cList))
