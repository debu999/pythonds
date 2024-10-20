"""
This module contains functions for printing and manipulating 2D ranges of integers.

Functions:
    print_items(n) -> None: Prints integers from 0 to n-1.
    print_items_2d(n) -> None: Prints all pairs of integers (i, j) such that 0 <= i < n and 0 <= j < n.

"""

import itertools
from pprint import pp

pp("hello world python ds.")


def print_items(n: int):
    """Prints integers from 0 to n-1.

    This function generates a sequence of integers starting from 0 up to, but not including, n.
    Each integer is printed using the pp function, allowing for easy visualization of the range.

    Args:
        n (int): The upper limit (exclusive) for the range of integers to print.

    Returns:
        None
    """
    for i in range(n):
        pp(i)


def print_items_2d(n: int):
    """
    Prints all pairs of integers (i, j) such that 0 <= i < n and 0 <= j < n.

    This function generates a sequence of pairs of integers, where each pair represents
    the coordinates of a point on a grid. The range of each coordinate is from 0 to,ff              dfgadˀˀˀ
    but not including, n.

    Args:
        n (int): The upper limit (exclusive) for the range of integers to print.

    Returns:
        None
    """
    for i, j in itertools.product(range(n), range(n)):
        pp(f"{i} {j}")


if __name__ == "__main__":
    print_items_2d(10)
    pp("done")
