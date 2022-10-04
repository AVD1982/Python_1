# 1 задание
# my_str = 'I am learning Python. hello, WORLD!'


class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def coord_x(self):  # __get_x
        print("Вызов __get_x")
        return self.__x

    @coord_x.setter
    def coord_x(self, x):  # __set_x
        print("Вызов __set_x")
        self.__x = x

    @coord_x.deleter
    def coord_x(self):  # __del_x
        print("Удаление свойства")
        del self.__x

    # coord_x = property(__get_x, __set_x, __del_x)


p1 = Point(5, 10)
p1.coord_x = 100
print(p1.coord_x)
del p1.coord_x
p1.coord_x = 7
print(p1.__dict__)