class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area_square(self):
        return self.a ** 2


# возведение в степень **2 (в квадрат)

class Circle:
    def __init__(self, r, pi=3.14):
        self.r = r
        self.pi = pi

    def get_area_circle(self):
        return (self.r ** 2) * self.pi
