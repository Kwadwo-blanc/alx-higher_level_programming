#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers of a list.

    Args:
        my_list (list): List containing elements of any type.
        x (int): Number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end="")
                count += 1
        print()
    except (IndexError, ValueError, TypeError):
        pass

    return count
