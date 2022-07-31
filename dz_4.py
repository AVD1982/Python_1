import random
a = random.randint(1, 100)
i = 0
j = 1
b = int(input("введите число от 1 до 100\nдля выхода нажмите 0: "))
if 1 <= b <= 100:
    while i < j:
        if 1 <= b <= 100:
            if b == a:
                i += 1
                print("вы угадали загаданное число с", i, "раза")
            elif b > a:
                print("загаданное число меньше")
                b = int(input("введите число: "))
                i += 1
                j += 1
            elif b < a:
                print("загаданное число больше")
                b = int(input("введите число: "))
                i += 1
                j += 1
        elif b < 1:
            print("вы не смогли угaдать с", i, "раз")
            break
        else:
            b = int(input("введите число от 1 до 100: "))
elif b < 1:
    print("вы не смогли угaдать")
else:
    b = int(input("введите число от 1 до 100: "))

