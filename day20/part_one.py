from collections import deque

low, high = False, True
flipflop, conjunction = "%", "&"
filename = "input.txt"


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


def count(pulse):
    global low_counter, high_counter

    if pulse:
        high_counter += 1
    else:
        low_counter += 1


def press_button():

    open_set = deque([("button", low, "broadcaster")])
    count(low)
    while len(open_set):
        sender, pulse, src = open_set.pop()

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

                count(pulse)
                open_set.appendleft((src, pulse, dest))

        elif module[1] == conjunction:
            destData, _, memories = module

            memories[sender] = pulse
            pulse = high

            if sum(memories.values()) == len(memories):
                pulse = low

            for dest in destData:

                count(pulse)
                open_set.appendleft((src, pulse, dest))

            pass
        else:
            destData = module[0]
            for dest in destData:

                count(low)
                open_set.appendleft((src, low, dest))


configs = parse_input()
low_counter = 0
high_counter = 0
for i in range(1000):
    press_button()
print("low->", low_counter, "high->", high_counter)
print("Result->", low_counter * high_counter)
