# dz 6.1
# import random as r
#
# a = [[r.randint(-20, 10) for row in range(3)] for col in range(4)]
# c = 0
# for row in a:
#     for x in row:
#         if x < 0:
#             c += 1
#         print(x, end="\t\t")
#     print()
#
#
# print('колличество отрицательных элементов: ', c)


#2
# s = [[r.randint(0, 4) for row in range(3)] for col in range(4)]
# c = 1
# for row in range(len(s)):
#     for col in range(len(s[row])):
#         print(s[row][col], end="\t\t")
#         if row > 0:
#             c *= row
#     print()
# print('произведение ненулевых элементов: ', c)
