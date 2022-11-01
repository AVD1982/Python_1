import geometry, math
from abc import ABC, abstractmethod


class Share(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class Square(Share):
    def __init__(self, w, color):
        self.w = w
        # self.h = h
        super().__init__(color)

    def perimeter(self):
        perimeter = self.w * 4
        return perimeter

    def square(self):
        return self.w * self.w

    def draw(self):
        return ('*' * self.w + '\n') * self.w

    def info(self):
        print(f"===Квадрат===\nСторона: {self.w}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр:"
              f" {self.perimeter()}\n{self.draw()} ")


class Rectangle(Share):
    def __init__(self, w, h, color):
        self.w = w
        self.h = h
        super().__init__(color)

    def perimeter(self):
        perimeter = self.w * 2 + self.h * 2
        return perimeter

    def square(self):
        return self.w * self.h

    def draw(self):
        return ('*' * self.h + '\n') * self.w

    def info(self):
        print(f"===Прямоугольник===\nСторона: {self.w}\nШирина: {self.h}\nЦвет: {self.color}"
              f"\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}\n{self.draw()} ")


class Triangle(Share):
    def __init__(self, w, h, l, color):
        self.w = w
        self.h = h
        self.l = l
        super().__init__(color)

    def perimeter(self):
        perimeter = self.w + self.h + self.l
        return perimeter

    def square(self):
        return round(self.w / 4 * math.sqrt(4 * self.h ** 2 - self.w ** 2), 2)

    def draw(self):
        rows = []
        for n in range(self.h):
            rows.append(" " * n + "*" * (self.w - 2 * n) + " " * n)
        return "\n".join(reversed(rows))

    def info(self):
        print(f"===Треугольник===\nСторона: {self.w}\nСторона 2: {self.h}\nСторона 3: {self.l}\nЦвет: {self.color}"
              f"\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}\n{self.draw()} ")


s = Square(3, 'red')
s.info()
s.draw()
r = Rectangle(3, 7, 'green')
r.info()
r.draw()
t = Triangle(11, 6, 6, "yellow")
t.info()
t.draw()


