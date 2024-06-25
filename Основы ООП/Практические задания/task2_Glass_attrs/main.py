from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume  # объем стакана

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume  # объем жидкости в стакане

    def copy(self):
        return Glass(self.capacity_volume, self.occupied_volume)

    def add_volume(self, new_volume):
        if not isinstance(new_volume, (int, float)):
            raise TypeError
        if new_volume < 0 or new_volume + self.occupied_volume > self.capacity_volume:
            raise ValueError
        self.occupied_volume += new_volume

    def remove_volume(self, volume_for_remove):
        if not isinstance(volume_for_remove, (int, float)):
            raise TypeError
        if volume_for_remove < 0 or volume_for_remove > self.occupied_volume:
            raise ValueError
        self.occupied_volume -= volume_for_remove

if __name__ == "__main__":
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.capacity_volume, glass1.occupied_volume)

    glass2 = glass1.copy()  # TODO инициализировать ещё один стакан
    print(glass2.capacity_volume, glass2.occupied_volume)  # TODO распечатать атрибуты экземпляра glass2

    print("Доливаем воды в первый стакан...")
    #  TODO доливаем воды в первый стакан
    glass1.add_volume(50)
    print(glass1.capacity_volume, glass1.occupied_volume)
    print(glass2.capacity_volume, glass2.occupied_volume)
    print("Выливаем воду из второго стакана...")
    glass2.remove_volume(10)
    print(glass1.capacity_volume, glass1.occupied_volume)
    print(glass2.capacity_volume, glass2.occupied_volume)
    #  TODO сравнить id объектов
    print(glass1 is glass2)
