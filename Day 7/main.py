from functools import wraps


def memoization(func):
    cache = set()

    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = args[1:3]

        if len(cache_key) < 2:
            return func(*args, **kwargs)

        if cache_key in cache:
            return 0
        else:
            cache.add(cache_key)
            return func(*args, **kwargs)

    def clear_cache():
        cache.clear()

    wrapper.clear_cache = clear_cache  # pyright: ignore[reportAttributeAccessIssue]

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


@memoization
def get_splits(
    data: list[dict[str, str | int]],
    start_x: int = 0,
    start_y: int = 0,
) -> int:
    if not start_x and not start_y:
        start_x, start_y = get_starting_pos(data)

    if next_splitter := max(
        (
            d
            for d in data
            if d["value"] == "^" and d["x"] == start_x and int(d["y"]) > start_y
        ),
        key=lambda d: -int(d["y"]),
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


def main():
    test_data = parse_input("Day 7/sample.txt")

    result = get_splits(test_data)

    print(result)

    assert result == 21, f"Expected 21 but got {result}"

    get_splits.clear_cache()  # pyright: ignore[reportFunctionMemberAccess]

    data = parse_input("Day 7/input.txt")

    print(get_splits(data))


if __name__ == "__main__":
    main()
