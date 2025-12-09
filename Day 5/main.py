def parse_input(input_file: str) -> dict[str, list[int | list[int]]]:
    with open(input_file) as file:
        lines = file.readlines()
        return {
            "ranges": [
                [int(x) for x in line.strip().split("-")]
                for line in lines
                if line.find("-") != -1
            ],
            "ids": [
                int(line.strip())
                for line in lines
                if line.find("-") == -1 and line.strip()
            ],
        }


def count_fresh_ids(data: dict) -> int:
    count = 0
    for id in data["ids"]:
        for range in data["ranges"]:
            if int(range[0]) <= int(id) <= int(range[1]):
                count += 1
                break
    return count


def unoverlap_ranges(ranges: list[list[int]]) -> list[list[int]]:
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    cleaned_ranges = []
    for range in sorted_ranges:
        if not cleaned_ranges:
            cleaned_ranges.append(range)
        else:
            last = cleaned_ranges[-1]
            if range[0] <= last[1] + 1:
                last[1] = max(last[1], range[1])
            else:
                cleaned_ranges.append(range)
    return cleaned_ranges


def total_fresh_ids(data: dict) -> int:
    total = 0
    cleaned_ranges = unoverlap_ranges(data["ranges"])
    for range in cleaned_ranges:
        total += int(range[1]) - int(range[0]) + 1
    return total


def main():
    test_data = parse_input("Day 5/sample.txt")

    assert count_fresh_ids(test_data) == 3
    assert total_fresh_ids(test_data) == 14

    data = parse_input("Day 5/input.txt")

    print(count_fresh_ids(data))
    print(total_fresh_ids(data))


if __name__ == "__main__":
    main()
