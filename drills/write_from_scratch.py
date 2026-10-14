"""
DRILL 2 : WRITE FROM SCRATCH
============================
Each function is empty (`raise NotImplementedError`). Write it, then run

    python -m pytest drills/test_write_from_scratch.py -k name_of_the_function

(from the practice/ folder). The functions are ordered from easy to hard.

THE METHOD (see ../HOW_TO_REASON.md) before writing any code:
    1. Rewrite the problem with YOUR words: what is the input, what is the output?
    2. Take the example of the docstring and solve it BY HAND on paper. Which steps did you do?
    3. Which kind of loop is it? (count / accumulate / find the best / filter / build a dict)
    4. What happens with the EMPTY input? with ONE element?
    5. Write the code. Then run the tests.
"""


# ---------------------------------------------------------------- level 1 : one loop

def count_even(numbers):
    """Return how many numbers of the list are even.   [1, 2, 4, 7] -> 2"""
    raise NotImplementedError


def running_sum(numbers):
    """Return the list of the partial sums.   [1, 2, 3, 4] -> [1, 3, 6, 10]   [] -> []"""
    raise NotImplementedError


def second_largest(numbers):
    """Return the second largest DISTINCT value, or None if there are fewer than 2 distinct values.
    [4, 9, 9, 7] -> 7     [5, 5] -> None
    (Do not use sorted() or max() on the whole list: use one loop and two variables.)"""
    raise NotImplementedError


def is_palindrome(text):
    """True if the text reads the same backwards, ignoring upper/lower case and spaces.
    "Never odd or even" -> True     "hello" -> False"""
    raise NotImplementedError


# ---------------------------------------------------------------- level 2 : dictionaries

def word_frequencies(text):
    """Return {word: number of times it appears}, words in lowercase, separated by spaces.
    "the cat the dog" -> {"the": 2, "cat": 1, "dog": 1}"""
    raise NotImplementedError


def invert_dict(d):
    """Swap keys and values (all the values are different).   {"a": 1, "b": 2} -> {1: "a", 2: "b"}"""
    raise NotImplementedError


def group_by_length(words):
    """Return {length: list of the words of that length, in the original order}.
    ["a", "bb", "c", "dd", "eee"] -> {1: ["a", "c"], 2: ["bb", "dd"], 3: ["eee"]}"""
    raise NotImplementedError


def nested_get(data, keys, default=None):
    """Follow a path of keys in nested dictionaries; return `default` if the path does not exist.
    nested_get({"a": {"b": {"c": 5}}}, ["a", "b", "c"]) -> 5
    nested_get({"a": {"b": 1}}, ["a", "x", "c"], 0) -> 0"""
    raise NotImplementedError


def top_n_by(items, field, n):
    """items is a list of dicts. Return the n dicts with the biggest value of `items[i][field]`,
    biggest first. (Fewer than n items -> return all of them.)
    top_n_by([{"v": 1}, {"v": 9}, {"v": 5}], "v", 2) -> [{"v": 9}, {"v": 5}]"""
    raise NotImplementedError


# ---------------------------------------------------------------- level 3 : lists and indices

def remove_duplicates(items):
    """Return a new list without duplicates, keeping the order of the first appearances.
    [3, 1, 3, 2, 1] -> [3, 1, 2]"""
    raise NotImplementedError


def transpose(matrix):
    """matrix is a list of rows (all of the same length). Return the transposed matrix.
    [[1, 2, 3], [4, 5, 6]] -> [[1, 4], [2, 5], [3, 6]]"""
    raise NotImplementedError


def rotate_right(items, k):
    """Return a new list rotated by k places to the right (k can be bigger than the length).
    [1, 2, 3, 4, 5], 2 -> [4, 5, 1, 2, 3]      [] -> []"""
    raise NotImplementedError


def merge_sorted(a, b):
    """Merge two lists that are ALREADY sorted into one sorted list, in ONE pass
    (two indices i and j, no sorted() call).   [1, 4, 6], [2, 3, 7, 8] -> [1, 2, 3, 4, 6, 7, 8]"""
    raise NotImplementedError


def index_of(sorted_numbers, target):
    """Binary search: return the index of target in the sorted list, or -1. O(log n) required
    (do NOT slice the list)."""
    raise NotImplementedError


def balanced(text):
    """True if every bracket ( [ { of the text is closed by the matching one in the right order.
    "([]{})" -> True     "(]" -> False     "((" -> False     "" -> True
    Hint: a list used as a stack (append / pop)."""
    raise NotImplementedError


# ---------------------------------------------------------------- level 4 : recursion

def digit_sum(n):
    """Sum of the digits of a non-negative integer, with recursion and NO str().  1234 -> 10
    Hint: n % 10 is the last digit, n // 10 is the number without its last digit."""
    raise NotImplementedError


def power(x, n):
    """x ** n for an integer n >= 0 using recursion and the fact that x**n = (x**(n//2))**2
    (times x if n is odd). Do not use the operator **. It must need only about log2(n) calls."""
    raise NotImplementedError


def count_change(amount, coins):
    """Number of different ways to pay `amount` with the coin values of the list (each value can be
    used any number of times; the order does not matter).
    count_change(4, [1, 2]) -> 3     (1+1+1+1, 1+1+2, 2+2)
    count_change(0, [5]) -> 1        count_change(3, [2]) -> 0
    Hint: the ways either do not use the first coin at all, or use it at least once."""
    raise NotImplementedError
