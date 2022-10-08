# name_new = "Elena"
# age = 20
# print('Hello ' + name_new + ". I am " + str(age))
#
# print(type(name))
# print(type(age))
# print(id(name))
# print(id(age))

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
# import keyword
# print(keyword.kwlist)

# a = 5
# print(a)
# a = 6
# print(a)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a  # c = 1
# # a = b  # a = 2
# # b = c  # b = 1
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("строка \nТекстовые последовательности или строки (string) – это набор символов, заключенный в кавычки.\nТекстовые последовательности или строки (string) – это набор символов, заключенный в кавычки. символов")
# print('строка \
#       символов')

# print("Документ \"script.py\" находтся \rпо заданному пути: \n\tD:\\Python\\project")

# print(type(46460))
# print(type(4.44564156))
# print(445641564454156341563416548674874896749)
# print(4.445641564454156341563416548674874896749)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 ** 2)
# print(5 % 2)

# a = 5
# b = 7
# c = 3
# s = a + b + c
# print("Сумма:", s)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", s / 3)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 4321  # 432
# print("Исходное число:", num)
# a = num % 10
# print(a)
# num = num // 10
# # print(num)
# b = num % 10
# print(b)
# num = num // 10
# # print(num)
# c = num % 10
# print(c)
# num = num // 10
# # print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 9573  # 432
# print("Исходное число:", num)
# res = (num % 10) * 1000
# num = num // 10  # 432
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# print(res)

# a = int(input("Введите число: "))
# # a = int(a)
# print(type(a))
# print(a * 2)

# a = 10
# b = 2
# print("a:", a)
# print("b:", b)
# a = a + b  # a = 10 + 2 = 12
# b = a - b  # b = 12 - 2 = 10
# a = a - b  # a = 12 - 10 = 2
# print("a:", a)
# print("b:", b)

# Функции преобразования типов
# int() - числовой тип
# str() - строковый тип
# float() - вещественный тип
# bool() - булевый тип

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)
# print(type(res))

# print(int(3.8))
# print(round(3.8954144165341, 5))

# print(5 / 2)

# a = '5.2'
# # b = 10
# # c = float(a) + b
# # print(c)
# # print(type(c))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="---", end=" ")
# print("Я учу Python")

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степень", power, "равно:", res)

# b1 = True
# # b2 = False
# # print(b1 + 5)
# # print(b2 + 5)
# print(type(b1))

# print(bool("python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool(-15.2))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)
# print(type(test))

# print(7 == 7)
# print(7 + 2 == 7)
# print(7 + 2 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 5)
# print('привет' > 'Привет')


# print(2 < 14 < 9)
# print(2 * 5 > 7 > 4 + 3)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)


# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)


# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 5
# # if a > b:
# #     print("a > b")
# # elif a < b:
# #     print("b > a")
# # else:
# #     print("b == a")
#
# if a > b:
#     print("a > b")
# if a < b:
#     print("b > a")
# if a == b:
#     print("b == a")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# # if a == b and b == c and c == a:
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or c == a or b == c:
#     print('Треугольник равнобедренный')
# # elif not (a == b and b == c and c == a):
# # elif a != b and b != c and c != a:
# else:
#     print("Треугольник разносторнний")

# num1 = 10
# num2 = 20
# num3 = 20
# if num1 == num2 == num3:
#     print("Равносторонний")
# elif num1 == num2 or num1 == num3 or num2 == num3:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")

# m = int(input("Введите номер месяца: "))
# month = int(input('Введите номер месяца: '))
# if month == 1 or month == 2 or month == 12:
#     print('Зима')
# elif month == 3 or month == 4 or month == 5:
#     print('Весна')
# elif month == 6 or month == 7 or month == 8:
#     print('Лето')
# elif month == 9 or month == 10 or month == 11:
#     print('Осень')
# else:
#     print('Ошибка')

# month = int(input('Введите номер месяца: '))
# if 1 <= month <= 12:
#     if 3 <= month <= 5:
#         print('Весна')
#     elif 6 <= month <= 8:
#         print('Лето')
#     elif 9 <= month <= 11:
#         print('Осень')
#     else:
#         print('Зима')
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     if n == 1:
#         print("На ветке", n, "ворона")
#     if 2 <= n <= 4:
#         print("На ветке", n, "вороны")
#     # else:
#     if 5 <= n <= 9 or n == 0:
#         print("На ветке", n, "ворон")
# else:
#     print("Ошибка ввода данных")

# (условие ? True : False)

# a, b = 10, 20
#
# minim = "a == b" if a == b else "a > b" if a > b else "b > a"
# print(minim)


# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Неправильные данные")
# else:
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")
# # except ValueError:
# #     print("Нельзя вводить строки")
# # except ZeroDivisionError:
# #     print("Нельзя делить на ноль")
#
# print("OK!!!")

# try:
#     a = int(input('Введите первое значение: '))
#     b = int(input('Введите второе значение: '))
#     print(a + b)
# except ValueError:
#     print(str(a) + str(b))


# a = input('Введите первое число: ')
# b = input('Введите второе: ')
# try:
#     a = int(a)  # a = 2
#     b = int(b)  # b = пять
# except ValueError:
#     a = str(a)
#     b = b
# finally:
#     print(a + b)


# while условие:
#     блок инструкций

# i = 10
# while i >= 0:
#     print("i =", i)
#     i -= 1  # i = i + 1

# i = 1
# while i <= 20:
#     if i % 2:
#         print(i, end=" ")
#     i += 1

# i = 1000
# while i >= 1:
#     print(i, end=" ")
#     i //= 10

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1


# n = int(input('Введите число: '))  # 1
# m = int(input('Введите число: '))  # 5
# # i = n
# res = 0
# while n <= m:
#     if n % 2:
#         res += n  # res = res + n
#         print(n, end=" ")
#     n += 1
# print("Сумма целых нечетных чисел:", res)


# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное челое число: "))
#     if not n < 0:
#         break
#
# print(n)
# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)
#
# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# n = int(input("Количество символов: "))
# sim = input("Тип символа: ")
# orient = input("0 - горизонтальная\n1 - вертикальная\nориентация линии: ")
# i = 0
# while i < n:
#     if orient == "0":
#         print(sim, end=" ")
#     elif orient == "1":
#         print(sim)
#     else:
#         print("Такой ориентации не предусмотренно")
#         break
#     i += 1

# kol = int(input("Количество чисел последовательности: "))
# i = 0

# number = int(input('Введите количество чисел последоват: '))  # 5
# i = 1
# n = float(input('Введите число: '))  # 4
# summa = n  # 4
# minim = n  # 4
# maxim = n  # 4
# while i < number:
#     n = float(input('Введите число: '))  # 2  3  6  1
#     summa += n  # summa = summa + n  4 + 2 = 6 + 3 = 9 + 6 = 15 + 1 = 16
#     if maxim < n:
#         maxim = n  # maxim = 6
#     if minim > n:
#         minim = n  # minim = 1
#     i += 1
# print('Среднее арифметическое равно:', summa / number)
# print('Минимальное число равно:', minim)
# print('Максимальное число равно:', maxim)


# i = 1
#
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in 5, 6, 7, 8, 9:
#     print(i)

# for i in 'Hello':
#     print(i)

# range(start, stop, step)
# print(range(4, 6))

# for i in range(100, 0, -10):
#     print(i, end=" ")

# a = int(input("Введите целое число: "))  # 36
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):  # 11
#     if i % 10 == i // 10:  # 1 == 1
#         print(i, end=' ')  # 11


# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Ширина прямоугольника: "))
# h = int(input("Высота прямоугольника: "))  # 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = [i for i in range(6) if i % 2 == 0]
# print(n)


# n = [i * 2 for i in "Hello"]
# print(n)

# Список
# n = [5, 6, [7, 8, 9], "Hello", 5.6, True]
# print(n)
# print(type(n))
# print(n[0])
# print(n[2][0])
# print(n[3])
# print(n[3][1])
#
# print(n[-2])

# n[1] = 256
# n[3] += "100"
# n[-7] = 45
# print(n)
# print(len(n))

# s = [1, 2, 3]
# print([5] * 6)
# print(s)
#
# b = list("Hello")
# print(b)

# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(id(n))
# print(n2)
# print(id(n2))
# if n is n2:
#     print('Списки равны')
# else:
#     print('Списки разные')

# [выражение for переменная in последовательность]
# n = 5
# a = [i for i in range(1, n + 1)]
# print(a)

# n = 5
#
# for i in range(1, n + 1):
#     print(i ** 2, end=" ")

# a = [1, 2, 3]
# b = [4]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# print([int(input("-> ")) for i in range(int(input("n = ")))])

# n = [2, 4, 6, 8]
#
# for i in range(len(n)):
#     print(n[i], end=" ")
#
# print()
# for elem in n:
#     print(elem, end=" ")

# n = [-3, 9, -5, -1]
# b = 0
# for i in n:
#     if i < 0:
#         b += i
#
# print(b)

# a = [int(input('Элементов списка: ')) for i in range(int(input('n = ')))]
# b = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         b += a[i]
# print(b)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         k += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
#
# print("Количество:", k)
# print("Сумма:", s)

# a = [int(input('-> ')) for i in range(int(input('Введите кол-во элементов списка: ')))]
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         s += a[i]
#         k += 1
# print(s / k)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [7, 9, 2, 1, 17, 25]
# a[0], a[-1] = a[-1], a[0]
# print(a)

# Срез
# список[start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::-1])
# print(s[1:5])
# print(s[6:7])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[:])
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# print(a[-3:1:-1])
# print(a[2:5])

# s = [5, 9, 3, 7, 1, 8]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:3] = [20]
# s[2] = 30
# s[32:] = [9, 18, 28, 38, 48]
# print(s)
#
# Методы списков

# s = [5, 9, 3, 7, 1, 8]
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список в конец основного списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, [100, 2])  # добаляет элемент по индексу (первый параметр), с заданным значением (второй параметр)
# print(s)


# s = []
# n = int(input("n = "))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)

# s = []
# n = int(input('n = '))
# for num in range(n):
#     x = int(input('-> '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# DZ
# a = [1, 2, 3]
# b = [11, 12, 13, 4, 2]
# c = []
# print("a =", a)
# print("b =", b)
# # i = 0
#
# # while i < len(a):
# #     c.append(a[i])
# #     c.append(b[i])
# #     i += 1
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)


# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# s = [5, 9, 3, 7, 1, 8]
# # s[3:] = []
# print(s)
# # s.remove(9)  # удаляет первый искомый элемент из списка по значению
# # print(s)
# # last = s.pop(-2)  # без параметров - удаляет последний элемент из списка, указанный параметр - это индекс удаляемого
# # # элемента
# # print(last)
# # print(s)
# # s.clear()  # удаляет из списка все элементы
# # print(s)
# del s[2:4]
# print(s)

# s = [int(input("-> ")) for i in range(int(input("введите ко-во элементов списка: ")))]
# # for i in range(len(s)):
# #     k = int(input('Введите индекс: '))
# #     del s[2]
# #     break
# k = int(input('Введите индекс: '))
# s.pop(k)
# print(s)

# s = [5, 9, 3, 7, 1, 8, 9, 9, 3, 9, 9, 3, 3]
# num = s.count(9)  # количество заданных значений в списке
# print(num)
# print(s)
# ind = s.index(3, 9, -1)
# print(ind)

# a = [1, 2, 3]
# b = a
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
# # a.append(20)
# a[0] = 5
# b[1] = 20
# print("a =", a)
# print("b =", b)


# s = [5, 9, 3, 7, 1, 8, 9, 9, 3, 9, 9, 3, 3]
# print(s)
# s.reverse()  # переворачивает список
# print(s)
# s.sort(reverse=True)  # сортирует в порядке возрастания, изменяет список, reverse=True - сортировка в порядке убывания
# print(s)
# a = sorted(s, reverse=True)  # сортирует в порядке возрастания, НЕ изменяет список
# print(a)
# print(s)

