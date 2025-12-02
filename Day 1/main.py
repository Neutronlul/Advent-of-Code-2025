def part1(initial_settings):
    dial = initial_settings["dial"]
    zeros = initial_settings["zeros"]
    with open("Day 1/input.txt") as file:
        for line in file:
            direction = line[0]
            clicks = int(line.lstrip("RL"))
            remainder = clicks % 100
            if direction == "R":
                dial += remainder
            else:
                dial -= remainder
            dial = dial % 100
            if dial == 0:
                zeros += 1

    print(f"Part 1: {zeros}")


def part2(initial_settings):
    dial = initial_settings["dial"]
    zeros = initial_settings["zeros"]
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

    print(f"Part 2: {zeros}")


def main():
    initial_settings = {"dial": 50, "zeros": 0}

    part1(initial_settings)

    part2(initial_settings)


if __name__ == "__main__":
    main()
