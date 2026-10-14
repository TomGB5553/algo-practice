import time


def test_grid_paths():
    from src.paths import grid_paths

    assert grid_paths(1, 1) == 1
    assert grid_paths(1, 9) == 1
    assert grid_paths(9, 1) == 1
    assert grid_paths(2, 2) == 2
    assert grid_paths(3, 3) == 6
    assert grid_paths(3, 7) == 28
    assert grid_paths(7, 3) == 28


def test_grid_paths_memo():
    from src.paths import grid_paths_memo

    assert grid_paths_memo(3, 3) == 6
    assert grid_paths_memo(3, 7) == 28
    assert grid_paths_memo(3, 7) == 28  # twice in a row
    start = time.perf_counter()
    assert grid_paths_memo(18, 18) == 2333606220
    assert grid_paths_memo(60, 60) > 0
    assert time.perf_counter() - start < 1.0, "the cache is not used"
    from tests.code_checks import called_names

    assert "grid_paths_memo" in called_names(grid_paths_memo), "it must be recursive"


def test_binary_strings():
    from src.paths import binary_strings

    assert binary_strings(0) == [""]
    assert binary_strings(1) == ["0", "1"]
    assert binary_strings(2) == ["00", "01", "10", "11"]
    assert binary_strings(3) == ["000", "001", "010", "011", "100", "101", "110", "111"]
    assert len(binary_strings(10)) == 1024


def test_flatten():
    from src.paths import flatten

    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert flatten([[[[7]]]]) == [7]
    assert flatten([[], [1, []], 2]) == [1, 2]
    nested = [1, [2, 3]]
    flatten(nested)
    assert nested == [1, [2, 3]]  # input not modified
