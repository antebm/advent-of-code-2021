input = open("input.txt", "r")

lines = input.readlines()
values = [int(i) for i in lines]
initial_value = values[0]

depth_increases = 0

for value in values:
    if value > initial_value:
        depth_increases = depth_increases + 1
    initial_value = value

print(depth_increases)

# second part
def three_sum(index):
    return values[index] + values[index-1] + values[index-2]

current_sum = three_sum(2)
depth_increases_2 = 0

for i in range(3, len(values)):
    if three_sum(i) > current_sum:
        depth_increases_2 = depth_increases_2 + 1

    current_sum = three_sum(i)

print(depth_increases_2)
