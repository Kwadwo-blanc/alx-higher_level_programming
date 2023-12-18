#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    Args:
        my_list (list): List containing elements of any type.
        x (int): Number of elements to print.
    Returns:
        int: The real number of elements printed.
    """
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
