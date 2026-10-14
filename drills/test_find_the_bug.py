import pytest

import drills.find_the_bug as b


def test_sum_of_squares():
    assert b.sum_of_squares([1, 2, 3]) == 14
    assert b.sum_of_squares([]) == 0


def test_count_vowels():
    assert b.count_vowels("banana") == 3
    assert b.count_vowels("rhythm") == 0


def test_sum_without_first():
    assert b.sum_without_first([5, 1, 2]) == 8
    assert b.sum_without_first([7]) == 7


def test_with_added():
    original = [1, 2]
    result = b.with_added(original, 3)
    assert result == [1, 2, 3]
    assert original == [1, 2], "the input list must not be modified"


def test_count_words():
    assert b.count_words(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_largest():
    assert b.largest([3, 9, 2]) == 9
    assert b.largest([-5, -2, -9]) == -2


def test_names_of_adults():
    people = [{"name": "A", "age": 20}, {"name": "B", "age": 10}, {"name": "C", "age": 18}]
    assert b.names_of_adults(people) == ["A", "C"]


def test_biggest_number_in_text():
    assert b.biggest_number_in_text(["10", "9", "100"]) == 100
    assert b.biggest_number_in_text(["9", "10"]) == 10


def test_double():
    assert b.double(4) == 8


def test_first_or_none():
    assert b.first_or_none([4, 5]) == 4
    assert b.first_or_none([]) is None


def test_safe_get():
    data = {"a": {"x": 1}}
    assert b.safe_get(data, "a", "x") == 1
    assert b.safe_get(data, "a", "y") is None
    assert b.safe_get(data, "z", "x") is None


def test_counter():
    c = b.Counter()
    c.increment()
    c.increment()
    assert c.count == 2


def test_sorted_copy():
    names = ["bob", "al", "cy"]
    assert b.sorted_copy(names) == ["al", "bob", "cy"]
    assert names == ["bob", "al", "cy"]


def test_append_to():
    assert b.append_to(1) == [1]
    assert b.append_to(2) == [2]
    assert b.append_to(3, [1, 2]) == [1, 2, 3]


def test_even_nights():
    assert b.even_nights({"101": 0, "102": 0, "104": 0, "7": 0}) == [102, 104]


def test_remove_negatives():
    original = [-1, -2, 3, -4, 5]
    assert b.remove_negatives(original) == [3, 5]
    assert original == [-1, -2, 3, -4, 5], "the input list must not be modified"


def test_factorial():
    assert b.factorial(0) == 1
    assert b.factorial(1) == 1
    assert b.factorial(5) == 120


def test_count_targets():
    assert b.count_targets({"M31": {}, "M42": {}, "longest": {}}) == 2
