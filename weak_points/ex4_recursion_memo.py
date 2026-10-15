"""
EX 4 : RECURSION, MEMOIZATION, ITERATION, TREES
  (your mistakes: `cache=None` then `n in cache` -> TypeError, cache never filled, memo calling the NON-memo function,
   `*` written `+` and `range(n)` instead of `range(k)` in the iterative version, `collect_infix` appending lists,
   functions left unwritten for lack of time: binary_strings, flatten, is_bst)

THE TEMPLATE for the memo version:
    def f(n, cache=None):
        if cache is None:
            cache = {}
        if <base case>:
            return ...
        if n in cache:
            return cache[n]
        result = ... f(smaller, cache) ...        # pass cache in EVERY recursive call
        cache[n] = result
        return result
"""


def motzkin(n):
    """Recursive, no cache."""
    raise NotImplementedError


def motzkin_memo(n, cache=None):
    """Recursive WITH a dictionary; must work when called several times in a row."""
    raise NotImplementedError


def motzkin_iter(n):
    """No recursion: build a list `values` with values[k] = M_k for k = 0..n."""
    raise NotImplementedError


def delannoy_memo(m, n, cache=None):
    """Recursive with a dict whose KEY is the tuple (m, n). Three recursive calls."""
    raise NotImplementedError


def binary_strings(n):
    """All the strings of n characters "0"/"1" in increasing order. binary_strings(2) -> ["00", "01", "10", "11"],
    binary_strings(0) -> [""]. Recursive."""
    raise NotImplementedError


def flatten(nested):
    """flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]. Recursive, uses isinstance(x, list)."""
    raise NotImplementedError


def digits_sum_rec(n):
    """Sum of the digits of n >= 0, recursive, no str(). digits_sum_rec(4711) -> 13"""
    raise NotImplementedError


def count_down(n):
    """List [n, n-1, ..., 1, 0] built recursively (n >= 0). count_down(3) -> [3, 2, 1, 0]"""
    raise NotImplementedError


def palindromic(s):
    """True if the string s reads the same backwards. RECURSIVE: compare the two ends, recurse on the middle."""
    raise NotImplementedError


class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def collect_infix(node):
    """Values in infix order (left, node, right) as a flat list. Empty tree -> []."""
    raise NotImplementedError


def collect_prefix(node):
    """Values in prefix order (node, left, right)."""
    raise NotImplementedError


def leaf_values(node):
    """Values of the leaves, left to right."""
    raise NotImplementedError


def count_even(node):
    """Number of nodes whose value is even."""
    raise NotImplementedError


def is_bst(node, low=None, high=None):
    """True if the tree is a binary search tree: at ALL depths, left values < node < right values.
    Hint: pass the allowed interval (low, high) down; None means 'no limit'."""
    raise NotImplementedError


def depth_of_max(node):
    """Depth (root = 0) of the node holding the largest value of a NON-EMPTY tree (values are distinct)."""
    raise NotImplementedError
