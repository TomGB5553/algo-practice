"""
EX 3 : WHAT DOES THE FUNCTION RETURN, WHAT DOES IT MODIFY?
   (your mistakes: `return out.sort()` -> None, `list.append(a, b)`, `out.append(collect_infix(...))` nesting a list,
    returning None for an empty input when the statement implies [], forgetting to copy the input)

Rules of the exercise:
  * "returns a NEW list" means the input list must be exactly the same afterwards (the checker verifies it)
  * `sort()`, `append()`, `extend()`, `insert()`, `remove()`, `reverse()` all return None
  * `append(x)` adds ONE element, `extend(l)` adds the elements of l, `+` builds a new list
"""


def sorted_unique(l):
    """New sorted list without duplicates. sorted_unique([3, 1, 3, 2]) -> [1, 2, 3]. Input not modified."""
    return sorted(set(l))


def with_item(l, x):
    """New list = l followed by x. The input list is NOT modified. with_item([1, 2], 3) -> [1, 2, 3]"""
    return l + [x]


def without_value(l, value):
    """New list without any occurrence of value. Input not modified. without_value([1, 2, 1, 3], 1) -> [2, 3]"""
    return [x for x in l if x != value]


def add_in_place(l, x):
    """MODIFY l by appending x and return NOTHING (None). The caller's list must be changed."""
    l.append(x)


def flatten_once(list_of_lists):
    """[[1, 2], [3], [], [4, 5]] -> [1, 2, 3, 4, 5]  (use extend, or +, NOT append)"""
    result = []
    for sub in list_of_lists:
        result.extend(sub)
    return result


def interleave(a, b):
    """Alternate the elements of a and b, then the leftovers. interleave([1, 2, 3], ["a"]) -> [1, "a", 2, 3]"""
    result = []
    for i in range(max(len(a), len(b))):
        if i < len(a):
            result.append(a[i])
        if i < len(b):
            result.append(b[i])
    return result


def names_between(people, first_year, last_year):
    """people = list of dicts {"name": ..., "year": ...}.
    Sorted list of the NAMES of the people with first_year <= year <= last_year (both included).
    Return [] (not None!) when nobody matches.
    """
    names = []
    for p in people:
        if first_year <= p["year"] <= last_year:
            names.append(p["name"])
    return sorted(names)


def top_n(items, n=3):
    """The n biggest numbers, biggest first. The input is not modified. top_n([4, 9, 1, 7], 2) -> [9, 7]"""
    return sorted(items, reverse=True)[:n]


def top_n_pairs(pairs, n=3):
    """pairs = [(name, score), ...] -> the n pairs with the biggest score, biggest first (stable on ties).
    top_n_pairs([("a", 1), ("b", 5), ("c", 3)], 2) -> [("b", 5), ("c", 3)]
    """
    return sorted(pairs, key=lambda p: p[1], reverse=True)[:n]


def normalize(numbers):
    """New list where each number is divided by the largest one. Input not modified. [1, 2, 4] -> [0.25, 0.5, 1.0]
    Empty list -> []. (If the largest is 0, return a list of zeros.)"""
    if len(numbers) == 0:
        return []
    biggest = max(numbers)
    if biggest == 0:
        return [0 for _ in numbers]
    return [x / biggest for x in numbers]


def reverse_copy(l):
    """New reversed list, input untouched (not l.reverse() which returns None and modifies)."""
    return l[::-1]


def remove_negatives_in_place(l):
    """MODIFY l: remove all the negative numbers, return None. [1, -2, 3, -4] -> l becomes [1, 3]
    Careful: removing from a list while looping over it skips elements. Hint: slice assignment l[:] = ..."""
    l[:] = [x for x in l if x >= 0]


def merge_dicts_sum(a, b):
    """New dict: keys of a and b, values added when the key is in both. Inputs not modified.
    {"x": 1, "y": 2} and {"y": 5, "z": 1} -> {"x": 1, "y": 7, "z": 1}"""
    result = dict(a)
    for k, v in b.items():
        result[k] = result.get(k, 0) + v
    return result


def swap_first_last(l):
    """New list with the first and the last element swapped (a list of 0 or 1 element is returned as a copy)."""
    result = l[:]
    if len(result) >= 2:
        result[0], result[-1] = result[-1], result[0]
    return result
