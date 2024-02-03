#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from abc import ABC, abstractmethod


class Triad(ABC):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    @abstractmethod
    def increase(self) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

    @abstractmethod
    def compare(self, other: Triad) -> str:
        pass


class Date(Triad):
    def __init__(self, day: int, month: int, year: int):
        super().__init__(day, month, year)

    def increase(self) -> None:
        self.a += 1
        self.b += 1
        self.c += 1

    def display(self) -> None:
        print(f"Дата: {self.a}/{self.b}/{self.c}")

    def compare(self, other: Triad) -> str:
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return "Даты равны"
        else:
            return "Даты не равны"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return (self.a, self.b, self.c) == (other.a, other.b, other.c)

    def __gt__(self, other: Date) -> bool:
        return (self.c, self.b, self.a) > (other.c, other.b, other.a)

    def __lt__(self, other: Date) -> bool:
        return (self.c, self.b, self.a) < (other.c, other.b, other.a)

    def __ge__(self, other: Date) -> bool:
        return (self.c, self.b, self.a) >= (other.c, other.b, other.a)

    def __le__(self, other: Date) -> bool:
        return (self.c, self.b, self.a) <= (other.c, other.b, other.a)

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return (self.a, self.b, self.c) != (other.a, other.b, other.c)


if __name__ == '__main__':
    date1 = Date(17, 3, 2001)

    date1.display()
    date1.increase()
    date1.display()

    date2 = Date(17, 3, 2001)
    print(date1.compare(Date(17, 3, 2001)))

    print(date1 == date2)
    print(date1 > date2)
    print(date1 < date2)
    print(date1 >= date2)
    print(date1 <= date2)
    print(date1 != date2)
