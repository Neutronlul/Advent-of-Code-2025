def parse_input() -> list[dict[str, int]]:
    """
    Parse the input file and return a sorted list of range dictionaries.

    Reads the input file containing comma-separated ranges in the format "min-max",
    parses each range into a dictionary with 'min' and 'max' keys, and returns
    them sorted by their minimum values.

    Returns:
        list[dict[str, int]]: A list of dictionaries, each containing 'min' and 'max'
                              keys with integer values, sorted in ascending order by 'min'.

    Example:
        If input.txt contains "1-3,11-17,5-9", the function returns:
        [{'min': 1, 'max': 3}, {'min': 5, 'max': 9}, {'min': 11, 'max': 17}]
    """
    with open("Day 2/input.txt") as file:
        return sorted(
            [
                {"min": int(min), "max": int(max)}
                for range in file.read().split(",")
                for min, max in [range.split("-")]
            ],
            key=lambda x: x["min"],
        )


def main():
    ranges = parse_input()

    print(ranges)


if __name__ == "__main__":
    main()
