def parse_input() -> list[list[dict[str, int | bool]]]:
    with open("Day 4/input.txt") as file:
        return [
            [{"is_full": char == "@", "neighbor_count": 0} for char in line]
            for line in file.read().splitlines()
        ]


def increment_neighbors(
    grid: list[list[dict[str, int | bool]]], row: int, col: int
) -> None:
    for r in range(max(0, row - 1), min(len(grid), row + 2)):
        for c in range(max(0, col - 1), min(len(grid[0]), col + 2)):
            if grid[r][c]["is_full"] and (r != row or c != col):
                grid[r][c]["neighbor_count"] += 1


def build_adjacency_weightings(grid: list[list[dict[str, int | bool]]]) -> None:
    for row in enumerate(grid):
        for cell in enumerate(row[1]):
            if cell[1]["is_full"]:
                increment_neighbors(grid, row[0], cell[0])


def get_accessible_rolls(grid: list[list[dict[str, int | bool]]]) -> int:
    build_adjacency_weightings(grid)

    accessible_rolls = 0

    for row in grid:
        for cell in row:
            accessible_rolls += (
                1 if cell["neighbor_count"] < 4 and cell["is_full"] else 0
            )

    return accessible_rolls


def decrement_neighbors(
    grid: list[list[dict[str, int | bool]]], row: int, col: int
) -> None:
    for r in range(max(0, row - 1), min(len(grid), row + 2)):
        for c in range(max(0, col - 1), min(len(grid[0]), col + 2)):
            if grid[r][c]["is_full"] and (r != row or c != col):
                grid[r][c]["neighbor_count"] -= 1


def get_accessible_rolls_recursive(grid: list[list[dict[str, int | bool]]]) -> int:
    build_adjacency_weightings(grid)
    total_accessible_rolls = 0
    pass_num = 0

    while True:
        accessible_rolls = 0

        for row in enumerate(grid):
            for cell in enumerate(row[1]):
                if cell[1]["neighbor_count"] < 4 and cell[1]["is_full"]:
                    accessible_rolls += 1
                    cell[1]["is_full"] = False
                    decrement_neighbors(grid, row[0], cell[0])

        if accessible_rolls == 0:
            break
        else:
            print(f"Pass {pass_num} found {accessible_rolls} accessible rolls.")
            pass_num += 1

            total_accessible_rolls += accessible_rolls

    return total_accessible_rolls


def main():
    data = parse_input()

    print(f"Number of accessible rolls: {get_accessible_rolls(data)}\n")

    data = parse_input()

    print(
        f"Total number of accessible rolls (recursive): {get_accessible_rolls_recursive(data)}"
    )


if __name__ == "__main__":
    main()
