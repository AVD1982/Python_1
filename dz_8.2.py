a = int(input("1-прямоугольник\n2-треугольник\n3-круг\nВведите номер фигуры для определения ее площади: ", ))
if 1 <= a <= 3:
    if a == 1:
        b = int(input("введите ширину: ", ))
        c = int(input("введите длинну: ", ))
    elif a == 2:
        b = int(input("введите основание: ", ))
        c = int(input("введите высоту: ", ))
    elif a == 3:
        b = int(input("введите радиус окружности: ", ))
else:
    print("Введите номер операции от 1 - 3")


def pl_f(s):
    if a == 1:
        print(b * c)
    elif a == 2:
        print(0.5 * b * c)
    else:
        a == 3
        print(3.14 * b ** 2)


pl_f(a)
