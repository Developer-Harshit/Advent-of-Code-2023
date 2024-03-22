import os

folder_number = int(input("Enter folder number -> "))
folder_path = "day" + str(folder_number)
try:
    os.makedirs(folder_path)
except FileExistsError:
    pass


f = open(folder_path + "/part_one.py", "a")
f.close()
f = open(folder_path + "/part_two.py", "a")
f.close()
f = open(folder_path + "/input.txt", "a")
f.close()
os.popen("code ./" + folder_path + " -r")
