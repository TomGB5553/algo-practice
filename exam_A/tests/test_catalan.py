import time

import pytest

EXPECTED = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]


def test_catalan():
    from src.catalan import catalan

    for n, expected in enumerate(EXPECTED):
        assert catalan(n) == expected, f"catalan({n}) should be {expected}"


def test_catalan_memo():
    from src.catalan import catalan_memo

    for n, expected in enumerate(EXPECTED):
        assert catalan_memo(n) == expected
    assert catalan_memo(30) == 3814986502092304
    # called twice in a row: the default cache must not be shared in a wrong way
    assert catalan_memo(10) == 16796
    assert catalan_memo(10) == 16796


def test_catalan_memo_is_fast_and_recursive():
    from src import catalan as module
    from tests.code_checks import called_names

    start = time.perf_counter()
    assert module.catalan_memo(200) > 0
    assert time.perf_counter() - start < 1.0, "catalan_memo(200) should be instant: is the cache really used?"
    assert "catalan_memo" in called_names(module.catalan_memo), "catalan_memo must be recursive (call itself)"


def test_catalan_iter():
    from src.catalan import catalan_iter

    for n, expected in enumerate(EXPECTED):
        assert catalan_iter(n) == expected
    assert catalan_iter(30) == 3814986502092304
    assert catalan_iter(500) > 0  # no recursion limit issue


def test_catalan_iter_is_not_recursive():
    from src import catalan as module
    from tests.code_checks import called_names

    assert "catalan_iter" not in called_names(module.catalan_iter), "catalan_iter must not call itself"
