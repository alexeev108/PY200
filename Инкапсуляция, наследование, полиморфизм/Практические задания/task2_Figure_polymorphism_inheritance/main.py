import math


class Figure:
    """ Базовый класс. """

    def area(self):
        print(f"Вызван метод класса {self.__class__.__name__}")
        return None


class Rectangle(Figure):
    """ Производный класс. Прямоугольник. """

    ...  # TODO определить конструктор и перегрузить метод area
    def __init__(self, a, b):
        if not isinstance(a, (int, float)):
            raise TypeError('a должно быть int или float')
        if not isinstance(b, (int, float)):
            raise TypeError('b должно быть int или float')
        if a < 0 or b < 0:
            raise ValueError('Недопустимое значение')
        self.a = a
        self.b = b
    def area(self):
        super().area()
        return self.a * self.b


class Circle(Figure):
    """ Производный класс. Круг. """

    ...  # TODO определить конструктор и перегрузить метод area
    def __init__(self, rad):
        if not isinstance(rad, (int, float)):
            raise TypeError('rad должно быть int или float')
        if rad < 0:
            raise ValueError('Недопустимое значение')
        self.rad = rad

    def area(self):
        super().area()
        return math.pi * self.rad**2


if __name__ == "__main__":
    fig = Figure()
    fig.area()

    rect = Rectangle(5, 10)
    rect.area()

    circle = Circle(5)
    circle.area()
