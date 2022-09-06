# 1 задача
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = {**a, **b, **c}
#
# print(d)
# 2 Задача

# sl = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 6500},
# }
#
# print(sl['emp3'])
# katal = input("Введите имя каталога: ") # emp3
# person = input("Введите раздел значение которого хотите изменить: ")  # salary
# salary = int(input("З.П: "))
# sl[katal][person] = salary
# for x in sl:
#     print(x)
#     for y in sl[x]:
#         print(y, ": ", sl[x][y], sep="")
#
#
# 3 задача _____________________________________________

# stud = int(input("Введите количество студентов: "))
# spisok = dict()
#
#
# def ch(*args):
#     res = []
#     sr_ar = sum(args) // stud
#     print("средний балл : ", sr_ar)
#
#     for i in args:
#         if i > sr_ar:
#             res.append(i)
#             return res
            # print('r', res)
            # for name_, ball_ in name_ball.items():
            #     if ball_ == res:
            #         print(list(name_ball.keys())[list(name_ball.values()).index(res)])

