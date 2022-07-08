"""
There are docstring...
"""
from __future__ import annotations

import timeit
from functools import partial


class Person:
    """
    There are docstring
    """

    def __init__(self, name: str, surname: str, address: str, email: str):
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email


class PersonSlots:
    """
    There are docstring
    """
    __slots__ = "name", "surname", "address", "email"

    def __init__(self, name: str, surname: str, address: str, email: str):
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email


def get_set_delete(person: Person | PersonSlots):
    """

    :param person:
    :return:
    """

    person.address = "Main St"
    _ = person.address
    del person.address


def main():
    """

    :return:
    """
    person = Person("Dane", "Stone", "Boston", "dane.stone@gmail.com")
    person_slots = PersonSlots("Dane", "Stone", "Boston", "dane.stone@gmail.com")
    number = 1_000_000
    no_slots = min(timeit.repeat(partial(get_set_delete, person), number=number))
    slots = min(timeit.repeat(partial(get_set_delete, person_slots), number=number))
    print(f"No slots: {no_slots}")
    print(f"Slots: {slots}")
    print(f"Performance improvement: {1 - slots / no_slots:.2%}")


if __name__ == '__main__':
    main()
