"""
DRILL 1 : FIND THE BUG
======================
Each function below is supposed to do what its docstring says, but it contains
ONE bug (a mistake that beginners often make).

How to work:
    1. run   python -m pytest drills/test_find_the_bug.py   (from the practice/ folder)
    2. read the failing test, then read the function
    3. fix the function in THIS file, run again
    4. when all the tests pass, write in a comment "# bug: ..." what the mistake was

Do not look at ../solutions/drills/ before you tried!
"""


def sum_of_squares(numbers):
    """Return 1*1 + 2*2 + ... : the sum of the squares of the numbers of the list."""
    total = 0
    for n in numbers:
        total = n * n
    return total


def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in the text (lowercase text)."""
    count = 0
    for letter in text:
        if letter == "a" or "e" or "i" or "o" or "u":
            count += 1
    return count


def sum_without_first(numbers):
    """Return the sum of ALL the numbers of the list (the first one included)."""
    total = 0
    for i in range(1, len(numbers)):
        total += numbers[i]
    return total


def with_added(numbers, x):
    """Return a NEW list made of `numbers` followed by x. `numbers` must NOT be modified."""
    numbers.append(x)
    return numbers


def count_words(words):
    """Return a dict {word: number of times it appears in the list}."""
    counts = {}
    for word in words:
        counts[word] += 1
    return counts


def largest(numbers):
    """Return the largest number of a non-empty list (the numbers may all be negative)."""
    best = 0
    for n in numbers:
        if n > best:
            best = n
    return best


def names_of_adults(people):
    """people = list of dicts {"name": str, "age": int}. Return the names of those aged 18 or more."""
    names = []
    for person in people:
        if person["age"] >= 18:
            names.append(person["name"])
        return names


def biggest_number_in_text(values):
    """values = list of STRINGS like ["10", "9", "100"] (as read from a CSV file).
    Return the biggest value as an INTEGER (here: 100)."""
    return max(values)


def double(n):
    """Return twice n (the result must be RETURNED, so that other code can use it)."""
    print(n * 2)


def first_or_none(items):
    """Return the first element of the list, or None if the list is empty."""
    return items[0]


def safe_get(data, key1, key2):
    """data is a dict of dicts. Return data[key1][key2], or None if key1 or key2 does not exist."""
    return data[key1][key2]


class Counter:
    """A counter that starts at 0 and goes up by 1 at each call of increment()."""

    def __init__(self):
        self.count = 0

    def increment(self):
        count = self.count + 1
        return self.count


def sorted_copy(names):
    """Return a NEW list with the names in alphabetical order. `names` is not modified."""
    result = names.sort()
    return result


def append_to(x, items=[]):
    """Return a list: `items` (empty list by default) with x added at the end.
    Two calls append_to(1) and append_to(2) must give [1] and [2]."""
    items.append(x)
    return items


def even_nights(data):
    """data is a dict whose keys are STRINGS of integers ("101", "102"...).
    Return the sorted list of the keys that are even numbers, as INTEGERS."""
    result = []
    for key in data:
        if key % 2 == 0:
            result.append(key)
    return sorted(result)


def remove_negatives(numbers):
    """Return a list without the negative numbers."""
    result = numbers
    for n in numbers:
        if n < 0:
            result.remove(n)
    return result


def factorial(n):
    """Return n! = 1*2*...*n, with 0! = 1. Use recursion."""
    if n == 1:
        return 1
    return n * factorial(n - 1)


def count_targets(targets):
    """targets is a dict like {"M31": {...}, "M42": {...}, "longest": {...}}.
    Return the number of real targets: the key "longest" is a summary, not a target."""
    return len(targets)
