input = open("input.txt", "r")

values = input.readlines()

horizontal = 0
vertical = 0
aim = 0

for value in values:
    course = value.split(" ")

    if course[0] == "forward":
        horizontal = horizontal + int(course[1])
        vertical = vertical + aim * int(course[1])
    if course[0] == "down":
        aim = aim + int(course[1])
    if course[0] == "up":
        aim = aim - int(course[1])

print(horizontal * vertical)