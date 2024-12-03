import re


def regex_search(data: str) -> list:
    regex = r"\w*(mul)\W+(\d+)+[,]+(\d+)+\)"
    matches = re.findall(regex, data)
    return [[int(num) for num in match if num.isdigit()] for match in matches]


def calculate_total_sum(data: list[tuple[int, int]]) -> int:
    if not data:
        return 0
    total_sum = sum(x * y for x, y in data)
    return total_sum


COMBINED_REGEX = r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))"

combined_pattern = re.compile(COMBINED_REGEX)

def second_part_data_splitter(data: str) -> int:
    is_multiplication_enabled = True
    total_sum = 0
    for match in combined_pattern.finditer(data):
        token = match.group()
        if token == "do()":
            is_multiplication_enabled = True
        elif token == "don't()":
            is_multiplication_enabled = False
        else:
            x, y = map(int, match.groups()[:2])
            if is_multiplication_enabled:
                total_sum += x * y
    return total_sum


def main() -> None:
    with open("input.txt") as file:
        data = file.read()
    formatted_data = regex_search(data)
    print(
        f"Part 1: {calculate_total_sum(formatted_data)}\nPart 2: {second_part_data_splitter(data)}"
    )


if __name__ == "__main__":
    main()