# s2 = ['Виталий', 'Сергей', 'Александр', 'Анна']
# s2.sort(key=len, reverse=True)
# print(s2)

# a = [1, 2, 3, 4, 2]
# b = [11, 12, 13]
# c = []
# print("a =", a)
# print("b =", b)
#
# if len(b) > len(a):
#     for i in range(len(a)):  # от 0 до 3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # от 3 до 5
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)

# import random
#
# print(random.random())
# print(random.randint(10, 15))
# print(random.randrange(0, 10, 2))

# from random import randint, randrange
#
# print(randint(10, 15))
# print(randrange(0, 10, 2))

import random as r

# print(r.randint(10, 15))
# print(r.randrange(10))
#
# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(r.choice(city))
#
# s = [55, 66, 77, 88, 99, 50, 20, 30, 40, 60, 70, 80, 90]
# print(r.choice(s))
# print(r.choices(s, k=5))
# r.shuffle(s)
# print(s)
#
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 2))

# mas = [r.randint(0, 100) for i in range(10)]
# print(mas)


#  Функции агрегирования

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# sum = [1, 2, 3]
# print(min(sum))
# print(sum(lst))

# x = [r.randint(0, 100) for i in range(0, 10)]
#
# print(x)
# m = max(x)
# print("Max:", m)
# x.remove(m)
# x.insert(0, m)
# print(x)


# x = [r.randint(-20, 20) for i in range(10)]
# print(x)
# x.sort(reverse=True)
# # x.reverse()
# print(x)

# x = [r.randint(0, 100) for i in range(10)]
# print(x)
# a = min(x)
# print("min:", a)
# b = x.index(a)
# print("index:", b)
# del x[:b]
# print(x)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# # if len(lst) == 0:
# #     print("Список пуст")
# if not lst:
#     print("Список пуст")

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [r.randint(0, 10) for i in range(n1)]
# b = [r.randint(0, 10) for j in range(n2)]
# print("a =", a)
# print("b =", b)
# # c = a + b
# # print("c = ", c)
#
# # c = []
# # print('Элементы обоих списков без повторений: ', c)
# # for i in a:
# #     if i not in c:
# #         c.append(i)
# # for i in b:
# #     if i not in c:
# #         c.append(i)
# # print("Элементы обоих списков без повторений", c)
#
# # c = []
# # for i in a:
# #     if i in b and i not in c:
# #         c.append(i)
# # print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()


# a = [1, 2, 3]
# print(a)
# for i in a:
#     print(i, end="\t\t")
# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# print(a)
# for x, y in a:
#     print(x, "+", y, "=", x + y)

# m = [[r.randint(-10, 20) for x in range(8)] for y in range(4)]
#
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# print(row, end="\t\t")


# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# i = 0
# while i < size:
#     j = 0
#     while j < symbol:
#         n = 0
#         while n < size:
#             m = 0
#             while m < symbol:
#                 if (i + n) % 2 == 0:
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#                 m += 1
#             n += 1
#         print()
#         j += 1
#     i += 1

# for i in range(8):
#     for j in range(8):
#         if i >= j:
#             print("*", end="")
#     print()


# size = int(input('Введите размер поля: '))
# sumbol = int(input('Введите количество символов: '))
# for i in range(size):
#     for j in range(sumbol):
#         for k in range(size):
#             for m in range(sumbol):
#                 if (i+k) % 2 == 0:
#                     print('+', end=' ')
#                 else:
#                     print(' ', end=' ')
#         print()

# for i in range(9):
#     for j in range(9):
#         if i < j:
#             print("*", end="")
#     print()

# print('Вывести треугольник из звездочек')
# print()
#
# size = 8
# for i in range(size):
#     for j in range(size, i, -1):
#         print('*', end='')
#     print()

# n = [[r.randint(0, 4) for x in range(3)] for b in range(4)]
# m = 1
# for row in n:
#     for x in row:
#         if x > 0:
#             m *= x
#         print(x, end="\t\t")
#     print()
# print("Произведение ненулевых элементов: ", m)


import math

# num1 = math.sqrt(16)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# print(dir(math))
# print(math.pi)

# rd = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * math.pi * rd, 2))

import time

# seconds = time.time()
# print("Секунды с начала эпохи: ", seconds)
# locale_time = time.ctime(454646354)
# print("Местное время:", locale_time)
# res = time.localtime()
# print("Localtime:", res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
# print(time.strftime("Today is %B %d, %Y."))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(4154545347)))


# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")

# text = input("Название напоминания: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "seconds.")

# start = time.monotonic()
# time.sleep(5)
# res = time.monotonic() - start
# print(res, "seconds.")

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня: %B %d, %Y."))

# Функция
# print()
#
#
# def hello(name):  # аргументы
#     print("Hello", name)
#
#
# hello("Irina")  # параметры
# hello("Igor")


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 6
# m = 4
# get_sum(n, m)
# get_sum("abc", "def")
# get_sum(2.5, 4.3)


# def symbol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end="")
#         else:
#             print(c, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     print(a + b)
#     return a + b
#
#
# res = get_sum(1, 8)
# print(res)
# print(get_sum(2, 5))

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))

# x = int(input("a: "))
# y = int(input("b: "))
#
#
# def rs(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# print(rs(x, y))


# def cube(a):
#     return a ** 3
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def fib(n):
#     # a, b = 0, 1
#     a = 0
#     b = 0
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b
#         c = a + b
#         a = b
#         b = c
#
#
# fib(15)


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 15))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if has_upper and has_lower and has_num:
#         if len(password) >= 8 and has_upper and has_lower and has_num:
#             return True
#         else:
#             if len(password) < 8:
#                 print("Количество символов слишком маленькое")
#     else:
#         print("Недопустимые символы")
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a=4, b=3, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# s = 2
# print(get_sum(c=s))

# def symbol(elements=20, sign='-'):
#     for i in range(elements):
#         print(sign, end='')
#     print()
#
#
# symbol(10, "+")
# symbol(5, "*")
# symbol(15, "#")
# symbol(7)
# symbol()

