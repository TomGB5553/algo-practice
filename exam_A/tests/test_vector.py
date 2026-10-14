import pytest


def test_constructor():
    from src.vector import Vector2D

    v = Vector2D(3, -1)
    assert v.x == 3
    assert v.y == -1


def test_add_returns_new_vector():
    from src.vector import Vector2D

    a = Vector2D(1, 2)
    b = Vector2D(10, 20)
    c = a + b
    assert isinstance(c, Vector2D)
    assert (c.x, c.y) == (11, 22)
    # the operands must not be modified, and c must be a NEW object
    assert (a.x, a.y) == (1, 2)
    assert (b.x, b.y) == (10, 20)
    assert c is not a and c is not b


def test_repr():
    from src.vector import Vector2D

    assert repr(Vector2D(3, -1)) == "Vector2D(3, -1)"
    assert str(Vector2D(0.5, 2)) == "Vector2D(0.5, 2)"


def test_norm_squared_and_lt():
    from src.vector import Vector2D

    assert Vector2D(3, 4).norm_squared() == 25
    short = Vector2D(1, 1)
    long = Vector2D(-5, 0)
    assert (short < long) is True
    assert (long < short) is False
    assert (short < Vector2D(-1, -1)) is False  # same length: not strictly smaller


def test_mul():
    from src.vector import Vector2D

    v = Vector2D(1, -2)
    w = v * 3
    assert isinstance(w, Vector2D)
    assert (w.x, w.y) == (3, -6)
    assert (v.x, v.y) == (1, -2)  # v unchanged
