import math


class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be > 0")
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * self.radius * self.radius


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        a, b, c = float(a), float(b), float(c)
        if min(a, b, c) <= 0:
            raise ValueError("Sides must be > 0")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle inequality violated")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        # Формула Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        a, b, c = sorted([self.a, self.b, self.c])
        return math.isclose(a * a + b * b, c * c, rel_tol=1e-9, abs_tol=1e-9)


def area(obj) -> float:
    """Универсальная функция площади, не зная тип фигуры."""
    return obj.area()
