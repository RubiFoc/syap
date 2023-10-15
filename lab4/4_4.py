# Задание 4:
# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса. – 1 – 3 балла
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    @staticmethod
    def is_square(length, width):
        return length == width

    @classmethod
    def create_square(cls, side_length):
        return cls(side_length, side_length)

    def __str__(self):
        return f"Четырёхугольник с длинной {self.length} и шириной {self.width}"

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width


rect1 = Rectangle(4, 6)
rect2 = Rectangle(3, 3)

print("Площадь прямоугольника 1:", rect1.area())
print("Площадь прямоугольника 2:", rect2.area())

print("Является ли прямоугольник 2 квадратом?", Rectangle.is_square(rect2.length, rect2.width))

square = Rectangle.create_square(5)
print("Созданный квадрат:", square)

print(rect1)

print("Прямоугольник 1 и прямоугольник 2 равны?", rect1 == rect2)