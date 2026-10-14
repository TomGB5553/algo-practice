import pytest


def test_constructor_copies_the_list():
    from src.polynomial import Polynomial

    coeffs = [3, 2, 5]
    p = Polynomial(coeffs)
    assert p.coeffs == [3, 2, 5]
    coeffs.append(99)  # changing the original list...
    assert p.coeffs == [3, 2, 5], "the constructor must store a COPY of the list"


def test_repr():
    from src.polynomial import Polynomial

    assert repr(Polynomial([3, 2, 5])) == "Polynomial([3, 2, 5])"
    assert repr(Polynomial([])) == "Polynomial([])"


def test_degree():
    from src.polynomial import Polynomial

    assert Polynomial([3, 2, 5]).degree() == 2
    assert Polynomial([1, 2, 0, 0]).degree() == 1
    assert Polynomial([0, 0, 7]).degree() == 2
    assert Polynomial([7]).degree() == 0
    assert Polynomial([0, 0]).degree() == -1
    assert Polynomial([]).degree() == -1


def test_evaluate():
    from src.polynomial import Polynomial

    assert Polynomial([3, 2, 5]).evaluate(2) == 27
    assert Polynomial([3, 2, 5]).evaluate(0) == 3
    assert Polynomial([1, -1]).evaluate(10) == -9
    assert Polynomial([]).evaluate(5) == 0


def test_add():
    from src.polynomial import Polynomial

    p = Polynomial([1, 2])
    q = Polynomial([10, 20, 30])
    assert (p + q).coeffs == [11, 22, 30]
    assert (q + p).coeffs == [11, 22, 30]
    assert isinstance(p + q, Polynomial)
    assert p.coeffs == [1, 2] and q.coeffs == [10, 20, 30]  # not modified
    assert (Polynomial([]) + q).coeffs == [10, 20, 30]


def test_mul():
    from src.polynomial import Polynomial

    p = Polynomial([1, 1])
    assert (p * p).coeffs == [1, 2, 1]
    assert (Polynomial([1, 2, 3]) * Polynomial([4, 5])).coeffs == [4, 13, 22, 15]
    assert (Polynomial([2]) * Polynomial([1, 2, 3])).coeffs == [2, 4, 6]
    assert (Polynomial([]) * Polynomial([1, 2])).coeffs == []
    a = Polynomial([1, 2, 3])
    a * Polynomial([1, 1])
    assert a.coeffs == [1, 2, 3]  # not modified
