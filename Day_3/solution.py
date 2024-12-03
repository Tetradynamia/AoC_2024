import re


def process_data(data: str, expression: str, total=0) -> int:
    expression = re.compile(expression)
    matches = expression.findall(data)

    for match in matches:
        nums = match.split(",")
        total += int(nums[0]) * int(nums[1])

    return total


def exclusions(data: str, expression: str) -> list[str]:
    pattern = re.compile("(do\(\)|don't\(\))")
    iter = re.finditer(
        pattern,
        data,
        flags=0,
    )

    do_flag = True
    start = []
    end = []
    for item in iter:
        if not do_flag and item.group() == "do()":
            end.append(item.span()[1])
            do_flag = True
        elif do_flag and item.group() == "don't()":
            start.append(item.span()[0])
            do_flag = False

    parts = zip(start, end)
    return parts


with open("Day_3/input.txt", "r") as f:
    data = f.read()

ans1 = process_data(data, r"mul\((\d{1,3},\d{1,3})\)")
print(f"Part 1: {ans1}")

parts = exclusions(data, r"(do\(\)|don't\(\))")
exclude_total = 0
for item in parts:
    exclude_total += process_data(data[item[0] : item[1]], r"mul\((\d{1,3},\d{1,3})\)")

ans2 = ans1 - exclude_total
print(f"Part 2: {ans2}")
