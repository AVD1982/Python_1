class Student:
    def __init__(self, name):
        self.name = name
        self.n = self.Laptop()

    def show(self):
        print(self.name, end="")
        self.n.show()

    class Laptop:
        def __init__(self):
            self.model = 'hp'
            self.processor = 'i7'
            self.memory = 16

        def show(self):
            print(f' => {self.memory}, {self.processor}, {self.memory}')


p = Student('Roman')
p2 = Student('Vladimir')
p.show()
p2.show()