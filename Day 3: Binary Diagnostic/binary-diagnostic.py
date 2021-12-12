data = open("./input.txt").read().splitlines()
column_stack = []
gamma = []
epsilon = []

# Format data into columns
for i in range(12):
    features, classes = zip(*[(s[:i], [s[i]]) for s in data])
    column_stack.append("".join(j for i in classes for j in i))

# Now we can calculate delta and gamma values for the solution!
def pt1(data=data):
    for i in column_stack:
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


gamma_dec = int("".join(gamma), 2)
epsilon_dec = int("".join(epsilon), 2)

print(f"Gamma (decimal): {gamma_dec} ({''.join(gamma)})")
print(f"Epsilon (decimal): {epsilon_dec} ({''.join(epsilon)})")
print(f"Pt. 1 Answer: {gamma_dec * epsilon_dec}")