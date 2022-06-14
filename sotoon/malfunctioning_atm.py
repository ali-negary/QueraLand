"""
This code is answer to 'https://quera.org/problemset/145009/'
passed: 55%
"""

from copy import deepcopy

if __name__ == "__main__":

    target_number = input()
    possible_inputs = [input() for _ in range(10)]
    # target_number = "18415"
    # possible_inputs = ["0", "16", "2", "3", "415", "59", "6", "7", "84", "9"]

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
            wait = "here"

    print(action_counter)
