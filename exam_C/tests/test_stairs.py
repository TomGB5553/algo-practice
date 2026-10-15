import time

import pytest

EXPECTED = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]


def test_ways():
    from src.stairs import ways

    for n, expected in enumerate(EXPECTED):
        assert ways(n) == expected, f"ways({n}) should be {expected}"


def test_ways_is_recursive():
    from src import stairs
    from tests.code_checks import called_names

    assert "ways" in called_names(stairs.ways)


def test_ways_memo():
    from src.stairs import ways_memo

    for n, expected in enumerate(EXPECTED):
        assert ways_memo(n) == expected
    assert ways_memo(40) == 23837527729
    # twice in a row: the cache must not be shared in a wrong way
    assert ways_memo(12) == 927
    assert ways_memo(12) == 927


def test_ways_memo_is_fast_recursive_and_uses_a_dict():
    from src import stairs as module
    from tests.code_checks import called_names

    start = time.perf_counter()
    assert module.ways_memo(300) > 0
    assert time.perf_counter() - start < 1.0, "ways_memo(300) should be instant: is the cache really used?"
    assert "ways_memo" in called_names(module.ways_memo), "ways_memo must be recursive"


def test_ways_memo_accepts_a_cache():
    from src.stairs import ways_memo

    cache = {}
    assert ways_memo(10, cache) == 274
    assert len(cache) > 0, "the dictionary given by the caller must be filled"


def test_ways_iter():
    from src.stairs import ways_iter

    for n, expected in enumerate(EXPECTED):
        assert ways_iter(n) == expected
    assert ways_iter(40) == 23837527729
    assert ways_iter(2000) > 0  # no recursion limit issue


def test_ways_iter_is_not_recursive():
    from src import stairs as module
    from tests.code_checks import called_names

    assert "ways_iter" not in called_names(module.ways_iter)


def test_stirling2_small_values():
    from src.stairs import stirling2

    assert stirling2(0, 0) == 1
    assert stirling2(3, 0) == 0
    assert stirling2(0, 3) == 0
    assert stirling2(1, 1) == 1
    assert stirling2(3, 2) == 3
    assert stirling2(4, 2) == 7
    assert stirling2(5, 3) == 25
    assert stirling2(3, 5) == 0  # more groups than elements


def test_stirling2_big_and_repeated():
    from src.stairs import stirling2

    assert stirling2(10, 3) == 9330
    assert stirling2(10, 3) == 9330  # twice in a row
    assert stirling2(25, 10) == 1203163392175387500


def test_stirling2_is_fast_recursive_and_key_is_a_tuple():
    from src import stairs as module
    from tests.code_checks import called_names

    start = time.perf_counter()
    assert module.stirling2(60, 20) > 0
    assert time.perf_counter() - start < 1.0, "stirling2(60, 20) should be instant: cache key must hold BOTH n and k"
    assert "stirling2" in called_names(module.stirling2)


def test_stirling2_fills_the_given_cache_with_pairs():
    from src.stairs import stirling2

    cache = {}
    stirling2(6, 3, cache)
    assert (6, 3) in cache and cache[(6, 3)] == 90


def test_main_stairs(capsys):
    import runpy

    runpy.run_path("main_stairs.py")
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == ["ways(40) = 23837527729", "S(10, 3) = 9330"]
