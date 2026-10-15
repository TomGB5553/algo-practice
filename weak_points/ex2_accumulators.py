"""
EX 2 : ACCUMULATORS   (your mistakes: `min, max = None`, `count` never incremented, `list = []` INSIDE the loop,
                       `counts[method] = sum.get(...)` copy-paste, `out[planet]` instead of `out[planet["Method"]]`,
                       variables named `sum`, `list`, `min`, `max` that hide the Python functions)

The 5 questions to ask BEFORE writing the loop:
   1. What do I start from?  (0, [], {}, None)     2. Where is it created? (BEFORE the loop)
   3. What changes at each turn?                    4. What if the input is empty?   5. What do I return?
Do NOT use the built-ins sum / min / max / sorted unless the statement says you can.
"""


def average(numbers):
    """Mean of a list, None if the list is empty. average([1, 2, 6]) -> 3.0"""
    raise NotImplementedError


def min_and_max(numbers):
    """(smallest, largest) with a loop, or None if the list is empty.  min_and_max([3, 9, 1]) -> (1, 9)"""
    raise NotImplementedError


def index_of_max(numbers):
    """Index of the first occurrence of the largest value, -1 if empty. index_of_max([2, 9, 9, 1]) -> 1"""
    raise NotImplementedError


def longest_word(words):
    """The longest word (the first one if there are ties), None if the list is empty."""
    raise NotImplementedError


def count_by_first_letter(words):
    """{first letter: number of words}   ["apple", "avocado", "kiwi"] -> {"a": 2, "k": 1}. Ignore empty strings."""
    raise NotImplementedError


def average_by_group(pairs):
    """pairs = [(group, value), ...]  ->  {group: average of its values}
    [("a", 1), ("b", 10), ("a", 3)] -> {"a": 2.0, "b": 10.0}
    You need TWO dictionaries (or one dict of lists): one for the totals, one for the counts.
    """
    raise NotImplementedError


def group_by_length(words):
    """{length: [words of that length, in original order]}   ["a", "bb", "c"] -> {1: ["a", "c"], 2: ["bb"]}"""
    raise NotImplementedError


def best_per_group(records, group_field, value_field):
    """records = list of dicts. For each group return the NAME ("name" field) of the record with the biggest value.
    records = [{"name": "A", "g": 1, "v": 5}, {"name": "B", "g": 1, "v": 9}, {"name": "C", "g": 2, "v": 1}]
    best_per_group(records, "g", "v") -> {1: "B", 2: "C"}
    """
    raise NotImplementedError


def second_largest(numbers):
    """Second largest DISTINCT value, None if there is none.  [3, 9, 5, 9] -> 5     [4, 4] -> None"""
    raise NotImplementedError


def count_while(numbers, condition):
    """Number of elements at the BEGINNING of the list for which condition(x) is True, stopping at the first False.
    count_while([2, 4, 5, 6], lambda x: x % 2 == 0) -> 2
    """
    raise NotImplementedError
