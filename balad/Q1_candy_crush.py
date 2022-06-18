"""
Candy Crush.
In the first line an integer 'n' will be given which indicates that
in the next n lines there will be n row of n numbers (n^2 total).
The output should be all the n numbers in order of sub-diameter of the
matrix.

sample input:
4
1 6 3 10
2 5 9 13
4 8 12 15
7 11 14 16

accepted output:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

passed: 100%
"""


def get_number_of_iterations(n) -> int:
    number_list = {1: 1, 2: 3}
    for i in range(1, n):
        number_list[i + 2] = 2 * i + 3
    return number_list[n]


def re_order_main(list_of_lists) -> list:
    iterations = get_number_of_iterations(len(list_of_lists))
    numbers_list = {}
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            numbers_list[(i, j)] = list_of_lists[i][j]
    final_list = []
    for i in range(iterations):
        keys_summed_in_i = [key for key in numbers_list.keys() if key[0] + key[1] == i]
        # sort values by the first element of the key
        keys_summed_in_i.sort(key=lambda x: x[0], reverse=True)
        final_list += [numbers_list[key] for key in keys_summed_in_i]
    return final_list


if __name__ == "__main__":
    row_col_count = int(input())
    numbers = [input().split() for i in range(row_col_count)]

    # re-order the list of lists
    result = re_order_main(numbers)
    print(" ".join(result))
