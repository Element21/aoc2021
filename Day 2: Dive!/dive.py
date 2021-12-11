data = open("./input.txt").read().split()


def part1(input_data):
    submarine = {"forward": 0, "down": 0, "up": 0}
    for index, value in enumerate(input_data):
        if value in submarine:
            # If i is equal to a key in the list, add the next item in data (the amount of units to travel) to the value of that key
            submarine[value] += int(input_data[index + 1])
    depth = submarine["down"] - submarine["up"]
    return submarine["forward"] * depth


def part2(input_data, aim=0, depth=0):
    submarine = {"forward": 0, "down": 0, "up": 0}
    for index, value in enumerate(input_data):
        if value == "down":
            aim += int(input_data[index + 1])
        elif value == "up":
            aim -= int(input_data[index + 1])
        elif value == "forward":
            submarine[value] += int(input_data[index + 1])
            depth += aim * int(input_data[index + 1])
    depth = (submarine["down"] - submarine["up"]) + depth
    return submarine["forward"] * depth


print(part1(data))
print(part2(data))
