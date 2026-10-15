"""
EX 1 : KEYS, VALUES AND INDICES   (your mistake: `for i in coeffs: coeffs[i]`, `for night in data: night["SEEING"]`,
                                   `target["type"]` when `target` was a key string)

Before every `[...]`, ask yourself : what TYPE do I hold in this variable? (int index? str key? dict? list?)
Allowed: everything except hard-coding the examples.
"""


def indices_of(l, value):
    """All the INDICES i such that l[i] == value, in increasing order.
    indices_of([5, 7, 5, 5], 5) -> [0, 2, 3]       indices_of([1, 2], 9) -> []
    """
    raise NotImplementedError


def dot_product(a, b):
    """Sum of a[i] * b[i] for two lists of the SAME length. dot_product([1, 2, 3], [4, 5, 6]) -> 32"""
    raise NotImplementedError


def last_nonzero_index(l):
    """Index of the LAST non-zero element, -1 if there is none (it is the degree of a polynomial).
    last_nonzero_index([1, 2, 0, 0]) -> 1       last_nonzero_index([0, 0]) -> -1     last_nonzero_index([]) -> -1
    Hint: do you need to start from the beginning or from the end?
    """
    raise NotImplementedError


def evaluate(coeffs, x):
    """Value of coeffs[0] + coeffs[1]*x + coeffs[2]*x**2 + ...   evaluate([3, 2, 5], 2) -> 27
    (The mock exam B version summed x**i and forgot the coefficient.)
    """
    raise NotImplementedError


def pairs_with_gap(l, gap):
    """All the pairs (l[i], l[j]) with i < j and l[j] - l[i] == gap, in order of i then j.
    pairs_with_gap([1, 3, 5, 3], 2) -> [(1, 3), (1, 3), (3, 5)]
    (i=0 pairs with j=1 and j=3, i=1 pairs with j=2, i=2 pairs with nobody)
    """
    raise NotImplementedError


def total_by_key(data):
    """data = {"a": {"v": 1, "w": 2}, "b": {"v": 10}}  ->  {"a": 3, "b": 10}
    The inner dict can have any keys; add up all of its VALUES.
    """
    raise NotImplementedError


def longest_name_id(data):
    """data = {"7": {"name": "Ada"}, "12": {"name": "Margaret"}}  ->  "12"   (the KEY, a string).
    None if data is empty. If two names have the same length, the first one in the dict wins.
    """
    raise NotImplementedError


def field_values(data, field):
    """The value of `field` for each entry, ordered by the key read as an INTEGER.
    data = {"10": {"t": 5}, "9": {"t": 7}, "11": {"t": 1}}, field = "t"  ->  [7, 5, 1]
    (strings would sort "10" < "11" < "9": convert to int to sort)
    """
    raise NotImplementedError


def count_real_targets(data):
    """data = {night: {"TARGETS": {"M42": {...}, "M31": {...}, "longest": {...}}, ...}, ...}
    Count the targets of ALL the nights, but the key "longest" is not a target.
    """
    raise NotImplementedError


def minutes_of_type(data, wanted_type):
    """Same structure with target = {"type": "nebula", "minutes": 105}.
    Total minutes of the targets of type `wanted_type` over all nights (skip "longest")."""
    raise NotImplementedError


def get_path(data, keys):
    """Follow a list of keys in a nested dict. get_path({"a": {"b": 5}}, ["a", "b"]) -> 5.
    If a key is missing anywhere, return None."""
    raise NotImplementedError
