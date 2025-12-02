def parse_input() -> list:
    with open("Day 2/input.txt") as file:
        contents = file.read().split(",")
        for range in contents:
            range.split("-")
    
def main():
    ranges = parse_input()

if __name__ == "__main__":
    main()