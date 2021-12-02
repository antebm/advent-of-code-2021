input = open("input.txt", "r")

values = input.readlines()

horizontal = 0
vertical = 0

for value in values:
    course = value.split(" ")

    if course[0] == "forward":
        horizontal = horizontal + int(course[1])
    if course[0] == "down":
        vertical = vertical + int(course[1])
    if course[0] == "up":
        vertical = vertical - int(course[1])

print(horizontal * vertical)