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
            print(tem_data)
        games.append(round_data)
    return games


balls = ["red", "blue", "green"]
ball_condition = {"red": 12, "green": 13, "blue": 14}
input_data = parse_input("input.txt")


def is_valid(gdata):
    for rdata in gdata:
        for bid in balls:
            if rdata[bid] > ball_condition[bid]:
                return False
    return True


id_sum = 0
for gid in range(1, len(input_data) + 1):
    gdata = input_data[gid - 1]
    if is_valid(gdata):
        id_sum += gid
print(id_sum)
