"""
RECURSION ON LISTS, STRINGS, NESTED LISTS, "ALL THE ..." GENERATORS

Run:  python3 snippets/recursion_on_structures.py

THE IDEA : the input shrinks by ONE element (or is cut in half) at each call.
    list  : first element = l[0], the rest = l[1:]            (empty list = base case)
    string: first char    = s[0], the rest = s[1:]            (empty string = base case)
    halves: middle = len(l) // 2, left = l[:middle], right = l[middle:]

BUILDING A LIST RECURSIVELY : the classic mistakes
    result.append(f(rest))   -> appends a LIST inside the list (nested list)       WRONG
    result = f(rest) + [x]   -> concatenation of two lists                          OK
    result.extend(f(rest))   -> adds the elements one by one                        OK
"""


# ---------------------------------------------------------------------------------------------
# A. LISTS : one element at a time              time O(n) (but l[1:] copies: really O(n^2) in total)
# ---------------------------------------------------------------------------------------------
def list_sum(l):
    if not l:                       # empty list
        return 0
    return l[0] + list_sum(l[1:])


def list_max(l):
    """Largest element of a NON-EMPTY list."""
    if len(l) == 1:
        return l[0]
    rest_max = list_max(l[1:])
    return l[0] if l[0] > rest_max else rest_max


def list_count(l, value):
    if not l:
        return 0
    return (1 if l[0] == value else 0) + list_count(l[1:], value)


def list_reverse(l):
    if not l:
        return []
    return list_reverse(l[1:]) + [l[0]]       # + between LISTS, so [l[0]] and not l[0]


def list_contains(l, value):
    if not l:
        return False
    return l[0] == value or list_contains(l[1:], value)


# same with an INDEX instead of slicing (no copies: O(n) in total) : the recursion carries `i`
def list_sum_index(l, i=0):
    if i == len(l):
        return 0
    return l[i] + list_sum_index(l, i + 1)


# ---------------------------------------------------------------------------------------------
# B. STRINGS
# ---------------------------------------------------------------------------------------------
def string_reverse(s):
    if s == "":
        return ""
    return string_reverse(s[1:]) + s[0]


def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])     # compare ends, then inner part


def count_char(s, c):
    if s == "":
        return 0
    return (1 if s[0] == c else 0) + count_char(s[1:], c)


def remove_char(s, c):
    if s == "":
        return ""
    rest = remove_char(s[1:], c)
    return rest if s[0] == c else s[0] + rest


def balanced_parentheses(s, open_count=0):
    """True if every '(' is closed. `open_count` = number of '(' still open (accumulator argument)."""
    if open_count < 0:
        return False
    if s == "":
        return open_count == 0
    if s[0] == "(":
        return balanced_parentheses(s[1:], open_count + 1)
    if s[0] == ")":
        return balanced_parentheses(s[1:], open_count - 1)
    return balanced_parentheses(s[1:], open_count)


# ---------------------------------------------------------------------------------------------
# C. DIVIDE AND CONQUER (halves)   time O(n) for sum/max, O(log n) for binary search
# ---------------------------------------------------------------------------------------------
def sum_halves(l):
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]
    middle = len(l) // 2
    return sum_halves(l[:middle]) + sum_halves(l[middle:])


def binary_search(sorted_list, target, low=0, high=None):
    """Index of target in a SORTED list, or -1. time O(log n)."""
    if high is None:
        high = len(sorted_list) - 1
    if low > high:
        return -1
    middle = (low + high) // 2
    if sorted_list[middle] == target:
        return middle
    if sorted_list[middle] < target:
        return binary_search(sorted_list, target, middle + 1, high)
    return binary_search(sorted_list, target, low, middle - 1)


def merge_sort(l):
    """time O(n log n). Returns a NEW list."""
    if len(l) <= 1:
        return l[:]
    middle = len(l) // 2
    left = merge_sort(l[:middle])
    right = merge_sort(l[middle:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:            # <= (not <) keeps the sort STABLE
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]  # one of the two is empty, the other holds the leftovers


def quick_sort(l):
    """time O(n log n) on average, O(n^2) worst case (already sorted + first element as pivot)."""
    if len(l) <= 1:
        return l[:]
    pivot = l[0]
    smaller = [x for x in l[1:] if x < pivot]
    bigger_or_equal = [x for x in l[1:] if x >= pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(bigger_or_equal)


# ---------------------------------------------------------------------------------------------
# D. NESTED LISTS (any depth)  -> isinstance(x, list)
# ---------------------------------------------------------------------------------------------
def flatten(nested):
    """flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]"""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))      # extend, NOT append
        else:
            result.append(item)
    return result


