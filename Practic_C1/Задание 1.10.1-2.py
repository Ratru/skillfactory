# Задание 1.10.1
class Rectangle_figure:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_atribute(self):
        return f"Rectangle {self.x} {self.y} {self.width} {self.height}"


rectangle_1 = Rectangle_figure(5, 10, 50, 100)

print(rectangle_1.get_atribute())


# Задание 1.10.2
class Rectangle_figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return f"Rectangle {self.width} {self.height} {self.width * self.height}"


rectangle_1_new = Rectangle_figure(5, 10)
print(rectangle_1_new.get_area())