#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
     """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """

    count = 0
    for i in my_list:
        try:
            if count < x:
                print(i, end="")
                count += 1
            else:
                break
            except:
                pass
            print()
            return count
