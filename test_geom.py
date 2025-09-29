import math
import pytest
from geom import Circle, Triangle, area


def test_circle_area():
    c = Circle(3)
    assert math.isclose(c.area(), math.pi * 9, rel_tol=1e-12)


def test_circle_invalid():
    try:
        Circle(0)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"


def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-12)


def test_triangle_invalid():
    try:
        Triangle(1, 2, 3)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError"


def test_triangle_is_right():
    t = Triangle(3, 4, 5)
    assert t.is_right()
    t2 = Triangle(2, 3, 4)
    assert not t2.is_right()


def test_area_function():
    c = Circle(2)
    t = Triangle(3, 4, 5)
    assert math.isclose(area(c), math.pi * 4, rel_tol=1e-12)
    assert math.isclose(area(t), 6.0, rel_tol=1e-12)