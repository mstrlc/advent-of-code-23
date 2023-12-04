# Advent of Code 2023
# Day 1

# Part 1
file = open("day-1.txt", "r")

lines = file.readlines()
total = 0

for line in lines:
    first_number = None
    second_number = None
    for char in line:
        if char.isdigit():
            if first_number == None:
                first_number = char
            second_number = char
    total = total + int(first_number + second_number)

print(total)

# Part 2
words_numbers = {
    "zero": "ze0ro",
    "one": "on1e",
    "two": "tw2o",
    "three": "thr3ee",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "sev7en",
    "eight": "eig8ht",
    "nine": "ni9ne"
}

total = 0

for line in lines:
    first_number = None
    second_number = None
    for word, num in words_numbers.items():
        line = line.replace(word, num)
    for char in line:
        if char.isdigit():
            if first_number == None:
                first_number = char
            second_number = char
    total = total + int(first_number + second_number)

print(total)
