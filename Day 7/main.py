from functools import wraps


def timeline_memoization(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args[1:3]

        if len(cache_key) < 2:
            return func(*args, **kwargs)

        if cache_key in cache:
            return cache[cache_key]
        else:
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result

    return wrapper


def parse_input(input_file: str) -> list[dict[str, str | int]]:
    with open(input_file) as file:
        data = []
        for line in enumerate(file.readlines()):
            for char in enumerate(line[1]):
                if char[1] in ("S", "^"):
                    data.append(
                        {
                            "value": char[1],
                            "x": char[0],
                            "y": line[0],
                            "activated": False,
                        }
                    )
        return data


def get_starting_pos(data) -> tuple[int, int]:
    for item in data:
        if item["value"] == "S":
            return item["x"], item["y"]
    raise ValueError("No starting position found")


def get_splits(
    data: list[dict[str, str | int]],
    start_x: int = 0,
    start_y: int = 0,
) -> int:
    if not start_x and not start_y:
        start_x, start_y = get_starting_pos(data)

    if next_splitter := max(
        (
            splitter
            for splitter in data
            if splitter["value"] == "^"
            and splitter["x"] == start_x
            and int(splitter["y"]) > start_y
        ),
        key=lambda splitter: -int(splitter["y"]),
        default=None,
    ):
        if not next_splitter["activated"]:
            next_splitter["activated"] = True
            return (
                1
                + get_splits(data, int(next_splitter["x"]) - 1, int(next_splitter["y"]))
                + get_splits(data, int(next_splitter["x"]) + 1, int(next_splitter["y"]))
            )

    return 0


@timeline_memoization
def get_timelines(
    data: list[dict[str, str | int]],
    start_x: int = 0,
    start_y: int = 0,
) -> int:
    if not start_x and not start_y:
        start_x, start_y = get_starting_pos(data)

    if next_splitter := max(
        (
            splitter
            for splitter in data
            if splitter["value"] == "^"
            and splitter["x"] == start_x
            and int(splitter["y"]) > start_y
        ),
        key=lambda splitter: -int(splitter["y"]),
        default=None,
    ):
        return get_timelines(
            data, int(next_splitter["x"]) - 1, int(next_splitter["y"])
        ) + get_timelines(data, int(next_splitter["x"]) + 1, int(next_splitter["y"]))

    return 1


def main():
    test_data = parse_input("Day 7/sample.txt")

    result = get_splits(test_data)

    assert result == 21, f"Expected 21 but got {result}"

    test_data = parse_input("Day 7/sample.txt")

    result = get_timelines(test_data)

    assert result == 40, f"Expected 40 but got {result}"

    data = parse_input("Day 7/input.txt")

    print(f"part 1: {get_splits(data)}")

    data = parse_input("Day 7/input.txt")

    print(f"part 2: {get_timelines(data)}")


if __name__ == "__main__":
    main()