# def digits_sum(n, event=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if event and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not event and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digits_sum(9874023, False))
# print(digits_sum(38271, False))
# print(digits_sum(123456789, event=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#     print("*" * 20)
#
#
# display_info("Ira", 20)
# display_info(20, "Ira")
# display_info(age=23, name="Igor")
# display_info("Ira", age=23, name="Igor")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
# print(id(lt1))
# print(id(lt2))


# lt1 = 5
# lt2 = 5
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # True
# print(id(lt1))
# print(id(lt2))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# print(id(lt1))

# s = "Hello "
# print(id(s))
# s += "World"  # s = s + "World"
# print(s)
# print(id(s))
# # s[1] = "a"
# # s[1:2] = "a"
# # s = s[:1] + s + s[2:]
# s = s[1:-1]
# print(s)
# print(id(s))

# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)

# a = 5
# b = 5
# print(a == b)
# print(a is b)

# a = True
# b = True
# print(a == b)
# print(a is b)

# def add_numbers(n):
#     print("Внутри функции:", n, "=", id(n))
#     n += 1
#     print("После изменения:", n, "=", id(n))
#     return n
#
#
# x = 1
# print(x, "=", id(x))
# x = add_numbers(x)
# print(x, "=", id(x))


# def add_numbers(n):
#     print("Внутри функции:", n, "=", id(n))
#     n += [4]
#     # n = n + [4]
#     print("После изменения:", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print(x, "=", id(x))
# add_numbers(x)
# print(x, "=", id(x))

# типы данных:
# изменяемые: список (list)
# неизменяемые: число (int), строка (str), вещественное число (float), булевы значения (bool)

# Кортеж (tuple) – это неизменяемая структура данных, которая по своему подобию очень похожа на список.
# Кортеж – неизменяемый список. Или списки доступные только для чтения. Cостоит из элементов, разделенных запятыми и
# заключенных в круглые скобки.

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
#
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 5, 6, 7, 8)
# print(a)
# print(type(a))
# b = tuple((1, 5, 6, 7, 8))
# print(b)
# print(type(b))
# q = 1, 2, 3, "w"  # упаковка кортежа
# t = (1,)
# print(type(q))
# print(type(t))
# t1 = tuple("hello")
# print(t1)
# print(t1[1])
# print(t1[1:3])
# t1[1] = "i"

# def change(lst):
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.insert(0, start)
#     # lst.insert(-1, end)
#     lst.append(end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# s1 = tuple(int(input("-> ")) for i in range(5))
# print(s1)

# s = input("-> ")
# print(tuple(s))

# mas = [r.randint(0, 100) for i in range(10)]
# tpl = tuple(mas)
# print(tpl)
# mas = tuple(r.randint(0, 100) for i in range(10))
# print(mas)

# s = tuple(2**i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple(" world")
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))
# # print(t3.count('a'))
# # print(t3.index('l', 4))
# # if 'e' in t3:
# #     print(t3.index('e'))
# # else:
# #     print("Такого символа нет")
# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# t = ("1", 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)
# print(type(x))
# print(type(t))

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user1, user2, user3 = get_user()
# print(user1)
# print(user2)
# print(user3)

# t = (1, 2, 3)
# del t
# print(t)

# lst = [1, 2, 3, 4, 5, 6]
# print(type(lst))
# print(lst)
# tpl = tuple(lst)
# print(type(tpl))
# print(tpl)
# print(list(tpl))

# countries = (
#     ("Германия", 20.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население =", city_population)

# Множества (set) - неупорядоченная коллекция, которая хранит только уникальные значения

# {}
# set()

# s = {4, 7, 8, 9, 4, 2, 4, 2, 4}
# print(type(s))
# print(len(s))
# print(s)

# s = set("hello")
# print(s)

# c = [1, 5, 4, 2, 2, 6, 4]
# s = set(c)
# print(s)
# c = list(s)
# print(c)
# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# def to_set(el):
#     # st = set(el)
#     # return st, len(st)
#
#     return set(el), len(set(el))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# # print("green" not in t)
# for i in t:
#     print(i)

# {i for i in последовательность}
# {i for i in последовательность if условие}
# {i(True) if условие else i(False) for i in последовательность}
# {i(True) if условие else i(False) for i in последовательность if условие}


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)

# print("Вносим изменения")
# print("Вносим изменения в клонируемый проект")

# j = (1, 2, 3, 4, 5, 6, 7, 8)
# d, c, *rest = j
# print(*j, sep="6:")
#
#
# p = range("stat, stop, step")
#
# h = range(1, 6)
# print(*h)
# for x in h: # h итерируемый объект

# # f = [1,2,3,4,5,6]
# # for i, x in enumerate (f):
#
# p = {"top", "BOB", "Viv"}
# p.add("kol")
# print(p)
#
# p.discard("BOB1")
# print(p)
#
# p.clear()
# print(p)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# #
# # c = a & b
# # c = b ^ a
# print(c)
#
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(max(s))
# print(min(s))

# s1 = "Hello"
# s2 = "How are you"
# a = set(s1) & set(s2)
# for i in a:
#     print(i, end=" ")

# drawing = {"Marina", "Jenya", " Sveta"}
# music = {"Kostya", "Jenya", "ilyi"}
# one = drawing ^ music
# print(one)
# two = drawing & music
# print(two)
# drawing = drawing - two
# print(drawing)

# ТИП frozenset (замороженное множество)

# a = frozenset([1, 2, 3, 4, 5])
# print(a)
#
# s = frozenset ({"helloy", "world"})
# print(s)

# словарь  disk()
# lst = ["one", "two", "three"]
# print(lst)
# print(lst[0])
# d = {"a": " one", "b": "two", "c": "three"}
# print(d)
# print(d["a"])

# d = {'one': 1, 2: 'two'}
# print(d)

# d = dict(short='dict', long='dictionary')
# print(d)

# users = (('igorr@com.ru', 'Igor'),('igor@com.ru', 'Iegor'))
# print(users)
# d_users = dict(users)
# print(d_users)

