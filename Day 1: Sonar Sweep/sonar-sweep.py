import os

data = open("./input.txt").read().splitlines()
data = list(map(int, data))


def sonar_sweep(input_data):
    count = 0
    for index, value in enumerate(input_data):
        if value > input_data[index - 1]:
            count += 1
    return count


def mini_batch(input_data, batch_size=3):
    "Break input list into a list of lists, each with a a size of batch_size"
    output_data = []
    for i in range(len(input_data) - batch_size + 1):
        output_data.append(input_data[i : i + batch_size])
    return output_data


def sliding_window(input_data, window_size=3):
    count = 0
    input_data = mini_batch(input_data)
    sums = []
    for a, b, c in input_data:
        sum = a + b + c
        sums.append(sum)
    return sonar_sweep(sums)


print(sonar_sweep(data))
print(sliding_window(data))
