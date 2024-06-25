class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        return False

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if cls.is_leap_year(year):
            days = cls.DAY_OF_MONTH[-1]
        else:
            days = cls.DAY_OF_MONTH[0]
        return days[month - 1]
          # TODO используя атрибут класса DAY_OF_MONTH вернуть количество дней в запрашиваемом месяце и году

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
          # TODO проверить валидность даты
        if not isinstance(day, int):
            raise ValueError('Некорректный формат day')
        if not isinstance(month, int):
            raise ValueError('Некорректный формат month')
        if not isinstance(year, int):
            raise ValueError('Некорректный формат year')
        if day < 1 or month < 1 or month > 12 or day > 31:
            raise ValueError('Ошибка в значении для day, month, year')
        max_day = self.get_max_day(month, year)
        if day > max_day:
            raise ValueError('Ошибка в значении для day')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.day}, {self.month}, {self.year})'

if __name__ == '__main__':
    date = Date(28, 2, 2023)
    print(date)
    print(Date(29, 2, 2023))