# d = {i: i ** 2 for i in range(7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[9] = 45
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [2, 3, 4], True: 1}
# # print(d)
# #
# # print(d[42][1])
# # print(d[(1, 2.3)])
# # #
# # # print('one1' in d)
# # key = 'one'
# # # if key in d:
# # #     del d[key]
# # try:
# #     del d[key]
# # except KeyError:
# #     print("НЕТ В СЛОВАРЕ")
# # print(d)
#
# for key in d:
#     print(key, "->", d[key])

# f = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in f:
#     res *= f[key]
# print(res)

# d = dict()
# # d[1] = input("->")
# # d[2] = input("->")
# # d[3] = input("->")
# # d[4] = input("->")
# d = {i: input("->")for i in range(1, 5)}
# print(d)
# dislike = int(input("какой элемент исключить: "))
# del d[dislike]
# print(d)
# print(len(d))

# goods = {
#     "1": ['core-i3-4330', 9, 4500],
#     "2": ['core-i5-4670', 3, 8500],
#     "3": ['AMD FM-6300', 6, 3700],
#     "4": ['pentium-i3-4330', 8, 2100],
#     "5": ['core-i5-3350', 5, 4600],
# }
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], "шт. по", goods[i][2], "руб.", sep="")
# while True:
#     n = input("№: ")
#     if n != "0":
#         k = int(input("количество"))
#         goods[n][1] = k
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], ' - ', goods[i][1], "шт. по", goods[i][2], "руб.", sep="")

# d = {'A': 1, 'B': 2, 'C': 3}
# # value = d.get ('B')
# a = d.items()
# print(a)
# b = d.keys()
# print(b)
# c = d.values()
# print(c)
#
# for key, val in d.items():
#     print(key, val)
#
# # item = d.pop('B')
# # item = d.setdefault('C', 8)
# d.update([('R', 7), ('Q', 9)])
# # print(item)
# print(d)
#
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'citty': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(new_d)

# a = {
#     'First': {
#         1: "one",
#         2: "two",
#         3: 'three',
#     },
#     'First2': {
#         1.1: "one",
#         2.2: "two",
#         3.3: 'three',
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep = "")
#

# sales = {
#     'John': {"N": 3056, 's': 8463, 'e': 8441, 'w': 2694},
#     'John2': {"N": 1634, 's': 789463, 'e': 847841, 'w': 23694},
#     'John3': {"N": 3547, 's': 847863, 'e': 84941, 'w': 26934},
#     'Joh4': {"N": 8956, 's': 8436863, 'e': 84441, 'w': 264694}
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep = "")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# data = int(input("Новое значение: "))
# sales[person][region] = data
# print(sales[person])

# data = {"Один": 1, "Два": 2, "Три": 3, "Четыре": 4}
# d = {k: v for k, v in data.items() if v <= 2}
# print(d)

# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)
# a = list(b.items() )
# print(a)

# a = ["Один", 1, 2, 3, "Два", 10, 20, "Три", 15, 36, 60, "Четыре", -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i # s = 'odin'
#     else:
#         d[s].append(i)
# print(d)
# zip____________________________________________________________________

# d = dict(zip([12, 1, 2], ['dec', 'jan', 'feb']))
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = {k: v for k, v in zip(b, a)}
# print(d)

# one = {"name": "Igor", "Last_ name": "Smith", "Job": "Consultant"}
# two = {"name": "Olga", "Last_ name": "Smat", "Job": "Manager"}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, v1)
#     print(k2, v2)
# распаковка последовательности

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# month = ["jan", "feb", "march"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Общая прибыль в", m, "=", profit)

# one = {"apple": 20, "orange": 35}
# two = {"pepper": 40, "onion": 55}
# print({**two, **one})
# _________________________________________________________
# for i in range(3):
#     print(i)
# colors = ['red', 'yellow', 'green']
# j = 1
# for i in colors:
#     print(j, i)
#     j += 1
# colors = ['red', 'yellow', 'green']
# for j, i in enumerate(colors, 1):
#     print(j, i)
# __________________________________________


# a = [1, 2, 3, 4, 5]
# b= [*a, 6,6, 1, 2, 3, 4, 5]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(2))
# print(func(2, 3, 1))
#


# def summs(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
# print(1, 2, 3, 4, 5)
# print(7, 3)


# def to_dict(*args):
#     return {i: i for i in args}
#

# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))


# def ch(*args):
#     res = []
#     sr_ar = sum(args) / len(args)
#     print(sr_ar)
#     for i in args:
#         if i < sr_ar:
#             res.append(i)
#     return res
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))
#

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))


# def print_scorec(student, *scorec):
#     print("Student Name:" + student)
#     for scorec in scorec:
#         print(scorec)
#
# print_scorec("Irina", 100, 85, 96, 33, 25)
# print_scorec("Igor", 100, 44, 25)


# def intro(**data):
#     for k, v in data.items():
#         print(k, 'is', v)
#     print()
#
# intro(first_name="Irina",last_name="Fokina",age=22)
# intro(first_name="Igor",last_name="Gina",email="a1hqih.com", age=22, phone="98736244")
#

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age='31', weight=61, eyes_color='gray')
# print('my_dict=', my_dict)

# def db(b, *args, name=None, **kwargs):
#     # print(b, args, name, kwargs)
#
# db(6, 'd', "l", a=5, name='Olga')
#
# name = 'Tom'  # глобальная область видимости
#
#
# def hi():
#     # global name
#     name = "Sam"  # локальная область видимости
#     print("Hello", name)
#
#
# def bye():
#     print("good bye", name)
#
#
# hi()
# bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print("i =", i)
#     print('arg =', arg)
#
#
# i = 6
# func()

# x = 4
#
# def add_two(a):
#     x = 2
#
#     def add_some():
#         x = 5
#         print('x=', x)
#
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
# @italic
# @bold
#
# def hello():
#     return "text"
# print(hello())
# ________________________________________________________________________________________
# def cnt(fn):
#     count = 0
#
#         def wrap():
#             nonlocal count
#             count = count +1
#             fn()
#             print('вызов функции: ',count)
#         return wrap
#
#
# @cnt
# def hello():
#      print(hello())
#
#
# hello()
# hello()

