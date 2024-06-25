from typing import Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "У лукоморья",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "Евгений Онегин",
        "pages": 400,
    },
    {
        "id": 3,
        "name": "Полтава",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, int):
            raise ValueError('Ошибка значения. Параметр id_ должен быть int')
        self.id_ = id_
        if not isinstance(name, str):
            raise ValueError('Ошибка значения. Параметр name должен быть str')
        self.name = name
        if not isinstance(pages, int):
            raise ValueError('Ошибка значения. Параметр pages должен быть int')
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name!r}, pages={self.pages!r})'


# TODO написать класс Library
class Library:
    def __init__(self, books: Optional[list] = None):
        if books is None:
            self.books = []
        elif not isinstance(books, list):
            raise TypeError('Переменная books должен быть типом list')
        else:
            self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, id_: int):
        if not isinstance(id_, int):
            raise ValueError('Переменная id_ Должна быть типа int')
        else:
            for index, item in enumerate(self.books):
                if item.id_ != id_:
                    continue
                else:
                    return index
            raise ValueError('Книги с запрашиваемым id не существует')

    def __str__(self):
        return f'Книги в библиотеке: {self.books}'


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    # for book in list_books:
    #     print(book)  # проверяем метод __str__
    #
    # print(list_books)  # проверяем метод __repr__

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами

    print(library_with_books)

    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    #
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
