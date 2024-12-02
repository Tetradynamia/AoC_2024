def decreasing(numbers: list[int]) -> bool:
    false_flag = False
    for i in range(len(numbers) - 1):
        if not (0 < (int(numbers[i]) - int(numbers[i + 1])) <= 3):
            false_flag = True
    return not false_flag


def increasing(numbers: list[int]) -> bool:
    false_flag = False
    for i in range(len(numbers) - 1):
        if not (-3 <= (int(numbers[i]) - int(numbers[i + 1])) < 0):
            false_flag = True
    return not false_flag


with open("Day_2/input.txt", "r") as f:
    data = f.readlines()
    data = [item.strip("\n").split(" ") for item in data]

safe_counter = 0
unsafe_reports = []

for item in data:
    if int(item[0]) > int(item[1]):
        if decreasing(item):
            safe_counter += 1
        else:
            unsafe_reports.append(item)
    elif int(item[0]) < int(item[1]):
        if increasing(item):
            safe_counter += 1
        else:
            unsafe_reports.append(item)
    else:
        unsafe_reports.append(item)

print(f"safe_counter: {safe_counter}")

# Part 2
for row in unsafe_reports:
    i = 0
    while i < len(row):
        test_row = row.copy()
        test_row.pop(i)
        if int(test_row[0]) > int(test_row[1]):
            if decreasing(test_row):
                safe_counter += 1
                break
        elif int(test_row[0]) < int(test_row[1]):
            if increasing(test_row):
                safe_counter += 1
                break
        i += 1
print(f"safe_counter: {safe_counter}")