# def args_dec(fn):
#     def wrap(x, y):
#         print("Сложение: ", x, "И", y, "=", end=" ")
#         fn(x, y)
#     return wrap
#
#
# @args_dec
# def summa(a, b):
#     print(a + b)
#
#
# summa(5, 2)
#
# def mytiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#         return wrap
#     return my_decorator
#
#
# @mytiply(3)
# def return_num(num):
#     return num
#
#
# print("Рузультат: ", return_num(5))


# def changeCharTOStr(s, c_old, c_new):
#     i = 0
#     s2 =""
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i = i + 1
#     return s2
#
#
# str1 = " Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования."
# str2 = changeCharTOStr(str1, "N", "P")
# print(str1)
# print(str2)

# _________________________________________________________________________

# print(ord("л"))
# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# my_str = 'Test string for meee'
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднеe арифмeтическое ", arr)
# arr += [x for x in [ord(x) for x in input('->') + " "[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print("Количество последних элементов: ", arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)
#
# print(chr(97))
# print(chr(7544))

# a = 122
# b = 97
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65

# from random import randint
#
# short = 7
# longest = 12
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_length = randint(short, longest)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(min_ascii, max_ascii))
#         res += random_char
#     return res
# print('Ваш случайный пароль:',random_password())

# s = "hello, WORLD! I am learn Python."
# print(s.capitalize())  # Hello, world! i am learn python.
# print(s.lower())  #
# print(s.upper())  # HELLO, WORLD! I AM LEARN PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARN pYTHON.
# print(s.title())  # Hello, World! I Am Learn Python.
#
#
# print(s. count('h', 1, -4))  # колличество искомых символов
# print(s.find("Python"))   #возвращается индекс первого совпадения
# print(s.find("oPython"))  #если пщдсстраки нет
#
# string = "один два"
# one = string[:string.find(" ")]
# two = string[string.find(" ") + 1:]
# print(two + " " + one)
#
# s = "hkj14blk8496hk"
# digits = []
# for symbol in s:
#     if '0123456789'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)

# print("   py".lstrip())
# print("py    ".rstrip())
# print('   py   '.strip())
#
# print("https://www.pyton.org".lstrip("th/sp:"))
#
# print('$py.$$$;'.rstrip(';$.'))
# print('$py.$$$;'.strip(';$.'))
#
# print("https://www.pyton.org".lstrip("th/sp:").rstrip("/.org"))

# str1 = " Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python", 2))
#
# s = " - "
# seq = ('a', 'b', 'c')
# print(s.join(seq))   # a - b - c
# print('..'.join(['1', '2']))
# print('..'.join('hello'))

# print('строка разделенная пробелами'.split())
#
# print('www.python.org.ru'.split('.', 2))
# print('www.python.org.ru'.rsplit('.', 2))
# print('www...python...org.'.rsplit('.'))

# a = input('->').split()
# print(a)
# ______________________________________________________________
# s = ''''hganinrgnq'''
#
# up = s.count ('E')
# down = s.count(' e')
# print(up)
# print(down)
# e = up + down
# print("an, ", e)
#  ____________ругулярные выражения____________________________

import re

# s = "Я ищу совпадения в 2021 года. И я из найду в 2 счёта.4654"
# reg = r'[2021]'
# print(s.find(reg))
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# print(re.search(reg, s))  # возвращает первое совпадение и останавливает поиск
# print(re.search(reg, s).span()) # 15,16
# print(re.search(reg, s).start()) #  15
# print(re.search(reg, s).end()) # 16
# print(re.search(reg, s).group()) # я
#
# print(re.match(reg, s)) # для поиска заданному шаблону в начале строки

# print(re.split(reg, s))
# print(re.split(reg, s, 1))
# print(re.sub(reg, "!", s, 1))

# [] - шаблон возвращает любой из символов
# print(re.findall(reg, s))
#
# reg = r'[12][0-9][0-9][0-9]'
# print(re.findall(reg, s))
# reg = r'[А-яё]'
# print(re.findall(reg, s))
#
# s = "Час в 24-часовом формате от 00 до 23. 2021-06Т21:45. Минуты, в диапазоне от 00 до 59. 2021-0615Т01:09"
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, s))

# s = "author=Пушкин А.С.; title = Евгений Онегин; price =200; tear= 1831"
# reg = r"\w+\s*=\s*[^;]+"
# print(re.findall(reg, s))

# s = "12 сентября 2021 года 789"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))

# s = '+7 499 456-45-78, +74994564578, +7(499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s))

# s = "Я ищу совпадения в 2021 года. И я из найду в 2 счёта.4654"
# reg = r'^\w+\s\w+'
# print(re.findall(reg, s))

#  __________________________________________________________________________________________________

# text = """Pyton,
# pyton,
# PYTON"""
# reg = "(?mi)^pyton"
# print(re.findall(reg, text))

# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name, re.IGNORECASE)
#
#  greedy - захватывает максимально возможное число символов
#  ? lazy - захватывает минимально возможное число символов
#  *?, +?, ??
#  {m,n}?, {,n}?, {m,}?


# print(validate_name('Pyton_master'))
# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>',text))


# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы </p>"
# # reg = '<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# text = "методы этой группы  [16] выполняют [17] лтпоцт [18][19]."
# print(re.findall(r'\[.*?]',text))

# # s = "Петр, и Виталий отлично учаться"
# reg = 'Петр|Ольга|Виталий'
# print(re.findall(reg, s))s

#
# s = "int = 4, float = 4.0, double = 8.0f"
# reg = r"((?:int|float)\s*=\s*\d[.w+]*)"
# print(re.findall(reg, s))


# s = '127.0.0.1'

# s = '192.255.255.255 '
# # reg = r'\d{1,3}.\d{1.3}.\{d1/3}.\d{1/3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = "Word2016, PS^, AI5"
# reg = r'[a-z]+\d*'
# print(re.findall(reg, s, re.I))

# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# a = "28-08-2021"
# reg = "(0[1-9[1-3]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, a))

# s = 'Я ищу совпадения в 2021 года. И я из найду в 2 счета'
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])
# print(re.findall(reg, s))
# print(re.search(reg, s).group(1))
# print(re.search(reg, s).group(2))

