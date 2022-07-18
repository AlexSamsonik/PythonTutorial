"""
This is provides example of usage __slots__ for increase performance with get, set and delete property on the object.
"""
from __future__ import annotations

import timeit
from functools import partial


class Person:
    """There is simple Person class."""

    def __init__(self, name: str, surname: str, address: str, email: str):
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email


class PersonSlots:
    """There is simple Person class but use __slots__."""
    __slots__ = "name", "surname", "address", "email"

    def __init__(self, name: str, surname: str, address: str, email: str):
        self.name = name
        self.surname = surname
        self.address = address
        self.email = email


def get_set_delete(person: Person | PersonSlots):
    """
    Function with set, get and delete address on Person or PersonSlots classes.
    :param person: Person | PersonSlots object.
    """

    person.address = "Main St"
    _ = person.address
    del person.address


def main():
    """Script which check difference between used and unused __slots__."""
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
