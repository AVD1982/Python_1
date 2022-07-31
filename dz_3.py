sim = input("введите номер операции\n1- унарный минус\n2-сложение\n3-вычитание\n4-деление\n5-умножение\n6-деление по модулю(остаток от деления)\n7-мин. значение\n8-мак. значение:")
while type(sim) != int:
    try:
        sim = int(sim)
        if 1 <= sim <= 8:
            a = int(input("введите целое число"))
            if sim == 1:
                a = - a
                print(a)
            else:
                b = int(input("введите  2-е целое число"))
                if sim == 2:
                    c = a + b
                    print(c)
                elif sim == 3:
                    d = a - b
                    print(d)
                elif sim == 4:
                    try:
                        i = a / b
                        print(i)
                    except ZeroDivisionError:
                        print("HA 0 делить нельзя")
                elif sim == 5:
                    f = a * b
                    print(f)
                elif sim == 6:
                    g = a % b
                    print(g)
                elif sim == 7:
                    if a < b:
                        print(a)
                    elif a > b:
                        print(b)
                    else:
                        print(a, "равнo", b, )
                elif sim == 8:
                    if a > b:
                        print(a)
                    elif a < b:
                        print(b)
                    else:
                        print(a, "равнo", b, )
        else:
            print("Введите номер операции от 1 - 8")
    except ValueError:
        print("число не целое")
        sim = int(input("Введите номер операции от 1 - 8!"))
