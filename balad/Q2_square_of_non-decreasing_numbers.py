"""
Square of Non-decreasing Numbers.
In the first line an integer 'n' will be given which indicates
how many numbers will appear in the next line.
Second line will be a list of non-decreasing numbers.

sample input:
4
-9 -8 -5 -3 1 2 4 7 9

accepted output:
1 4 9 16 25 49 64 81 81

passed: not tested yet.
"""


def get_sorted_square(num_list) -> list:
    """Considering the list is already sorted,
    pointer is used to go through the list."""
    n = len(num_list)
    left, right = 0, n - 1
    index = n - 1
    squared = []

    while index >= 0:
        if abs(num_list[left]) <= abs(num_list[right]):
            squared.insert(0, num_list[right] * num_list[right])
            right -= 1
        else:
            squared.insert(0, num_list[left] * num_list[left])
            left += 1
        index -= 1

    return list(map(str, squared))


if __name__ == "__main__":
    _ = input()
    numbers = list(map(int, input().rstrip().split(" ")))
    result = get_sorted_square(num_list=numbers)
    print(" ".join(result))
