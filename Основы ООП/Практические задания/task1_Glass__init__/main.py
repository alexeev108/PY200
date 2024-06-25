from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        ...  # TODO инициализировать объект "Стакан"

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Ошибка типа. Capacity volume должен быть int или float")
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Ошибка типа. Occupied volume должен быть int или float")
        if capacity_volume < 0:
            raise ValueError("Ошибка значения. Стакан не может иметь отрицательный объем")
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError("Ошибка значения. "
                             "Occupied volume не может быть отрицательным числом"
                             " и не может быть больше Capacity volume")

        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __repr__(self):
        return f'Glass({self.capacity_volume}, {self.occupied_volume})'

if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass
    glass1 = Glass(300, 200)
    # glass1 = Glass('f', 3)
    print(glass1)



    # TODO попробовать инициализировать не корректные объекты
