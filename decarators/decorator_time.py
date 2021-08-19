"""Simple example to use decorator to count time execution for function."""

from datetime import datetime
from typing import List


def count_time(arg):
    """Decorator to count time execution for function.

    :param arg: Param for decorator.
    """

    def other(func):
        def wrapper(*args):
            print(arg, end=" -> ")
            start = datetime.now()
            result = func(*args)
            print(datetime.now() - start)
            return result

        return wrapper

    return other


@count_time("Create even list by for loop")
def get_even_list_by_for(max_range: int) -> List[int]:
    """Function which generate list with even numbers use for loop.

    :param max_range: param which use in range() like max number.
    :return: List with even numbers
    """
    even_list = []
    for n in range(max_range):
        if n % 2 == 0:
            even_list.append(n)
    return even_list


@count_time("Create even list by list comprehension")
def get_even_list_by_generator(max_range: int) -> List[int]:
    """Function which generate list with even numbers use list comprehension.

    :param max_range: param which use in range() like max number.
    :return: List with even numbers
    """
    return [n for n in range(max_range) if n % 2 == 0]


if __name__ == '__main__':
    m = 10 ** 8
    get_even_list_by_for(m)
    get_even_list_by_generator(m)
