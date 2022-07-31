# # 1
# # r = ('ab', 'abcd', 'cde', 'abc', 'def')
# # s = input("-> ")
# # if s in r:
# #     print('YES')
# # else:
# #     print('такого символа нет')
#
# # 2
a = (2, 5, 3, 5, 2, 3, 6, 5, 1)
print(a)
b = 0
c = 0
d = 0
z = 0
x = 0
for el in a:
    if el == 2:
        b += 1
    if el == 5:
        c += 1
    if el == 3:
        d += 1
    if el == 6:
        z += 1
    if el == 1:
        x += 1
print('Колличество 2= ', b, '\nКолличество 5= ', c, '\nКолличество 3= ', d, '\nКолличество 6= ', z, '\nКолличество 1= ',
      x)
