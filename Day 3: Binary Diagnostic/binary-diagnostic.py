from math import gamma


data = open("./input.txt").read().splitlines()


def get_column(column, data=data):
    "Return a generator that returns all numbers in column 'column'"
    for i, _ in enumerate(data):
        yield data[i][column]


def pt1(data=data):
    gamma = []
    epsilon = []
    for colnum in range(12):
        for i in list(get_column(colnum)):
            num0s = i.count("0")
            num1s = i.count("1")
        if num0s > num1s:
            "0 is more common, so gamma bit is 0 and epsilon bit is 1"
            gamma.append("0")
            epsilon.append("1")
        else:
            "1 is more common, so gamma bit is 1 and epsilon bit is 0"
            gamma.append("1")
            epsilon.append("0")
    return gamma, epsilon


gamma, epsilon = pt1()
print(int("".join(epsilon), 2) * int("".join(gamma), 2))


def part2_oxygen(data=data, column=0):
    if len(data) == 1:
        return data
    num0s = 0
    num1s = 0
    for cs in list(get_column(column)):
        num0s += cs.count("0")
        num1s += cs.count("1")
    if num0s > num1s:
        "0 is more common, keep everything with a 0 in 'column' column"
        oxygen = [j for i, j in enumerate(data) if data[i][column] == "0"]
        return part2_oxygen(data=oxygen, column=column + 1)
    if num0s < num1s:
        "1 is more common, keep everything with a 1 in 'column' column"
        oxygen = [j for i, j in enumerate(data) if data[i][column] == "1"]
        return part2_oxygen(data=oxygen, column=column + 1)
    else:
        "Equal frequency, for oxygen, keep everything with a 1 in 'column' column"
        oxygen = [j for i, j in enumerate(data) if data[i][column] == "1"]
        return part2_oxygen(data=oxygen, column=column + 1)


def part2_co2(data=data, column=0):
    if len(data) == 1:
        return data
    num0s = 0
    num1s = 0
    for cs in list(get_column(column)):
        num0s += cs.count("0")
        num1s += cs.count("1")
    if num0s < num1s:
        "0 is less common, keep everything with a 0 in 'column' column"
        co2 = [j for i, j in enumerate(data) if data[i][column] == "0"]
        return part2_oxygen(data=co2, column=column + 1)
    if num0s > num1s:
        "1 is less common, keep everything with a 1 in 'column' column"
        co2 = [j for i, j in enumerate(data) if data[i][column] == "1"]
        return part2_oxygen(data=co2, column=column + 1)
    else:
        "Equal frequency, for co2, keep everything with a 0 in 'column' column"
        co2 = [j for i, j in enumerate(data) if data[i][column] == "0"]
        return part2_oxygen(data=co2, column=column + 1)


print(int(part2_co2()[0], 2) * int(part2_oxygen()[0], 2))
