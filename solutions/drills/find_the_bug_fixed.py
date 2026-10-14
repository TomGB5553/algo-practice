"""Fixed version of drills/find_the_bug.py. Each fix is explained in a '# BUG' comment."""


def sum_of_squares(numbers):
    total = 0
    for n in numbers:
        total += n * n  # BUG: `total = n*n` REPLACED the total at every turn; `+=` accumulates
    return total


def count_vowels(text):
    count = 0
    for letter in text:
        # BUG: `letter == "a" or "e" ...` is always True, because the non-empty string "e"
        # is "truthy". Each comparison must be written in full; `in` is shorter.
        if letter in "aeiou":
            count += 1
    return count


def sum_without_first(numbers):
    total = 0
    for i in range(len(numbers)):  # BUG: range(1, ...) starts at index 1 and skips index 0
        total += numbers[i]
    return total


def with_added(numbers, x):
    result = list(numbers)  # BUG: append on `numbers` modified the caller's list; work on a copy
    result.append(x)
    return result


def count_words(words):
    counts = {}
    for word in words:
        # BUG: counts[word] does not exist the first time -> KeyError.
        # .get(key, default) returns the default when the key is missing.
        counts[word] = counts.get(word, 0) + 1
    return counts


def largest(numbers):
    best = numbers[0]  # BUG: starting from 0 is wrong when all numbers are negative
    for n in numbers:
        if n > best:
            best = n
    return best


def names_of_adults(people):
    names = []
    for person in people:
        if person["age"] >= 18:
            names.append(person["name"])
    return names  # BUG: `return` was indented INSIDE the loop -> stopped after the 1st person


def biggest_number_in_text(values):
    # BUG: max() on strings compares text ("9" > "10"). Convert to int FIRST.
    return max(int(v) for v in values)


def double(n):
    return n * 2  # BUG: print shows the value but returns None. Use return.


def first_or_none(items):
    if len(items) == 0:  # BUG: items[0] on an empty list raises IndexError. Check first.
        return None
    return items[0]


def safe_get(data, key1, key2):
    # BUG: data[key1][key2] raises KeyError when a key is missing.
    if key1 not in data:
        return None
    return data[key1].get(key2)  # dict.get returns None when the key is missing


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1  # BUG: `count = ...` created a LOCAL variable; the
        # attribute must be changed through self.count
        return self.count


def sorted_copy(names):
    # BUG: list.sort() sorts IN PLACE and returns None. sorted(list) returns a new list.
    return sorted(names)


def append_to(x, items=None):
    # BUG: a default value `[]` is created ONCE and shared by all calls. Use None.
    if items is None:
        items = []
    items.append(x)
    return items


def even_nights(data):
    result = []
    for key in data:
        night = int(key)  # BUG: the keys are strings; "102" % 2 is an error. Convert first.
        if night % 2 == 0:
            result.append(night)
    return sorted(result)


def remove_negatives(numbers):
    # BUG: `result = numbers` is NOT a copy (same list, two names) and removing items from a
    # list while looping on it skips elements. Build a NEW list instead.
    result = []
    for n in numbers:
        if n >= 0:
            result.append(n)
    return result


def factorial(n):
    if n == 0:  # BUG: the base case was n == 1, so factorial(0) never stopped (0 -> -1 -> -2...)
        return 1
    return n * factorial(n - 1)


def count_targets(targets):
    count = 0
    for name in targets:
        if name != "longest":  # BUG: the summary key must not be counted
            count += 1
    return count
