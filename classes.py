import math


class Shape:
    """Might get rid of that and rename Shape2D and add other properties, like volume, for example."""

    def area(self):
        pass


class Shape2D(Shape):

    def __init__(self):
        super().__init__()

    def perimeter(self):
        pass


class Circle(Shape2D):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return math.pi * pow(self.radius, 2)

    @classmethod
    def perimeter(cls, self):
        return 2 * math.pi * self.radius


class Square(Shape2D):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return pow(self.side, 2)

    def perimeter(self):
        return self.side * 4


class Rectangle(Shape2D):

    def __init__(self, side1, side2):
        super().__init__()
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return (self.side1 + self.side2) * 2


class Triangle(Shape2D):

    def __init__(self, side1, side2, side3):
        super().__init__()
        if self.triangle_impossible(side1, side2, side3):
            raise ValueError
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def triangle_impossible(a, b, c):
        return a + b <= c or a + c <= b or b + c <= a

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


class Trapeze(Shape2D):

    def __init__(self, base1, base2, side1, side2):
        super().__init__()
        if self.trapeze_impossible(base1, base2, side1, side2):
            raise ValueError
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    @staticmethod
    def trapeze_impossible(base1, base2, side1, side2):
        return Triangle.triangle_impossible(abs(base2 - base1), side1, side2)

    def area(self):
        return (self.base1 + self.base2) * 0.5 \
               * math.sqrt(self.side1 ** 2 - (((self.base2 - self.base1) ** 2
                                               + self.side1 ** 2 - self.side2 ** 2) / (
                                                      2 * (self.base2 - self.base1))) ** 2)

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2


class Rhombus(Shape2D):

    def __init__(self, diag1, diag2):
        super().__init__()
        self.diag1 = diag1
        self.diag2 = diag2

    def area(self):
        return self.diag1 * self.diag2 * 0.5

    def perimeter(self):
        return math.hypot(self.diag1 / 2, self.diag2 / 2) * 4


class Sphere(Circle):

    def area(self):
        return 4 * math.pi * self.radius ** 3

    def volume(self):
        return 4 / 3 * math.pi * self.radius ** 3


class Cube(Square):

    def area(self):
        return 6 * self.side ** 2

    def perimeter(self):
        return 12 * self.side

    def volume(self):
        return self.side ** 3


class Parallelepiped(Rectangle):

    def __init__(self, height):
        super().__init__()
        self.height = height

    def area(self):
        return 2 * (self.side1 * self.height + self.side1 * self.side2 + self.side2 * self.height)

    def perimeter(self):
        return 4 * (self.side1 + self.side2 + self.height)

    def volume(self):
        return self.side1 * self.side2 * self.height


class Pyramid(Square):

    def __init__(self, height):
        super().__init__()
        self.height = height
        self.face_median = math.hypot(self.height, self.side / 2)

    def area(self):
        return 2 * self.side * self.face_median + self.side * (self.side + 2 * self.face_median)

    def volume(self):
        return 1 / 3 * pow(self.side, 2) * self.height


class Cylinder(Circle):

    def __init__(self, height, radius):
        super().__init__(radius)
        self.height = height

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.height * self.radius ** 2


class Cone(Cylinder):

    def __init__(self, height, radius):
        super().__init__(height, radius)
        self.edge = math.hypot(self.radius, self.height)

    def area(self):
        return math.pi * self.radius * (self.edge + self.radius)

    def volume(self):
        return (1 / 3) * math.pi * self.radius ** 2 * self.height
