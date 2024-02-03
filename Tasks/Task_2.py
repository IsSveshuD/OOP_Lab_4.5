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


class Date(Triad):
    def __init__(self, day: int, month: int, year: int):
        super().__init__(day, month, year)

    def increase(self) -> None:
        self.a += 1
        self.b += 1
        self.c += 1

    def display(self) -> None:
        print(f"Дата: {self.a}/{self.b}/{self.c}")


class Time(Triad):
    def __init__(self, hour: int, minute: int, second: int):
        super().__init__(hour, minute, second)

    def increase(self) -> None:
        self.a += 1
        self.b += 1
        self.c += 1

    def display(self) -> None:
        print(f"Время: {self.a}:{self.b}:{self.c}")


if __name__ == '__main__':
    date: Date = Date(17, 3, 2001)
    time: Time = Time(12, 30, 45)

    date.display()
    date.increase()
    date.display()

    time.display()
    time.increase()
    time.display()
