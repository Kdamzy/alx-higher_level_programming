#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    add_sum = 0
    for a in range(x):
        try:
            print(f"{my_list[a]}", end="")
            add_sum += 1
        except IndexError:
            break
    print()
    return(add_sum)
