from typing import List

def read_input_file() -> None:
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            left_value, right_value = map(int, line.split())
            left_values.append(left_value)
            right_values.append(right_value)


def calculate_digit_difference(left: List[int], right: List[int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def calculate_similarity_score(left: List[int], right: List[int]) -> int:
    right_value_counts = {}
    for value in right:
        right_value_counts[value] = right_value_counts.get(value, 0) + 1
    total = 0
    for value in left:
        total += value * right_value_counts.get(value, 0)
    return total


def main() -> str:
    read_input_file()
    sorted_left_values = sorted(left_values)
    sorted_right_values = sorted(right_values)
    digit_difference_value = calculate_digit_difference(sorted_left_values, sorted_right_values)
    similarity_score_value = calculate_similarity_score(sorted_left_values, sorted_right_values)
    return f"Side by side sum: {digit_difference_value}\nSimilarity score: {similarity_score_value}"


left_values: List[int] = []
right_values: List[int] = []

print(main())