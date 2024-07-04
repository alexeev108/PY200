class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.__name = self.__get_valid_name(name)
        self.__author = self.__get_valid_author(author)

    def __get_valid_name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'Переменная name должна быть типа str, а ввели тип {type(name)}')
        return name

    def __get_valid_author(self, author):
        if not isinstance(author, str):
            raise TypeError(f'Переменная author должна быть типа str, а ввели тип {type(author)}')
        return author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name!r}, author={self.__author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = self.get_valid_pages(pages)

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, duration):
        self._pages = self.get_valid_pages(duration)

    def get_valid_pages(self, pages):
        if not isinstance(pages, int):
            raise TypeError(f'Переменная pages должна быть типа int, а ввели тип {type(pages)}')
        if pages < 0:
            raise ValueError(f'Переменная pages должна быть больше 0')
        return pages

    def __str__(self):
        return super().__str__() + f". Количество страниц {self.pages!r}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = self.get_valid_duration(duration)

    def get_valid_duration(self, duration):
        if not isinstance(duration, float):
            raise TypeError(f'Переменная pages должна быть типа int, а ввели тип {type(duration)}')
        if duration < 0:
            raise ValueError(f'Переменная pages должна быть больше 0')
        return duration

    def __str__(self):
        return super().__str__() + f". Длительность {self.duration!r}"

if __name__ == '__main__':
    paper = PaperBook('GH', 'uh', 90)
    print(paper)
    audio = AudioBook('dhdb', 'ghfb', 45.0)
    print(audio)