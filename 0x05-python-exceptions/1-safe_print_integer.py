#!/usr/bin/python3


def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format().

    Args:
        value: Any type (integer, string, etc.).

    Returns:
        bool: True if value is an integer and has been correctly printed,
        False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
