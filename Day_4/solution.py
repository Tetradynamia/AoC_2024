from collections import defaultdict

with open("Day_4/input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]


xmas_counter = 0


# Check each row
for line in data:
    xmas_counter += line.count("XMAS")
    xmas_counter += line[::-1].count("XMAS")


# Check each column
for i in range(len(data)):
    test_string = ""
    for j in range(len(data[i])):
        test_string += data[j][i]
    xmas_counter += test_string.count("XMAS")
    xmas_counter += test_string[::-1].count("XMAS")


# Check each major diagonal
diagonals = defaultdict(list)
for y in range(len(data)):
    for x in range(len(data[y])):
        diagonals[x - y].append(data[y][x])


for key in diagonals.keys():
    test_string = "".join(diagonals[key])
    xmas_counter += test_string.count("XMAS")
    xmas_counter += test_string[::-1].count("XMAS")

# Check each minor diagonal
diagonals_2 = defaultdict(list)
for y in range(len(data)):
    for x in range(len(data[y]) - 1, -1, -1):
        diagonals_2[y + x].append(data[x][y])

for key in diagonals_2.keys():
    test_string = "".join(diagonals_2[key])
    xmas_counter += test_string.count("XMAS")
    xmas_counter += test_string[::-1].count("XMAS")
print(xmas_counter)


######################################## PART 2
x_count = 0

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        if data[x][y] == "A":
            test_1 = "".join([data[x - 1][y - 1], data[x + 1][y + 1]])
            if test_1 == "MS" or test_1 == "SM":
                test_1 = "".join([data[x - 1][y + 1], data[x + 1][y - 1]])
                if test_1 == "MS" or test_1 == "SM":
                    x_count += 1

print(x_count)
