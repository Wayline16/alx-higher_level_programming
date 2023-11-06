#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        exit()
    elif idx > len(my_list):
        exit()
    return my_list[idx]
