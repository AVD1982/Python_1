class OldOrder:
    def __set_name__(self, owner, name):
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(f"{self.__name} число должно быть положительным")
        instance.__dict__[self.__name] = value


class Order:
    price = OldOrder()
    amount = OldOrder()

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def sum(self):
        return self.price * self.amount


o = Order('apple', 5, 10)
print(o.sum())
