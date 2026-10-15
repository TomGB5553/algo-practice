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


# ---- A. Motzkin numbers :  M0 = 1,  M1 = 1,  Mn = M(n-1) + sum for i in 0..n-2 of  M(i) * M(n-2-i)
#         1, 1, 2, 4, 9, 21, 51, 127, ...       (same shape as Catalan: a sum of products)

def motzkin(n):
    """Recursive, no cache."""
    if n < 2:
        return 1
    total = motzkin(n - 1)
    for i in range(n - 1):
        total += motzkin(i) * motzkin(n - 2 - i)
    return total


def motzkin_memo(n, cache=None):
    """Recursive WITH a dictionary; must work when called several times in a row."""
    if cache is None:
        cache = {}
    if n < 2:
        return 1
    if n in cache:
        return cache[n]
    total = motzkin_memo(n - 1, cache)
    for i in range(n - 1):
        total += motzkin_memo(i, cache) * motzkin_memo(n - 2 - i, cache)
    cache[n] = total
    return total


def motzkin_iter(n):
    """No recursion: build a list `values` with values[k] = M_k for k = 0..n."""
    values = [1, 1]
    for k in range(2, n + 1):
        total = values[k - 1]
        for i in range(k - 1):
            total += values[i] * values[k - 2 - i]
        values.append(total)
    return values[n]


# ---- B. Two arguments : Delannoy numbers D(0, n) = D(m, 0) = 1,  D(m, n) = D(m-1, n) + D(m, n-1) + D(m-1, n-1)

def delannoy_memo(m, n, cache=None):
    """Recursive with a dict whose KEY is the tuple (m, n). Three recursive calls."""
    if cache is None:
        cache = {}
    if m == 0 or n == 0:
        return 1
    key = (m, n)
    if key in cache:
        return cache[key]
    result = (delannoy_memo(m - 1, n, cache)
              + delannoy_memo(m, n - 1, cache)
              + delannoy_memo(m - 1, n - 1, cache))
    cache[key] = result
    return result


# ---- C. Recursion that BUILDS a list / handles nested lists

def binary_strings(n):
    """All the strings of n characters "0"/"1" in increasing order. binary_strings(2) -> ["00", "01", "10", "11"],
    binary_strings(0) -> [""]. Recursive."""
    if n == 0:
        return [""]
    shorter = binary_strings(n - 1)
    return ["0" + s for s in shorter] + ["1" + s for s in shorter]


def flatten(nested):
    """flatten([1, [2, [3, 4]], 5]) -> [1, 2, 3, 4, 5]. Recursive, uses isinstance(x, list)."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def digits_sum_rec(n):
    """Sum of the digits of n >= 0, recursive, no str(). digits_sum_rec(4711) -> 13"""
    if n < 10:
        return n
    return n % 10 + digits_sum_rec(n // 10)


def count_down(n):
    """List [n, n-1, ..., 1, 0] built recursively (n >= 0). count_down(3) -> [3, 2, 1, 0]"""
    if n == 0:
        return [0]
    return [n] + count_down(n - 1)


def palindromic(s):
    """True if the string s reads the same backwards. RECURSIVE: compare the two ends, recurse on the middle."""
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and palindromic(s[1:-1])


# ---- D. Trees (Node is given)

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def collect_infix(node):
    """Values in infix order (left, node, right) as a flat list. Empty tree -> []."""
    if node is None:
        return []
    return collect_infix(node.left) + [node.value] + collect_infix(node.right)


def collect_prefix(node):
    """Values in prefix order (node, left, right)."""
    if node is None:
        return []
    return [node.value] + collect_prefix(node.left) + collect_prefix(node.right)


def leaf_values(node):
    """Values of the leaves, left to right."""
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.value]
    return leaf_values(node.left) + leaf_values(node.right)


def count_even(node):
    """Number of nodes whose value is even."""
    if node is None:
        return 0
    own = 1 if node.value % 2 == 0 else 0
    return own + count_even(node.left) + count_even(node.right)


def is_bst(node, low=None, high=None):
    """True if the tree is a binary search tree: at ALL depths, left values < node < right values.
    Hint: pass the allowed interval (low, high) down; None means 'no limit'."""
    if node is None:
        return True
    if low is not None and node.value <= low:
        return False
    if high is not None and node.value >= high:
        return False
    return is_bst(node.left, low, node.value) and is_bst(node.right, node.value, high)


def depth_of_max(node):
    """Depth (root = 0) of the node holding the largest value of a NON-EMPTY tree (values are distinct)."""
    best_value = [None, 0]

    def walk(n, depth):
        if n is None:
            return
        if best_value[0] is None or n.value > best_value[0]:
            best_value[0], best_value[1] = n.value, depth
        walk(n.left, depth + 1)
        walk(n.right, depth + 1)

    walk(node, 0)
    return best_value[1]
