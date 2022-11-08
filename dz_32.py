class Integer:
    @classmethod
    def verify(cls, coord):
        if not isinstance(coord, int) or coord <= 0:
            raise TypeError(f'Координата {coord} должна быть положительным целым числом')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def existence(self):
        if (self.a + self.b > self.c) and (self.c + self.b > self.a) and (self.a + self.c > self.b):
            return "существует"
        else:
            return "не существует"

    def info(self):
        print(f'Треугольник со сторонами({self.a},{self.b},{self.c}) {self.existence()}')


z1 = Triangle(2, 5, 6)
z2 = Triangle(5, 2, 8)
z3 = Triangle(7, 3, 6)
z1.info()
z2.info()
z3.info()
