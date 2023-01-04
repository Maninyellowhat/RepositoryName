# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union

class Table:
    """
    Документация на класс
    Класс описывает модель стола
    """
    def __int__(self, cost: Union[int, float], height: Union[int, float]):
        """
        Cоздание и подготовка к работе объекта "Table"

        :param cost: стоимость стола
        :param height: высота стола

        Примеры:
        >>> table = Table(5000, 20) # инициализация экземпляра класса
        """
        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость стола должна быть типа int или float")
        if not cost > 0: # проверяем, что cтоимость не отрицательная
            raise ValueError("Стоимость должна быть положительным числом")
        self.cost = cost
        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть типа int или float")
        if not height >= 0: # проверяем, что длина не отрицательная
            raise ValueError("Высота должна быть больше нуля")
        self.height = height

    def Raising_the_praise(self, raising_cost: Union[int,float]):
        """
        Метод увеличивает стоимомь стола.
        :param raising_cost: То, на сколько выросла стоимость стола

        Примеры:
        >>> table = Table(5000, 20)
        >>> table.Raising_the_praise(1000)
        """
        if not isinstance(raising_cost, (int, float)): # проверяем, что добавочная стоимость тпа int или float
            raise TypeError # вызываем ошибку
        if not raising_cost > 0:  # проверяем, что cтоимость не отрицательная
            raise ValueError
        ...

    def low_the_praise (self, low_cost: Union[int,float]):
        """
        Метод уменьшает стоимомь стола.
        :param low_cost: То, на сколько снизилась стоимость стола

        Примеры:
        >>> table = Table(5000, 100)
        >>> table.low_the_praise(1000)
        """
        if not isinstance(low_cost, (int, float)): # проверяем, что скидка типа int или float
            raise TypeError # вызываем ошибку
        if low_cost > self.cost: # проверяем, что размер скидки не больше изначальной стоимости
            raise ValueError
        if low_cost < 0:  # проверяем, что cтоимость не отрицательная
            raise ValueError
        ...

if __name__ == "__main__":
    doctest.testmod() #тестирование примеров, которые находятся в документации






    class Cats:
        """
        Документация на класс
        Класс описывает модель кошки
        """

        def __int__(self, tale: bool, color: str, ):
            """
            Cоздание и подготовка к работе объекта "Cats"

            :param tale: наличие хвоста
            :param color: цвет кошки

            Примеры:
            >>> cats = Cats(True, "black") # инициализация экземпляра класса
            """

            self.color = color
            self.tale = tale

        def Changing_color(self, new_color: str):
            """
            Метод изменяет цвет кошки.
            :param new_color: То, на какой цвет проводится замена

            Примеры:
            >>> cats = Cats(True, "black")
            >>> cats.Changing_color("white")
            """
            ...

        def is_cat_red(self) -> bool:
            """
            Метод проверяет являеся ли кошка рыжей.
            :return: Является ли кошка рыжей.

            Примеры:
            >>> cats = Cats(True, "black")
            >>> cats.is_cat_red()
            """
            ...

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации


    class Magazine:
        """
        Документация на класс
        Класс описывает модель журнала
        """

        def __int__(self, cost: Union[int, float], topic: str, page: int):
            """
            Cоздание и подготовка к работе объекта "Magazine"

            :param cost: стоимость журнала
            :param topic: тематика журнала
            :param page: число страниц в журнале

            Примеры:
            >>> magazine = Magazine(500, sport, 80) # инициализация экземпляра класса
            """
            if not isinstance(cost, (int, float)):
                raise TypeError("Стоимость журнала должна быть типа int или float")
            if not cost > 0:  # проверяем, что cтоимость не отрицательная
                raise ValueError("Стоимость должна быть положительным числом")
            self.cost = cost
            if not isinstance(page, int):
                raise TypeError("Число страниц должно быть типа int ")
            if not page >= 0:  # проверяем, что число страниц не отрицательное
                raise ValueError("Число страниц должно быть больше нуля")
            self.page = page
            self.topic = topic
        def Raising_the_praise(self, raising_cost: Union[int, float]):
            """
            Метод увеличивает стоимомь журнала.
            :param raising_cost: То, на сколько выросла стоимость журнала

            Примеры:
            >>> magazine = Magazine(500, sport, 80)
            >>> magazine.Raising_the_praise(60)
            """
            if not isinstance(raising_cost, (int, float)):  # проверяем, что добавочная стоимость тпа int или float
                raise TypeError  # вызываем ошибку
            if not raising_cost > 0:  # проверяем, что cтоимость не отрицательная
                raise ValueError
            ...

        def cost_of_page(self) -> None:
            """
            Метод рассчитывает стоимость одной страницы журнала.

            :return: стоимость одной страницы журнала

            Примеры:
            >>> magazine = Magazine(500, sport, 80)
            >>> magazine.cost_of_page()
            """
            ...

    if __name__ == "__main__":
        doctest.testmod()  # тестирование примеров, которые находятся в документации

    pass
