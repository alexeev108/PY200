class Automobile:
    """ Базовый класс автомобиля. """
    def __init__(self, name: str, country: str):
        self.__name = self.__get_valid_name(name)
        self.__country = self.__get_valid_country(country)
        self.country_prod = self.country_of_production(country)

    def __get_valid_name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'Переменная name должна быть типа str, а ввели тип {type(name)}')
        return name

    def __get_valid_country(self, country):
        if not isinstance(country, str):
            raise TypeError(f'Переменная country должна быть типа str, а ввели тип {type(country)}')
        return country

    def country_of_production(self, country):
        self.country_prod = self.__get_valid_country(country)
        return self.country_prod

    def __str__(self):
        return f"Автомобиль {self.__name}. Страна происхождения {self.__country}. Страна производства {self.country_prod}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, country={self.__country!r})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country

class Light(Automobile):
    def __init__(self, name: str, author: str, weight: float):
        super().__init__(name, author)
        self.weight = self.get_valid_weight(weight)

    def get_valid_weight(self, weight):
        """
        Валидация веса легковой машины
        """
        if not isinstance(weight, float):
            raise TypeError(f'Переменная weight должна быть типа int, а ввели тип {type(weight)}')
        if weight < 0:
            raise ValueError(f'Переменная weight должна быть больше 0')
        return weight

    def __str__(self):
        return super().__str__() + f". Вес легковой машины {self.weight!r}"

class Heavy(Automobile):
    def __init__(self, name: str, author: str, weight_to_get: float):
        super().__init__(name, author)
        self.weight_to_get = weight_to_get

    @property
    def weight_to_get(self):
        return self._weight_to_get

    @weight_to_get.setter
    def weight_to_get(self, weight_to_get):
        self._weight_to_get = self.get_valid_weight_to_get(weight_to_get)

    def get_valid_weight_to_get(self, weight_to_get):
        """
        Валидация груза на борту
        """
        if not isinstance(weight_to_get, float):
            raise TypeError(f'Переменная weight_to_get должна быть типа int, а ввели тип {type(weight_to_get)}')
        if weight_to_get < 0:
            raise ValueError(f'Переменная pages должна быть больше 0')
        return weight_to_get

    def country_of_production(self, country_of_production: str):
        """
        Грузовые автомобили производятся в стране, отличной от страны происхождения
        :param country_of_production: страна, отличная от страны происхождения
        :return: страна производства
        """
        self.country_prod = super().country_of_production(country_of_production)
        return self.country_prod

    def __str__(self):
        return super().__str__() + f". Груз на борту {self.weight_to_get!r}"

if __name__ == '__main__':
    auto = Automobile('bmw', 'germany')
    print(auto)
    auto1 = Light('mazda', 'japan', 1500.1)
    print(auto1)
    auto2 = Heavy('volvo', 'sweden', 10000.0)
    print(auto2)
    auto2.country_of_production('china')
    print(auto2)
