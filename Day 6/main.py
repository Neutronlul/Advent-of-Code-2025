def parse_input(input_file: str) -> list[dict[str, str | list[int]]]:
    with open(input_file) as file:
        lines = file.readlines()
        lines = [line.split() for line in lines]
        return [
            {
                "operator": lines[-1][i],
                "operands": [int(line[i]) for line in lines[:-1]],
            }
            for i in range(len(lines[-1]))
        ]


def parse_input_2(input_file: str) -> list[dict[str, str | list[int]]]:
    with open(input_file) as file:
        lines = file.readlines()
        data = []
        operands = []
        current_op = ""

        for i, operator in enumerate(lines[-1]):
            if operator != " ":
                current_op = operator

            num = ""
            for line in lines[:-1]:
                num += line[i]

            if i == len(lines[-1]) - 1:
                operands.append(num.strip())

            if num.strip() == "" or i == len(lines[-1]) - 1:
                data.append({"operator": current_op, "operands": operands})
                operands = []
            else:
                operands.append(num.strip())

        return data


def sum_worksheet(data: list[dict[str, str | list[int]]]) -> int:
    total = 0
    for column in data:
        sum = 0
        if column["operator"] == "*":
            sum = 1
            for operand in column["operands"]:
                sum *= int(operand)
            total += sum
        else:
            for operand in column["operands"]:
                sum += int(operand)
            total += sum
    return total


def main():
    test_data = parse_input("Day 6/sample.txt")

    assert sum_worksheet(test_data) == 4277556

    test_data = parse_input_2("Day 6/sample.txt")

    result = sum_worksheet(test_data)
    assert result == 3263827, f"Expected 3263827 but got {result}"

    data = parse_input("Day 6/input.txt")

    print(sum_worksheet(data))

    data = parse_input_2("Day 6/input.txt")

    print(sum_worksheet(data))


if __name__ == "__main__":
    main()
