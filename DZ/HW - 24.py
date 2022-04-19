
class Mass:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, k):
        if isinstance(k, (int, float)):
            self.__kg = k
        else:
            raise ValueError("Килограммы задаются только числами: ")

    def print_kg(self):
        return self.__kg * 2.2


m1 = Mass(12)
print(m1.kg, "кг =>", (round(m1.print_kg(), 2)), "фунтов")
# a = int(input("Введите число в кг: "))
m1.kg = 41
print(m1.kg, "кг =>", (round(m1.print_kg(), 2)), "фунтов")
m1.kg = "abc"
print(m1.kg, "кг =>", (round(m1.print_kg(), 2)), "фунтов")

