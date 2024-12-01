def main():
    left_list, right_list = [], []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)

    return sum(abs(a - b) for a, b in zip(sorted_left, sorted_right))

print(main())

# 3246517