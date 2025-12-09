import time
from functools import wraps


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{fn.__name__} took {elapsed:.6f} s")
        return result

    return wrapper


@timeit
def parse_input(input_file: str) -> list[dict[str, str]]:
    """
    Parse the input file and return a sorted list of range dictionaries.

    Reads the input file containing comma-separated ranges in the format "min-max",
    parses each range into a dictionary with 'min' and 'max' keys, and returns
    them sorted by their minimum values.

    Returns:
        list[dict[str, str]]: A list of dictionaries, each containing 'min' and 'max'
                              keys with numeric string values, sorted in ascending order by 'min'.

    Example:
        If input.txt contains "1-3,11-17,5-9", the function returns:
        [{'min': '1', 'max': '3'}, {'min': '5', 'max': '9'}, {'min': '11', 'max': '17'}]
    """
    with open(input_file) as file:
        return sorted(
            [
                {"min": min, "max": max}
                for range in file.read().split(",")
                for min, max in [range.split("-")]
            ],
            key=lambda x: int(x["min"]),
        )


def split_id(id: str) -> tuple[str, str]:
    half = len(id) // 2
    return id[:half], id[half:]


@timeit
def find_invalid_ids_naive(ranges) -> list[int]:
    invalid_ids = []
    for id_range in ranges:
        for id in range(int(id_range["min"]), int(id_range["max"]) + 1):
            for first_half, second_half in [split_id(str(id))]:
                # print(first_half, second_half)
                if first_half != second_half:
                    break
            else:
                invalid_ids.append(id)
                # print(f"Invalid ID found: {id}")
    return invalid_ids


def raise_min_to_first_double(range) -> dict[str, str] | None:
    first_double = split_id(range["min"])[0] * 2

    if first_double <= range["max"] and first_double >= range["min"]:
        range["min"] = first_double
    elif int(first_double) + (10 ** (len(first_double) // 2) + 1) < int(range["max"]):
        range["min"] = str(int(first_double) + (10 ** (len(first_double) // 2) + 1))
    else:
        range["min"] = None

    return range if range["min"] else None


def evenify_ranges(ranges: list[dict[str, str]]) -> list[dict[str, str]]:
    pruned_ranges = []
    for id_range in ranges:
        min_digits = len(id_range["min"])
        max_digits = len(id_range["max"])

        if min_digits == max_digits and min_digits % 2 == 0:
            id_range = raise_min_to_first_double(id_range)
            if id_range:
                pruned_ranges.append(id_range)
        elif min_digits != max_digits and max_digits - min_digits == 1:
            if min_digits % 2 == 0:
                id_range["max"] = "9" * min_digits
            else:
                id_range["min"] = "1" + "0" * (max_digits - 1)
            id_range = raise_min_to_first_double(id_range)
            if id_range:
                pruned_ranges.append(id_range)
    return pruned_ranges


@timeit
def find_invalid_ids(ranges) -> list[int]:
    invalid_ids = []
    ranges = evenify_ranges(ranges)

    # print(f"Pruned ranges: {ranges}")

    for id_range in ranges:
        for id in range(
            int(id_range["min"]),
            int(id_range["max"]) + 1,
            10 ** (len(id_range["min"]) // 2) + 1,
        ):
            invalid_ids.append(id)
            # print(f"Invalid ID found: {id}")
    return invalid_ids


def partition_ranges(ranges) -> list[dict[str, str]]:
    partitioned_ranges = []
    for id_range in ranges:
        min_digits = len(id_range["min"])
        max_digits = len(id_range["max"])
        if min_digits != max_digits and max_digits - min_digits == 1:
            # Split the range into two ranges
            first_range = {
                "min": id_range["min"],
                "max": "9" * min_digits,
            }
            second_range = {
                "min": "1" + "0" * (max_digits - 1),
                "max": id_range["max"],
            }
            partitioned_ranges.append(first_range)
            partitioned_ranges.append(second_range)
        elif min_digits != max_digits and max_digits - min_digits > 1:
            raise ValueError(
                f"Range {id_range} has more than one digit difference between min and max"
            )
        else:
            partitioned_ranges.append(id_range)
    return sorted(
        partitioned_ranges,
        key=lambda x: int(x["min"]),
    )


def get_factors(id_range) -> set[int]:
    factors = set(
        x
        for tup in (
            [i, len(id_range["min"]) // i]
            for i in range(1, int(len(id_range["min"]) ** 0.5) + 1)
            if len(id_range["min"]) % i == 0
        )
        for x in tup
    )

    factors.discard(len(id_range["min"]))

    return factors


def split_arbitrary(id: str, factor: int) -> list[str]:
    parts = [id[i : i + factor] for i in range(0, len(id), factor)]
    return parts


@timeit
def find_invalid_ids_naive_2(ranges) -> list[int]:
    invalid_ids = []
    ranges = partition_ranges(ranges)
    for id_range in ranges:
        factors = get_factors(id_range)
        for factor in factors:
            for id in range(
                int(id_range["min"]),
                int(id_range["max"]) + 1,
            ):
                parts = split_arbitrary(str(id), factor)
                if len(set(parts)) == 1 and id not in invalid_ids:
                    invalid_ids.append(id)
                    # print(f"Invalid ID found: {id}")

    return invalid_ids


def main():
    test_ranges = parse_input("Day 2/sample.txt")

    test_ranges_copy = [r.copy() for r in test_ranges]

    assert sum(find_invalid_ids_naive(test_ranges_copy)) == 1227775554

    test_ranges_copy = [r.copy() for r in test_ranges]

    assert sum(find_invalid_ids(test_ranges_copy)) == 1227775554

    test_ranges_copy = [r.copy() for r in test_ranges]

    assert sum(find_invalid_ids_naive_2(test_ranges_copy)) == 4174379265

    ranges = parse_input("Day 2/input.txt")

    print("Part 1:")

    ranges_copy = [r.copy() for r in ranges]

    print(f"Sum of all invalid IDs: {sum(find_invalid_ids_naive(ranges_copy))}")

    ranges_copy = [r.copy() for r in ranges]

    print(f"Sum of all invalid IDs: {sum(find_invalid_ids(ranges_copy))}")

    print("\n" + "-" * 20 + "\nPart 2:")

    ranges_copy = [r.copy() for r in ranges]

    print(f"Sum of all invalid IDs: {sum(find_invalid_ids_naive_2(ranges_copy))}")


if __name__ == "__main__":
    main()
