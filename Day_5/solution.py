from math import floor


def is_ordered(update: list[int], instructions: list[list[int]], ordered=True) -> bool:
    for instruction in instructions:
        try:
            ind1 = update.index(instruction[0])
            ind2 = update.index(instruction[1])
            if ind1 < ind2:
                continue
            else:
                ordered = False
        except ValueError:
            continue
    return ordered


def orderCorrectly(update: list[int], instructions: list[list[int]]) -> list[int]:
    for instruction in instructions:
        try:
            ind1 = update.index(instruction[0])
            ind2 = update.index(instruction[1])
            if ind1 < ind2:
                continue
            else:
                update[ind1], update[ind2] = update[ind2], update[ind1]
                return orderCorrectly(update, instructions)
        except ValueError:
            continue
    return update


def findMiddle(numbers: list[int]) -> int:
    middle_index = floor(len(numbers) / 2)
    return numbers[middle_index]


with open("Day_5/input.txt", "r") as f:
    data = f.readlines()
    instructions = [line.strip() for line in data if "|" in line]
    updates = [line.strip() for line in data if "|" not in line and line != "\n"]


instructions = [list(map(int, instruction.split("|"))) for instruction in instructions]
updates = [list(map(int, update.split(","))) for update in updates]


correctly_ordered = []
incorrectly_ordered = []
for update in updates[:]:
    if is_ordered(update, instructions):
        correctly_ordered.append(update)
    else:
        incorrectly_ordered.append(update)


total = 0
for item in correctly_ordered:
    total += findMiddle(item)

print(f"Part 1 answer: {total}")


corrected = []
for item in incorrectly_ordered:
    corrected.append(orderCorrectly(item, instructions))

total = 0
for item in corrected:
    total += findMiddle(item)
print(f"Part 2 answer: {total}")
