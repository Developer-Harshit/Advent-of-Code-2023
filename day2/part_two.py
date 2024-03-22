def parse_input(file_path):
    f = open(file_path, "r")
    data = f.readlines()
    games = []
    for i in range(len(data)):
        line = data[i]
        line = line.strip()
        rouunds = line.split(":")[1].split(";")
        round_data = []
        tem_data = {"red": 0, "blue": 0, "green": 0}
        for i in rouunds:
            tem_data = {"red": 0, "blue": 0, "green": 0}
            for k in i.split(","):
                packet = k.split(" ")
                tem_data[packet[2]] = int(packet[1]) + tem_data[packet[2]]
            round_data.append(tem_data)
        games.append(round_data)
    return games


balls = ["red", "blue", "green"]
ball_condition = {"red": 12, "green": 13, "blue": 14}
input_data = parse_input("input.txt")


def calculate_minimum(gdata):
    min_balls = {"red": 0, "blue": 0, "green": 0}
    for rdata in gdata:
        for bid in balls:
            min_balls[bid] = max(rdata[bid], min_balls[bid])
    return min_balls


power_sum = 0
for gid in range(1, len(input_data) + 1):
    gdata = input_data[gid - 1]
    min_balls = calculate_minimum(gdata)
    power_sum += min_balls["red"] * min_balls["green"] * min_balls["blue"]
print(power_sum)