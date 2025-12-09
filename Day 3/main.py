def parse_input(input_file: str) -> list[str]:
    with open(input_file) as file:
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


def find_largest_joltage_part_2(banks: list[str], battery_count: int) -> int:
    total_joltage = 0
    for bank in banks:
        max_joltage = ""
        start_index = 0
        for x in range(battery_count):
            largest_battery = 0
            battery_index = 0

            for battery in bank[start_index : len(bank) - (battery_count - (x + 1))]:
                joltage = int(battery)
                if joltage > largest_battery:
                    largest_battery = joltage
                    battery_index = bank.index(battery, start_index)

                    if largest_battery == 9:
                        break

            max_joltage += str(largest_battery)
            start_index = battery_index + 1

            # print(f"selected battery: {largest_battery} at position {start_index}")

        total_joltage += int(max_joltage)

    return total_joltage


def main():
    test_data = parse_input("Day 3/sample.txt")

    assert find_largest_joltage_part_2(test_data, 2) == 357
    assert find_largest_joltage_part_2(test_data, 12) == 3121910778619

    data = parse_input("Day 3/input.txt")

    print(f"Total output joltage (Part 1): {find_largest_joltage_part_1(data)}")

    print(f"Total output joltage (Part 2): {find_largest_joltage_part_2(data, 12)}")


if __name__ == "__main__":
    main()
