import pytest

import drills.write_from_scratch as w
from drills.code_checks import called_names, uses_power_operator


def test_count_even():
    assert w.count_even([1, 2, 4, 7]) == 2
    assert w.count_even([]) == 0
    assert w.count_even([-2, 0, 3]) == 2


def test_running_sum():
    assert w.running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert w.running_sum([]) == []
    assert w.running_sum([5]) == [5]


def test_second_largest():
    assert w.second_largest([4, 9, 9, 7]) == 7
    assert w.second_largest([5, 5]) is None
    assert w.second_largest([]) is None
    assert w.second_largest([-3, -1, -2]) == -2
    assert w.second_largest([1, 2]) == 1


def test_is_palindrome():
    assert w.is_palindrome("Never odd or even") is True
    assert w.is_palindrome("hello") is False
    assert w.is_palindrome("") is True
    assert w.is_palindrome("a") is True


def test_word_frequencies():
    assert w.word_frequencies("the cat the dog") == {"the": 2, "cat": 1, "dog": 1}
    assert w.word_frequencies("The the THE") == {"the": 3}
    assert w.word_frequencies("") == {}


def test_invert_dict():
    assert w.invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert w.invert_dict({}) == {}


def test_group_by_length():
    assert w.group_by_length(["a", "bb", "c", "dd", "eee"]) == {1: ["a", "c"], 2: ["bb", "dd"], 3: ["eee"]}
    assert w.group_by_length([]) == {}


def test_nested_get():
    assert w.nested_get({"a": {"b": {"c": 5}}}, ["a", "b", "c"]) == 5
    assert w.nested_get({"a": {"b": 1}}, ["a", "x", "c"], 0) == 0
    assert w.nested_get({"a": 1}, ["a", "b"]) is None  # 1 is not a dict: stop with default
    assert w.nested_get({"a": 1}, []) == {"a": 1}


def test_top_n_by():
    items = [{"v": 1}, {"v": 9}, {"v": 5}]
    assert w.top_n_by(items, "v", 2) == [{"v": 9}, {"v": 5}]
    assert w.top_n_by(items, "v", 10) == [{"v": 9}, {"v": 5}, {"v": 1}]
    assert items == [{"v": 1}, {"v": 9}, {"v": 5}]  # not modified
    assert w.top_n_by([], "v", 3) == []


def test_remove_duplicates():
    assert w.remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert w.remove_duplicates([]) == []
    assert w.remove_duplicates(["a", "a"]) == ["a"]


def test_transpose():
    assert w.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert w.transpose([[1], [2], [3]]) == [[1, 2, 3]]
    assert w.transpose([]) == []


def test_rotate_right():
    assert w.rotate_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert w.rotate_right([1, 2, 3], 0) == [1, 2, 3]
    assert w.rotate_right([1, 2, 3], 4) == [3, 1, 2]
    assert w.rotate_right([], 3) == []
    original = [1, 2, 3]
    w.rotate_right(original, 1)
    assert original == [1, 2, 3]


def test_merge_sorted():
    assert w.merge_sorted([1, 4, 6], [2, 3, 7, 8]) == [1, 2, 3, 4, 6, 7, 8]
    assert w.merge_sorted([], [1, 2]) == [1, 2]
    assert w.merge_sorted([1, 2], []) == [1, 2]
    assert w.merge_sorted([1, 1], [1]) == [1, 1, 1]
    assert "sorted" not in called_names(w.merge_sorted) and "sort" not in called_names(w.merge_sorted)


def test_index_of():
    numbers = list(range(0, 2000, 2))
    assert w.index_of(numbers, 0) == 0
    assert w.index_of(numbers, 1998) == 999
    assert w.index_of(numbers, 500) == 250
    assert w.index_of(numbers, 501) == -1
    assert w.index_of([], 3) == -1


def test_balanced():
    assert w.balanced("([]{})") is True
    assert w.balanced("(]") is False
    assert w.balanced("((") is False
    assert w.balanced("") is True
    assert w.balanced("a(b)c") is True
    assert w.balanced(")(") is False


def test_digit_sum():
    assert w.digit_sum(1234) == 10
    assert w.digit_sum(0) == 0
    assert w.digit_sum(7) == 7
    assert "str" not in called_names(w.digit_sum)
    assert "digit_sum" in called_names(w.digit_sum), "use recursion"


def test_power():
    assert w.power(2, 10) == 1024
    assert w.power(3, 0) == 1
    assert w.power(5, 1) == 5
    assert w.power(2, 100) == 2 ** 100
    assert not uses_power_operator(w.power), "do not use the operator **"
    assert "power" in called_names(w.power), "use recursion"


def test_count_change():
    assert w.count_change(4, [1, 2]) == 3
    assert w.count_change(0, [5]) == 1
    assert w.count_change(3, [2]) == 0
    assert w.count_change(10, [1, 5, 10]) == 4
    assert w.count_change(100, [1, 5, 10, 25]) == 242
