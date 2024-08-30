from abc import ABC, abstractmethod
from math import pi, sqrt


class Area(ABC):

    def __init__(self, *args):
        self.__args = args

    @property
    def args(self):
        return self.__args

    @abstractmethod
    def area(self):
        pass


class Circle(Area):

    def area(self):
        return pi * super().args[0] * super().args[0]


class Rectangle(Area):

    def area(self):
        return super().args[0] * super().args[1]


class Triangle(Area):

    def area(self):
        p = (super().args[0] + super().args[1] + super().args[2]) / 2
        return sqrt(p * (p - super().args[0]) * (p - super().args[1]) * (p - super().args[2]))


if __name__ == "__main__":
    print(Circle(5).area())
    print(Rectangle(5, 6).area())
    print(Triangle(5, 6, 8).area())
