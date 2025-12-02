dial = 50
zeros = 0

# with open("Day 1/input.txt") as file:
#     for line in file:
#         direction = line[0]
#         clicks = line.lstrip("RL")
#         remainder = int(clicks) % 100
#         if direction == "R":
#             dial += remainder
#         else:
#             dial -= remainder
#         dial = dial % 100
#         if dial == 0:
#             zeros += 1
#         zeros += int(clicks) / 100


with open("Day 1/input.txt") as file:
    for line in file:
        direction = line[0]
        clicks = int(line.lstrip("RL"))
        if direction == "L":
            clicks *= -1

        zeros += abs(clicks) // 100
        clicks = clicks % 100

        final_position = (dial + clicks) % 100

        if direction == "R" and final_position < dial:
            zeros += 1
        elif direction == "L" and final_position > dial:
            zeros += 1

        dial = final_position

print(zeros)
