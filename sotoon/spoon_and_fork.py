from pprint import pprint

if __name__ == '__main__':

    plates_count = int(input())
    sf_string = input()
    plates = {p: {"left": None, "right": None} for p in range(0, plates_count)}
    for index, sp in enumerate(sf_string):
        if sp in ["s", "p"]:
            pass
        else:
            plate = index % plates_count
            placement = "left" if sp == "F" else "right"
            if plates[plate][placement] is not None:
                placement = "right" if placement == "left" else "left"
            plates[plate][placement] = sp

    # pprint(plates)

    final_states = []
    for plate, sf in plates.items():
        if sf["left"] == sf["right"] and sf["left"] is not None:
            final_states.append(False)
        else:
            final_states.append(True)

    # print(final_states)
    print("YES" if all(final_states) else "NO")
