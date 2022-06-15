"""
This code is answer to 'https://quera.org/problemset/145009/'
passed: 58%
"""


def walk_through(target_number, possible_inputs):
    action_counter = 0
    possible_inputs = {digit[0]: digit for digit in possible_inputs}
    while len(target_number) > 0:
        digit = target_number[0]
        entered_value = possible_inputs[digit]
        length = len(entered_value)
        action_counter += 1
        go_next = False
        while not go_next:
            if entered_value[:length] == target_number[:length]:
                target_number = target_number[length:]
                go_next = True
            else:
                length -= 1
                action_counter += 1

    return action_counter


def find_biggest_sub(target_number, possible_inputs):
    subsets_in_target = [key for key in possible_inputs if key in target_number]
    action_counter = 0
    while len(subsets_in_target) > 0:
        subsets_in_target = sorted(subsets_in_target)
        biggest_sub = subsets_in_target.pop(0)
        target_number = target_number.replace(biggest_sub, "", 1)
        action_counter += 1
        subsets_in_target = [sub for sub in subsets_in_target if sub in target_number]

    if len(target_number) > 0:
        action_counter += walk_through(
            target_number=target_number, possible_inputs=possible_inputs
        )

    return action_counter


if __name__ == "__main__":

    target = input()
    key_results = [input() for _ in range(10)]
    # target = "18415"
    # key_results = ["0", "16", "2", "3", "415", "59", "6", "7", "84", "9"]

    res_walk_through_improved = find_biggest_sub(
        target_number=target, possible_inputs=key_results
    )

    print(res_walk_through_improved)
