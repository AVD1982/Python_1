# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.__num} ПРИНАДЛЕЖИТ {self.__surname} БЫЛ ОТКРЫТ.')
#         print("*" * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет # {self.__num} принадлежащий {self.__surname} был закрыт')
#
#     def get_num(self):
#         return self.__num
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     def print_info(self):
#         print(f'Информация о счете:')
#         print("-" * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f'{val}{Account.suffix} было успешно снято!')
#             self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account("12345", 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percents()
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
#

#  ___________________________________
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.__num} ПРИНАДЛЕЖИТ {self.__surname} БЫЛ ОТКРЫТ.')
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')
#
#     def __set_num(self, num):
#         self.__num = num
#
#     def __get_num(self):
#         return self.__num
#
#     num1 = property(__get_num, __set_num)
#
#     def __set_surname(self, surname):
#         self.__surname = surname
#
#     def __get_surname(self):
#         return self.__surname
#
#     surname1 = property(__get_surname, __set_surname)
#
#     def __set_percent(self, percent):
#         self.__percent = percent
#
#     def __get_percent(self):
#         return self.__percent
#
#     percent1 = property(__get_percent, __set_percent)
#
#     def __set_value(self, value):
#         self.__value = value
#
#     def __get_value(self):
#         return self.__value
#
#     value1 = property(__get_value, __set_value)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}.")
#
#     def print_info(self):
#         print(f'Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты {self.__percent:.0%}')
#         print('-' * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет{val}{Account.suffix}")
#         else:
#             self.__value -= val
#             print(f'{val}{Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#
# acc = Account("12345", "ДОЛГИХ", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.surname1 = "Дюма"
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


#  _____________________ 22.10

class Point3d:
    CH = "Koopдината должна быть числом"
    Rigth = "Правый операнд должен быть типом Point3d"

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.__x}, {self.__y}, {self.__z}"

    @staticmethod
    def __check_Vvalu(v):
        return isinstance(v, int) or isinstance(v, float)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.__check_Vvalu(value):
            self.__x = value
        else:
            print(self.CH)

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        if self.__check_Vvalu(value):
            self.__z = value
        else:
            print(self.CH)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.__check_Vvalu(value):
            self.__y = value
        else:
            print(self.CH)

    def __add__(self, other):
        if not isinstance(other, Point3d):
            raise ValueError(self.Rigth)
        else:
            return Point3d(self.__x + other.x, self.__y + other.y, self.__z + other.z)

    def __sub__(self, other):
        if not isinstance(other, Point3d):
            raise ValueError(self.Rigth)
        else:
            return Point3d(self.__x - other.x, self.__y - other.y, self.__z - other.z)

    def __mul__(self, other):
        if not isinstance(other, Point3d):
            raise ValueError(self.Rigth)
        else:
            return Point3d(self.__x * other.x, self.__y * other.y, self.__z * other.z)

    @staticmethod
    def __check0(exemplar):
        if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
            raise ZeroDivisionError("Ни одна из координат второго операнда не долдна быть равна 0")

    def __truediv__(self, other):
        if not isinstance(other, Point3d):
            raise ValueError(self.Rigth)
        self.__check0(other)
        return Point3d(self.__x / other.x, self.__y / other.y, self.__z / other.z)

    def __eq__(self, other):
        if not isinstance(other, Point3d):
            raise ValueError(self.Rigth)
        return self.__x == other.x and self.__y == other.y and self.__z == other.z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")
        elif item == "x":
            return self.__x
        elif item == 'y':
            return self.__y
        elif item == "z":
            return self.__z
        else:
            print("Неверно задан ключ")

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")
        if self.__check_Vvalu(value):
            if key == 'x':
                self.__x = value
            elif key == 'y':
                self.__y = value
            elif key == 'z':
                self.__z = value
        else:
            print("Koopдинаты должны быть числами")


pt1 = Point3d(12, 15, 18)
pt2 = Point3d(6, 3, 9)
print("Координаты 1й точки: ", pt1)
print("Координаты 2й точки: ", pt2)

pt3 = pt1 + pt2
print(f"Сложение координат: ({pt3})")

pt4 = pt1 - pt2
print(f"Разность координат: ({pt4})")

pt5 = pt1 - pt2
print(f"Произведение координат: ({pt5})")

pt6 = pt1 / pt2
print(f"Произведение координат: ({pt6})")

print(f'Равенство координат: {pt1 == pt2}')

print("x =", pt1['x'], 'x1=', pt2['x'])
print("y =", pt1['y'], 'y1=', pt2['y'])
print("z =", pt1['z'], 'z1=', pt2['z'])

pt1['x'] = 20
print('Запись значения в координату x: ', pt1['x'])

____________________________
[12:41] Петров Александр Владимирович
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}'
    def make_sound(self):
        return f'{self.name} гавкает'
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'Я кот. Меня зовут {self.name}. Мой возраст {self.age}'
    def make_sound(self):
        return f'{self.name} гавкает'


cat = Cat('Пушок', 2.5)
dog = Dog('Мухтар', 4)
s = [cat, dog]
for i in s:
    print(i.info(), '\n', i.make_sound())