# text = '''
# Астрахагь
# Орск
# Курск
# '''
# count = 0
#
#
# def replece_find(m):
#     global count
#     count += 1
#
#     return f"<option value='{count}'>{m.group(1)}/</option>\n"
#
# print("<select>")
# print(re.sub(r'\s*(\w+)\s*', replece_find, text))
# print("</select>")


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы </p>"
# # reg = r'<img\s+[^>]*src=([\'"])(.+)+\1>'
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q)>'
# # (?P<name>)  (?P=name)
# print(re.findall(reg, s))

# s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022"
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# # print(re.findall(reg, s))
# print(re.sub(reg, r"\2.\1.\3", s))
#
# s = "google.com and google.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# # print(re.findall(reg, s))
# print(re.sub(reg, r"http://\1", s))
# #
# def validat_phone(name):
#     reg = r"^\+?7[ (]*\d+[ )]*[\d -]{8,10}$"
#     return re.search(reg, name).group()
#
#
# print(validat_phone('+7 499 456-45-78'))
# print(validat_phone('+74994564578'))
# print(validat_phone('7 (499) 456-45-78'))
# print(validat_phone('7 (499) 456-45-78'))

# s = '+7 499 456-45-78'
# reg = r"\+?7[ (]*\d+[ )]*[\d -]{8,10}"
# print(re.findall(reg, s))

# РЕКУРСИЯ
# ___________________________________________________________________
# def sum_list(lst)
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def sum_list(lst):
#     if len(lst) == 1: # базовый случай (условие выхода)
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0]
#     else:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(255, 16))

# name = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']

# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count


# print(count_items(name))
#
#
# # print(name[0])
# # print(isinstance(name[0], list))  # False
# # print(ame[1])
# # print(isinstance(name[1], list))  # True
# # print(name[1][1][0])n
# def func(item_list):
#     count = 0
#     for i in item_list:
#         if isinstance(i, list):
#             for j in i:
#                 if isinstance(j, list):
#                     for k in j:
#                         count += 1
#                 else:
#                     count += 1
#         else:
#             count += 1
#     return count


#  Файлы
#  _____________________________________________

#  1-е открытие файла
#  2-е операции с файлом (запись, чтение)
#  3-е закрытие файла
# f = open(r'C:\Users\Chia_Dub\PycharmProjects\pythonProject1\text.txt', 'r')
# #
# # # print(f.closed)
# # # print(f.mode)
# # # print(f.name)
# # # print(f.encoding)
# # print(f.read(3))
#
#
# # print(f.readline())
# # print(f.readline(3))
# # print(f.readline())
# print(f.readline(26))
# f.close()

# f = open("fail.txt")
# # print(len(f.readline()))
# # f.close()
# cnt = 0
# s = f.readline()
# while s != '':
#     s = f.readline()
#     cnt += 1
# print(cnt)
# f.close()
#
# f = open('xyz.txt', 'a')
# f.write('Hello \nWorld')
# f.write('\nNew text')
# f.close()
# lines = ['This is line1', "This is line2"]

# my_file = open("text2.txt", "w")
# my_file.write("Замена строки в текстовом документе;\nизменение строки в списке;\nзаписать список в файл;")
# my_file.close()
#
# my_file = open("text2.txt", "r")
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменение строки в списке;\n":
#         read_file[i] = "Hello World!\n"
# print(read_file)
# my_file.close()
#
#
#
#
# my_file = open("text2.txt", "w")
# my_file.writelines(read_file)
# my_file.close()


#  ____________________________________

# file_name = 'res.txt'
# lst = [4.5, 2.8, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# print(get_line(lst))
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# file_name = 'res.txt'
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# num_list = list(map(float, nums.split()))
# print(nums)

# with open('test.txt', 'r') as f:
#     w = f.read().split()
#     print(w)
#     # max_length = len(max(w, key=len))
#     max_length = max(len(word) for word in w)
#
#
#     print(max_length)
#     res = [word for word in w if len(word) == max_length]
#     print(res)

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10"
#
# with open('one.txt', 'w')as f:
#     f.write(text)
#
# read_file = 'one.txt'
# write_file = 'two.txt'
#
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replase('Строка', 'Линия-')
#         fw.write(line)
# #  ?????????????????????????????????????????
# with open(w)

#
# f = open ('test.txt')
# line = 0
#
# for i in f:
#     line += 1
#     word = 0
#     flag = 0
#     for j in i:
#         if j != " " and flag == 0:
#             word += 1
#             flag = 1
#         elif j == " ":
#             flag = 0
#     print(i, len(i), word, 'clov')
#
# print(line, 'строки')

import os

# print("текущая директоия:", os.getcwd())
# print(os.listdir())  #  вернулся список файлов и папок, находящихся в текущей директории (по умолчанию
# #  или в директории по указанному пути
# print(os.listdir(".."))
# os.mkdir("folder")  #создает директорию по указанному пути
# os.makedirs("folder1/folder2") # создание влоенных папок
# os.remove('xyz.txt') # удаление файла

# os.rename('folder1', "test1") # переименование папки (файла)

# os.rename("text2.txt", "test/test.txt") # переносы и переименование файла (папки)

# os.renames("text.txt", "text/text1.txt")

# os.rmdir("folder")  #  удаление _пустой_ папки!!!

# for root, dirs, files in os.walk('res'):
#     print("Root", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)
#  ______________________________________________________________
# os.paht.join()
# dirs = ['Work/F!', 'Work/F2/f21']
# for dir in dirs:
#     os.makedirs(dir)

# files = {
#     'Work':['w.txt'],
#     'Work\\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     'work\\F2\\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         print(file_path)
#         open(file_path, "w").close()
# file_with_text = []

# class Point:


#     x = 1
#     y = 1
#
#     def set_coords(self):
#         print(self.__dict__)
#
# p1 = Point()
# print(type(p1))
# Point.x = 100
# p1.x = 200
# p1.y =5
# p1.set_coords()
# print(p1.x, p1.y)
# print(id(p1))
# print(id(Point))
# print(p1.__dict__)
# print(Point.__dict__)
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))
# p2 = Point
# print(p2.x, p2.y)


