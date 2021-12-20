with open("input.txt", "r") as f:
    data = f.read().splitlines()

# data = """00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".splitlines()


def get_column(column, data=data):
    "Return a string that includes all numbers in column 'column'"
    return "".join([data[i][column] for i, _ in enumerate(data)])


def pt1(data=data):
    gamma = []
    epsilon = []
    num_cols = len(data[0])
    for colnum in range(num_cols):
        i = get_column(colnum)
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
print("part 1=", int("".join(epsilon), 2) * int("".join(gamma), 2))


def check_bit(i, col, val):
    # return true if bit col in i is equal to val
    return i[col] == val


def part2_oxygen(data=data, column=0):
    if len(data) == 1:
        return int(data[0], 2)
    cs = get_column(column, data)
    num0s = cs.count("0")
    num1s = cs.count("1")

    if num0s > num1s:
        # keep zeros in this bit position
        keep = "0"
    else:
        keep = "1"
    print(f"COL {column} {data} ({num0s}/{num1s}) keeping {keep}")
    f_expr = lambda x: check_bit(x, column, val=keep)
    return part2_oxygen(data=list(filter(f_expr, data)), column=column + 1)


def part2_co2(data=data, column=0):
    if len(data) == 1:
        return int(data[0], 2)
    cs = get_column(column, data)
    num0s = cs.count("0")
    num1s = cs.count("1")

    if num0s > num1s:
        # keep ones in this bit position
        keep = "1"
    else:
        keep = "0"
    print(f"COL {column} {data} ({num0s}/{num1s}) keeping {keep}")
    f_expr = lambda x: check_bit(x, column, val=keep)
    return part2_co2(data=list(filter(f_expr, data)), column=column + 1)


print("part 2")

oxy = part2_oxygen(data)
print("oxy = ", oxy)

co2 = part2_co2(data)
print("co2 = ", co2)

print("part2 -- ", oxy * co2)