def nested_depth(nested):
    """nested_depth([]) = 1,  nested_depth([1, [2]]) = 2"""
    deepest = 0
    for item in nested:
        if isinstance(item, list):
            deepest = max(deepest, nested_depth(item))
    return 1 + deepest


def nested_sum(nested):
    total = 0
    for item in nested:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total


# ---------------------------------------------------------------------------------------------
# E. "ALL THE ..." GENERATORS : choose the first element, then recurse on the rest
# ---------------------------------------------------------------------------------------------
def binary_strings(n):
    """All strings of n characters '0'/'1', increasing order. time O(n * 2^n) (2^n strings of length n)."""
    if n == 0:
        return [""]
    shorter = binary_strings(n - 1)
    return ["0" + s for s in shorter] + ["1" + s for s in shorter]


def subsets(l):
    """All subsets of a list. subsets([1,2]) -> [[], [2], [1], [1, 2]]  (2^n subsets)."""
    if not l:
        return [[]]
    without_first = subsets(l[1:])
    with_first = [[l[0]] + s for s in without_first]
    return without_first + with_first


def permutations(l):
    """All orderings of a list (n! of them)."""
    if len(l) <= 1:
        return [l[:]]
    result = []
    for i in range(len(l)):
        rest = l[:i] + l[i + 1:]             # the list without element i
        for p in permutations(rest):
            result.append([l[i]] + p)
    return result


def combinations(l, k):
    """All the ways to choose k elements (order does not matter)."""
    if k == 0:
        return [[]]
    if len(l) < k:
        return []
    with_first = [[l[0]] + c for c in combinations(l[1:], k - 1)]
    without_first = combinations(l[1:], k)
    return with_first + without_first


def hanoi(n, source="A", target="C", spare="B"):
    """List of moves (from, to) to move n disks. 2^n - 1 moves."""
    if n == 0:
        return []
    return (hanoi(n - 1, source, spare, target)
            + [(source, target)]
            + hanoi(n - 1, spare, target, source))


def paths_in_grid(rows, cols):
    """The paths themselves, as strings of 'R'/'D' (grid_paths only counted them)."""
    if rows == 1 and cols == 1:
        return [""]
    result = []
    if cols > 1:
        result += ["R" + p for p in paths_in_grid(rows, cols - 1)]
    if rows > 1:
        result += ["D" + p for p in paths_in_grid(rows - 1, cols)]
    return result


# ---------------------------------------------------------------------------------------------
# F. FILES AND DICTS (recursion on a nested dict = same idea as nested lists)
# ---------------------------------------------------------------------------------------------
def count_leaves_dict(d):
    """Count the values that are not dicts: {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}} -> 3"""
    total = 0
    for value in d.values():
        if isinstance(value, dict):
            total += count_leaves_dict(value)
        else:
            total += 1
    return total


def dict_depth(d):
    deepest = 0
    for value in d.values():
        if isinstance(value, dict):
            deepest = max(deepest, dict_depth(value))
    return 1 + deepest


# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    assert list_sum([1, 2, 3, 4]) == list_sum_index([1, 2, 3, 4]) == 10
    assert list_max([3, 9, 2]) == 9
    assert list_count([1, 2, 1, 1], 1) == 3
    assert list_reverse([1, 2, 3]) == [3, 2, 1]
    assert list_contains([1, 2, 3], 3) and not list_contains([], 3)

    assert string_reverse("abc") == "cba"
    assert is_palindrome("kayak") and not is_palindrome("kayaks")
    assert count_char("banana", "a") == 3
    assert remove_char("banana", "a") == "bnn"
    assert balanced_parentheses("(()())") and not balanced_parentheses("(()") and not balanced_parentheses(")(")

    assert sum_halves([1, 2, 3, 4, 5]) == 15
    assert binary_search([1, 3, 5, 7, 9], 7) == 3 and binary_search([1, 3, 5], 4) == -1
    assert merge_sort([5, 2, 9, 1, 5, 6]) == quick_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]

    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert nested_depth([1, [2, [3]]]) == 3
    assert nested_sum([1, [2, [3, 4]], 5]) == 15

    assert binary_strings(2) == ["00", "01", "10", "11"] and binary_strings(0) == [""]
    assert len(subsets([1, 2, 3])) == 8
    assert sorted(permutations([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert combinations([1, 2, 3], 2) == [[1, 2], [1, 3], [2, 3]]
    assert len(hanoi(3)) == 7
    assert sorted(paths_in_grid(2, 3)) == ["DRR", "RDR", "RRD"]

    assert count_leaves_dict({"a": 1, "b": {"c": 2, "d": {"e": 3}}}) == 3
    assert dict_depth({"a": 1, "b": {"c": {}}}) == 3

    print("recursion_on_structures: all OK")