# class Point:
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coords(5, 10)
# print(p1.__dict__)

# class Human:
#     name = "name"
#     birthday = '00.00.00'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print('Персональные данные'.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\n'
#               f'Номер телефона:{self.phone}\n Страна: {self.country}\n'
#               f'Город: {self.city}\n Домашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name): # Установить имя
#         self.name = name
#
#     def get_name(self): # получить имя
#         return self.name
#
#
# h1 = Human()
# h1.input_info('Юля', "23.05.1986", "45-46-98", 'Россия', "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("VIKA")
# print(h1.get_name())
#
# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# print(p1.__dict__)
# print(p1.x)
# print(getattr(p1, 'x'))
# print(getattr(p1, 'z', 'False'))
# print(hasattr(p1, 'z'))
#
# setattr(p1, 'z', 7)
# print(p1.__dict__)
#
# delattr(p1, 'z')

#
# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Дaнные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('квалификация сотрудника:', self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Diznik")
# p2.print_info()
# p1.add_skill(2)


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print("Удаление экземпляра:" + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
#
# print(p1.x)


# class Point:
#     count = 0  # статические свайства
#
#     def __init__(self, x=0, y=0):  # динамические свойства
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# print(Point.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключаются")
#         Robot.k -= 1
#         if Robot == 0:
#             print(self.name, "был последним")
#         else:
#             print("работающих роботов осталось:", self.name)
#
#     def say_hi(self):
#         print("Приветствую меня зовут:", Robot.k)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("c-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какуют-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# print("Численность роботов:", Robot.k)

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(q):
#         if isinstance(q, int) or isinstance(q,float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         # if (isinstance(x, int) or isinstance(x, float) and (isinstance(y, int) or isinstance(y, float))):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("координаты числами")
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("координаты должны быть числами")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("координаты должны быть числами")
#
#     def get_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("координаты должны быть числами")
#
#     def get_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(1, 2)
# print(p1.get_coords())
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.__y = 'abc'
# # print(p1.__x, p1.__y)
# print(p1.__dict__)
#


# class Car:
#     def __init__(self, name, year, model, power, color, price):
#         self.__name = self.__model = self.__color = "некоректные данные"
#         self.__year = self.__power = self.__power = 0
#         if Car __check_value_str(name):
#             self.__name = name
#
#         self.__model = model
#         self.__power = power
#         self.__color = color
#         self.__price = price
#
#     def __check_value_int(s):
#         if not isinstance(s, int):
#             print("Данные должны быть числом")
#             return False
#         return True
#
#     def __check_value_str(s):
#         if not isinstance(s, str):
#             print("Данные должны быть строкой")
#             return False
#         return True
#
#     def set_name(self, name):
#         if Car.__check_value_set(name):
#             self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     def print_info(self):
#         print("данные автомобиля".center(40, '*'))
#         print(f"""Название модели: {self.__name}
# Год выпуска: {self.__year}
# Производительность: {self.__model}
# Мощность двигателя: {self.__power} л. c.
# Цвет машины: {self.__color}
# Цена :{self.__price}""")
#
#
# c1 = Car('X7 M50i', 2021, 'BMW', 530, "white", 10790000)
# c1.print_info()
# c1.set_name('X2')
# print(c1.get_name())
# c1.print_info()

# class Point:
#     __slots__ = ["x", "y", "z"]
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# p1.z = 2
# print(p1.z)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __set_x(self, x):
#         print("вызов сет")
#         self.__set_x = x
#
#     def __get__(self):
#         print("вызов гет")
#         return self.__x
#     coord_x = property(__get__x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.coord_x = 100

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name (self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def name(self, n):
#         self.__old = n_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
# p1 = Person('Irina', 26)
# print(p1.name)
# p1.name = " Igor"
# del p1.name
# p1.old = 31
#
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# print("p1=", Point.get_count())
# p2 = Point()
# print("p2=", Point.get_count())
# p3 = Point()
# print("p3=", p1.get_count())
# class Point:

#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count())
#
#
# p1 = Point()
# print("p1=", Point.get_count())
# p2 = Point()
# print("p2=", Point.get_count())
# p3 = Point()
# print("p3=", p1.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

#  __________________________________________________________
# class Numbers:
#     @staticmethod
#     def min(a, b, c, d):
#         minim = min(a, b, c, d)
#         return min
#
#
# print("Минимальное число", Numbers.min(2, 5, 1, 9))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_bd(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         d, m, y = map(int, data_as_string.split('.'))
#         return cls(d, m, y)
#
#     @staticmethod
#     def is_date_valit(data_as_string):
#         if data_as_string.count('.') == 2:
#             d, m, y = map(int, data_as_string.split('.'))
#             return d <= 31 and m <= 12 and y <= -3999
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '01.31.2021',
#     '12.31.2020'
# ]
# for string_data in dates:
#     if Date.is_date_valit(string_data):
#         data = Date.from_string((string_data))
#         string_to_db = date.string_to_bd()
#         print(string_to_db)
#     else:
#         print("не корректная дата")

# d1 = Date.from_string('12.11.2022')
# print(d1.string_to_db())

#         string_data = '20.10.2022'
# d, m, y = map(int, string_data.split('.'))
# date1 = Date(d, m, y)
# print(date1.string_to_bd())
# _______________________________________________________________________________________________
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value=0):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} ПРИНАДЛЕЖИТ {self.surname} БЫЛ ОТКРЫТ.')
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')

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
        self.surname = surname

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}.")

    def print_info(self):
        print(f'Информация о счете:')
        print('-' * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты {self.percent:.0%}')
        print('-' * 20)

    def add_percents(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начисленны")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет{val}{Account.suffix}")
        else:
            self.value -= val
            print(f'{val}{Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавленно!')
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

acc.edit_owner("Дюма")
acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)  #  ____________________________________________________________________________
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall(r"[a-z-а-яё-]", fio, flags=re.IGNORECASE))
#         # print(letters)
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('Вес должен быть от 20 кг и выше')
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
