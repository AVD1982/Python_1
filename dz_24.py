class Abc:
    def __init__(self, kg=0):
        self.__kg = kg

    @property
    def kg_kg(self):
        return self.__kg

    @kg_kg.setter
    def kg_kg(self, kg):
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            print("Килограммы должны быть заданы числами")

    def to_pounds(self):
        return round(self.__kg * 2.205, 2)


s1 = Abc(12)
print(s1.kg_kg, "кг =>", end="")
print(s1.to_pounds(), " фунты ")
s1.kg_kg = 41
print(s1.kg_kg, "кг =>", end="")
print(s1.to_pounds(), " фунты ")

