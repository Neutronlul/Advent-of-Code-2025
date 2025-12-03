def parse_input() -> list[str]:
    with open("Day 3/input.txt") as file:
        return file.read().splitlines()


def find_largest_joltage_part_1(banks: list[str]) -> int:
    total_joltage = 0
    for bank in banks:
        largest_battery = 0
        first_battery_index = 0

        for battery in bank:
            joltage = int(battery)
            if joltage > largest_battery and bank.index(battery) != len(bank) - 1:
                largest_battery = joltage
                first_battery_index = bank.index(battery)

        max_joltage = str(largest_battery)

        largest_battery = 0

        for battery in bank[first_battery_index + 1 :]:
            joltage = int(battery)
            if joltage > largest_battery:
                largest_battery = joltage

        max_joltage += str(largest_battery)

        total_joltage += int(max_joltage)

    return total_joltage


def find_largest_joltage_part_2(banks: list[str]) -> int:
    pass


def main():
    data = parse_input()

    print(f"Total output joltage (Part 1): {find_largest_joltage_part_1(data)}")

    print(f"Total output joltage (Part 2): {find_largest_joltage_part_2(data)}")


if __name__ == "__main__":
    main()
