# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         d, m, y = map(int, data_as_string.split('.'))
#         return cls(d, m, y)
#
#     @staticmethod
#     def is_date_valid(data_as_string):
#         if data_as_string.count('.') == 2:
#             d, m, y = map(int, data_as_string.split('.'))
#             return d <= 31 and m <= 12 and y <= 3999
#
#
# dates = [
#     '30.12.2020',
#     '30.12.2020',
#     '31.01.2021',
#     '12.31.2020'
# ]
#
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)  # '30.12.2020'
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print("Некорректная дата")
#
#
#
# class Change:
#     def __init__(self, kg=0):
#         self.kg = kg
#
#     @property
#         def coord_x(self):  # __get_x
#             print("Вызов __get_x")
#             return self.__x
#
#         @coord_x.setter
#         def coord_x(self, x):  # __set_x
#             print("Вызов __set_x")
#             self.__x = x
#     coord_x = property(__get_x, __set_x, __del_x)
