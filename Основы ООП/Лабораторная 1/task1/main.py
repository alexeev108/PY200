# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class Pizza:
    def __init__(self,
                 tomatoe: Union[int, float],
                 cheese: Union[int, float],
                 meat: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Пицца"
        :param tomatoe: Ингредиент "Томаты" в граммах
        :param cheese: Ингредиент "Сыр" в граммах
        :param meat: Ингредиент "Мясо" в граммах

        Примеры:
        >>> pizza = Pizza(100, 200, 300)
        """
        if not isinstance(tomatoe, (int, float)):
            raise TypeError("Ошибка типа. Tomatoe должен быть int или float")
        if not isinstance(cheese, (int, float)):
            raise TypeError("Ошибка типа. Cheese должен быть int или float")
        if not isinstance(meat, (int, float)):
            raise TypeError("Ошибка типа. Meat должен быть int или float")
        if tomatoe < 0 or cheese < 0 or meat < 0:
            raise ValueError("Ошибка значения. Число не может быть меньше 0")

        self.tomatoe = tomatoe
        self.cheese = cheese
        self.meat = meat

    def add_tomatoe(self, tomatoe_add):
        """
        Функция, которая добавляет количество помидоров в граммах
        :param tomatoe_add: вес добавляемого продукта
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> pizza = Pizza(100, 200, 300)
        >>> pizza.add_tomatoe(50)
        """
        if not isinstance(tomatoe_add, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if tomatoe_add < 0:
            raise ValueError("Введенное значение должно быть положительным числом")
        self.tomatoe += tomatoe_add

    def remove_tomatoe(self, tomatoe_delete):
        """
        Функция, которая удаляет количество помидоров в граммах
        :param tomatoe_delete: вес добавляемого продукта
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> pizza = Pizza(100, 200, 300)
        >>> pizza.remove_tomatoe(100)
        """
        if not isinstance(tomatoe_delete, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if (tomatoe_delete < 0) or (self.tomatoe - tomatoe_delete < 0):
            raise ValueError("Введенное значение должно быть положительным числом и меньше tomatoe")
        self.tomatoe -= tomatoe_delete

    def add_cheese(self, cheese_add):
        """
        Функция, которая добавляет количество сыра в граммах
        :param cheese_add: вес добавляемого продукта
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> pizza = Pizza(100, 200, 300)
        >>> pizza.add_cheese(50)
        """
        if not isinstance(cheese_add, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if cheese_add < 0:
            raise ValueError("Введенное значение должно быть положительным числом")
        self.cheese += cheese_add

    def remove_cheese(self, cheese_delete):
        """
        Функция, которая удаляет количество сыра в граммах
        :param cheese_delete: вес добавляемого продукта
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> pizza = Pizza(100, 200, 300)
        >>> pizza.remove_cheese(100)
        """
        if not isinstance(cheese_delete, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if cheese_delete < 0:
            raise ValueError("Введенное значение должно быть положительным числом")
        self.cheese -= cheese_delete

    def add_meat(self, meat_add):
        """
        Функция, которая добавляет количество мяса в граммах
        :param meat_add: вес добавляемого продукта
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> pizza = Pizza(100, 200, 300)
        >>> pizza.add_meat(50)
        """
        if not isinstance(meat_add, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if meat_add < 0:
            raise ValueError("Введенное значение должно быть положительным числом")
        self.meat += meat_add

    def remove_meat(self, meat_delete):
        """
        Функция, которая удаляет количество мяса в граммах
        :param meat_delete: вес добавляемого продукта
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> pizza = Pizza(100, 200, 300)
        >>> pizza.remove_meat(100)
        """
        if not isinstance(meat_delete, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if meat_delete < 0:
            raise ValueError("Введенное значение должно быть положительным числом")
        self.cheese -= meat_delete

class Rectangle:
    def __init__(self, a: Union[int, float], b: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Прямоугольник"
        :param a: сторона прямоугольника a в мм
        :param b: сторона прямоугольника b в мм

        Примеры:
        >>> rectangle = Rectangle(100, 200)
        """
        if not isinstance(a, (int, float)):
            raise TypeError("Ошибка типа. Сторона a должна быть int или float")
        if not isinstance(b, (int, float)):
            raise TypeError("Ошибка типа. Сторона b должна быть int или float")
        if a < 0 or b < 0:
            raise ValueError("Ошибка значения. Число не может быть меньше 0")
        self.a = a
        self.b = b

    def perimeter(self):
        """
        Функция вычисляет периметр прямоугольника
        :return: Периметр прямоугольника в мм
        >>> rectangle = Rectangle(100, 200)
        >>> x = rectangle.perimeter()
        """
        perimeter = 2 * self.a + 2 * self.b
        return perimeter

    def square(self):
        """
        Функция вычисляет площадь прямоугольника
        :return: Площадь прямоугольника в мм2
        >>> rectangle = Rectangle(100, 200)
        >>> x = rectangle.square()
        """
        square = self.a * self.b
        return square

class Vkontakte:
    def __init__(self, foto: int, music: int):
        if not isinstance(foto, int):
            raise TypeError("Ошибка типа. Количество фото должно быть int")
        if not isinstance(music, int):
            raise TypeError("Ошибка типа. Количество музыкальных треков должно быть int")
        self.foto = foto
        self.music = music

    def add_foto(self, foto_quantity):
        """
        Функция, которая добавляет количество фото
        :param foto_quantity: количество добавляемых фото
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> vkontakte = Vkontakte(100, 200)
        >>> vkontakte.add_foto(50)
        """
        if not isinstance(foto_quantity, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if foto_quantity < 0:
            raise ValueError("Введенное значение должно быть положительным числом")
        self.foto += foto_quantity

    def add_music(self, music_quantity):
        """
        Функция, которая добавляет количество музыкальных треков
        :param music_quantity: количество музыкальных треков
        :raise ValueError: если значение меньше 0, то вызываем ошибку

        Примеры:
        >>> vkontakte = Vkontakte(100, 200)
        >>> vkontakte.add_music(50)
        """
        if not isinstance(music_quantity, (int, float)):
            raise TypeError("Введенное значение должно быть типа int или float")
        if music_quantity < 0:
            raise ValueError("Введенное значение должно быть положительным числом")
        self.music += music_quantity


if __name__ == "__main__":
    pizza1 = Pizza(100, 200, 300)
    doctest.testmod()

    print(pizza1.tomatoe)
    pizza1.add_tomatoe(100)
    print(pizza1.tomatoe)
    pizza1.remove_tomatoe(30)
    print(pizza1.tomatoe)

    rectangle1 = Rectangle(100, 200)
    print(f'Периметр: {rectangle1.perimeter()} мм')
    print(f'Площадь: {rectangle1.square()} мм2')

    vkontakte1 = Vkontakte(100, 200)
    print(vkontakte1.foto)
    vkontakte1.add_foto(200)
    print(vkontakte1.foto)
