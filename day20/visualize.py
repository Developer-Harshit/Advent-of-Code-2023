import os

f = open("input.txt")
data = f.read().splitlines()
f.close()

f = open("input.dot", "w")
f.write("digraph {\n")
for line in data:
    if "broadcaster" not in line:
        line = line[1:]
    f.write(line + ";\n")

f.write("}")
f.close()


out_format = "png"
command = f"dot -T{out_format} input.dot > output.{out_format}"
os.system(command)
