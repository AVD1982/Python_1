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


#  ___________________________________
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f'Счет #{self.__num} ПРИНАДЛЕЖИТ {self.__surname} БЫЛ ОТКРЫТ.')
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')

    def __set_num(self, num):
        self.__num = num

    def __get_num(self):
        return self.__num

    num1 = property(__get_num, __set_num)

    def __set_surname(self, surname):
        self.__surname = surname

    def __get_surname(self):
        return self.__surname

    surname1 = property(__get_surname, __set_surname)

    def __set_percent(self, percent):
        self.__percent = percent

    def __get_percent(self):
        return self.__percent

    percent1 = property(__get_percent, __set_percent)

    def __set_value(self, value):
        self.__value = value

    def __get_value(self):
        return self.__value

    value1 = property(__get_value, __set_value)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):
        self.__surname = surname

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}.")

    def print_info(self):
        print(f'Информация о счете:')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты {self.__percent:.0%}')
        print('-' * 20)

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет{val}{Account.suffix}")
        else:
            self.__value -= val
            print(f'{val}{Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()


acc = Account("12345", "ДОЛГИХ", 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.surname1 = "Дюма"
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)