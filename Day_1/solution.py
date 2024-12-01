with open("Day_1/input_1.txt", "r") as f:
    data = f.readlines()
    data = [item.strip("\n").split("   ") for item in data]


left_list = []
right_list = []

for item in data:
    left_list.append(int(item[0]))
    right_list.append(int(item[1]))

left_list = sorted(left_list)
right_list = sorted(right_list)


total_difference = 0
for index, item in enumerate(left_list):
    total_difference += abs(right_list[index] - left_list[index])

print(total_difference)


total_similarity = 0

for num in left_list:
    total_similarity += num * right_list.count(num)

print(total_similarity)
