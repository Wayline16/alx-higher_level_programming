#!/usr/bin/python3
for number in range(0,10):
    for j in range(1, 10):
        if number >= j:
            continue
        elif number == 8 and j == 9:
            print("{}{}".format(number, j))
        else:
            print("{}{}, ".format(number, j), end="")
