import datetime
import os

# Create folder and files for today's challenge

today = datetime.datetime.now().day
name = "day-" + str(today)

if(os.path.isdir(name)):
    print("Folder already exists.")
    exit()

os.mkdir(name)
os.chdir(name)
os.system("touch " + name + ".py")
os.system("touch " + name + ".txt")

with open(name + ".py", "w") as file:
    file.write("# Advent of Code 2023\n# Day " + str(today) + "\n\n# Part 1\nfile = open(\"" + name + ".txt\", \"r\")\n\n# Part 2\n")

print("Created folder and files for day " + str(today) + ".")
print("Today's challenge: https://adventofcode.com/2023/day/" + str(today))