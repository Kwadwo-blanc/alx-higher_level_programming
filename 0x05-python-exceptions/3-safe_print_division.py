#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): Dividend.
        b (int): Divisor.

    Returns:
        float or None: The result of the division,
        or None if an exception occurs.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    except TypeError:
        return None
    else:
        print("Inside result: {}".format(result))
    finally:
        return result if 'result' in locals() else None
