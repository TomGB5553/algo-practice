"""
PYTHON RECIPES : lists, dicts, sets, strings, slicing, sorting, files, mutation traps, quiz facts.

Run:  python3 snippets/python_recipes.py

Each section = one thing the quiz or an exercise asks. The asserts show the exact result.
"""
import json
import os
import tempfile


# =============================================================================================
# 1. THE "WHAT DOES IT RETURN?" TABLE (the cause of most `None` bugs)
# =============================================================================================
def return_values_demo():
    l = [3, 1, 2]
    assert l.sort() is None                    # sort() MODIFIES the list and returns None
    assert l == [1, 2, 3]
    assert sorted([3, 1, 2]) == [1, 2, 3]      # sorted() returns a NEW list
    assert [1].append(2) is None               # append / extend / insert / remove / reverse -> None
    assert [1, 2, 3].pop() == 3                # pop RETURNS the removed element
    assert [1, 2, 3].index(2) == 1             # index: position of the first match (ValueError if absent)
    assert "abc".upper() == "ABC"              # strings are IMMUTABLE: methods return a new string
    s = "abc"
    s.upper()                                  # result thrown away: s is unchanged
    assert s == "abc"


# =============================================================================================
# 2. ALIASING AND COPIES (quiz question 1 of the training exam)
# =============================================================================================
def aliasing_demo():
    x = [1, 2, 3]
    y = x                                      # y is ANOTHER NAME for the same list
    y.append(4)
    assert x == [1, 2, 3, 4]                   # x changed too!

    z = x[:]                                   # copy (also list(x) or x.copy())
    z.append(5)
    assert x == [1, 2, 3, 4]                   # x not affected

    grid = [[0] * 3] * 2                       # TRAP: the 2 rows are the SAME list
    grid[0][0] = 9
    assert grid == [[9, 0, 0], [9, 0, 0]]
    grid = [[0] * 3 for _ in range(2)]         # RIGHT: a new row each time
    grid[0][0] = 9
    assert grid == [[9, 0, 0], [0, 0, 0]]


def modifies_argument(l):
    l.append(99)                               # modifies the caller's list


def does_not_modify(l):
    l = l + [99]                               # `+` builds a NEW list, rebinding the local name only
    return l


def default_argument_trap(item, bucket=[]):    # DON'T: the same list is shared between calls
    bucket.append(item)
    return bucket


def default_argument_ok(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


# =============================================================================================
# 3. SLICING  l[start:stop:step]   start included, stop EXCLUDED
# =============================================================================================
def slicing_demo():
    l = [10, 20, 30, 40, 50]
    assert l[1:3] == [20, 30]
    assert l[:2] == [10, 20] and l[2:] == [30, 40, 50]
    assert l[-2:] == [40, 50] and l[:-1] == [10, 20, 30, 40]
    assert l[::2] == [10, 30, 50] and l[::-1] == [50, 40, 30, 20, 10]
    assert l[10:] == [] and l[:100] == l       # out-of-range slices never crash (an INDEX does)
    assert "hello"[1:4] == "ell" and "hello"[::-1] == "olleh"
    top3 = sorted(l, reverse=True)[:3]
    assert top3 == [50, 40, 30]


# =============================================================================================
# 4. LOOPS : which one gives what
# =============================================================================================
def loops_demo():
    l = ["a", "b", "c"]
    assert [x for x in l] == ["a", "b", "c"]                       # the VALUES
    assert [i for i in range(len(l))] == [0, 1, 2]                 # the INDICES
    assert list(enumerate(l)) == [(0, "a"), (1, "b"), (2, "c")]    # both
    assert list(zip(l, [1, 2, 3])) == [("a", 1), ("b", 2), ("c", 3)]   # two lists side by side
    d = {"x": 1, "y": 2}
    assert list(d) == ["x", "y"]                                   # for k in d       -> KEYS
    assert list(d.values()) == [1, 2]                              # d.values()       -> VALUES
    assert list(d.items()) == [("x", 1), ("y", 2)]                 # d.items()        -> (key, value)
    assert list(range(5, 0, -1)) == [5, 4, 3, 2, 1]                # range(start, stop_excluded, step)

    # for ... else : the else runs when the loop finished WITHOUT break
    out = []
    for i in range(3):
        out.append(i)
    else:
        out.append("done")
    assert out == [0, 1, 2, "done"]
    out = []
    for i in range(3):
        if i == 1:
            break
        out.append(i)
    else:
        out.append("done")
    assert out == [0]

    # continue skips the rest of ONE iteration; break leaves the whole loop; return leaves the function
    kept = [x for x in range(6) if x % 2 == 0]
    assert kept == [0, 2, 4]


# =============================================================================================
# 5. COMPREHENSIONS (a loop inside brackets)
# =============================================================================================
def comprehensions_demo():
    assert [x * x for x in range(4)] == [0, 1, 4, 9]
    assert [x for x in range(10) if x % 3 == 0] == [0, 3, 6, 9]
    assert {w: len(w) for w in ["a", "bb"]} == {"a": 1, "bb": 2}              # dict comprehension
    assert {x % 3 for x in range(10)} == {0, 1, 2}                            # set comprehension
    assert [[0] * 2 for _ in range(2)] == [[0, 0], [0, 0]]
    assert [c for row in [[1, 2], [3]] for c in row] == [1, 2, 3]            # flatten one level
    assert sum(x for x in range(4)) == 6                                      # generator, no brackets


# =============================================================================================
# 6. DICTIONARIES : the 5 patterns
# =============================================================================================
def count_items(items):
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1       # .get(key, default): no KeyError
    return counts


def group_items(items, key):
    groups = {}
    for x in items:
        k = key(x)
        if k not in groups:
            groups[k] = []
        groups[k].append(x)
    return groups


def invert(d):
    return {v: k for k, v in d.items()}


def merge_counts(a, b):
    result = dict(a)                           # copy, do not modify a
    for k, v in b.items():
        result[k] = result.get(k, 0) + v
    return result


def key_with_max_value(d):
    best = None
    for k in d:
        if best is None or d[k] > d[best]:
            best = k
    return best                                # or  max(d, key=d.get)


def dict_demo():
    assert count_items("banana") == {"b": 1, "a": 3, "n": 2}
    assert group_items(["a", "bb", "cc"], len) == {1: ["a"], 2: ["bb", "cc"]}
    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert merge_counts({"a": 1}, {"a": 2, "b": 1}) == {"a": 3, "b": 1}
    assert key_with_max_value({"a": 1, "b": 7}) == "b"
    d = {"a": 1}
    assert d.get("zzz") is None and d.get("zzz", 0) == 0 and "zzz" not in d
    d.pop("a")
    assert d == {}
    assert {"a": 1} == {"a": 1} and {1, 2} == {2, 1}
    try:
        {"a": 1}["b"]
    except KeyError:
        pass                                   # reading a missing key with [] raises KeyError
    # Only IMMUTABLE objects can be keys: str, int, tuple yes; list, dict no
    cache = {(2, 3): 3}
    assert cache[(2, 3)] == 3


# =============================================================================================
# 7. SETS (unique elements, fast `in`)
# =============================================================================================
def sets_demo():
    assert sorted(set([3, 1, 3, 2])) == [1, 2, 3]                    # remove duplicates
    assert len(set("banana")) == 3
    a, b = {1, 2, 3}, {2, 3, 4}
    assert a & b == {2, 3} and a | b == {1, 2, 3, 4} and a - b == {1}
    assert 2 in a                                                    # O(1) on average (O(n) for a list)


def remove_duplicates_keep_order(items):
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# =============================================================================================
# 8. STRINGS
# =============================================================================================
def strings_demo():
    s = "Hello, World"
    assert s.lower() == "hello, world" and s.upper() == "HELLO, WORLD"
    assert s.split(", ") == ["Hello", "World"] and " a  b ".split() == ["a", "b"]
    assert "-".join(["a", "b", "c"]) == "a-b-c"
    assert s.replace("l", "L") == "HeLLo, WorLd"
    assert s.startswith("Hello") and s.endswith("d") and "World" in s
    assert s.find("World") == 7 and s.find("zzz") == -1 and s.count("l") == 3
    assert "  x ".strip() == "x"
    assert "abc".isalpha() and "123".isdigit() and not "a1".isalpha()
    assert "7".zfill(3) == "007" and f"{3.14159:.2f}" == "3.14" and f"{5:03d}" == "005"
    assert ord("a") == 97 and chr(98) == "b"               # letter <-> number
    assert "a" < "b" and "10" < "9"                         # strings compare character by character!
    assert not (int("10") < int("9"))        # converted to numbers: 10 < 9 is False
    assert "abc" * 2 == "abcabc" and len("abc") == 3 and "abc"[0] == "a"
    letters_only = "".join(c for c in "a1b2" if c.isalpha())
    assert letters_only == "ab"


def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def word_frequencies(text):
    freq = {}
    for word in text.lower().split():
        word = word.strip(".,;:!?")
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq


def letter_frequencies(text):
    """{letter: proportion}  (language-detection project)"""
    letters = [c.lower() for c in text if c.isalpha()]
    total = len(letters)
    counts = {}
    for c in letters:
        counts[c] = counts.get(c, 0) + 1
    return {c: n / total for c, n in counts.items()}


def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result


# =============================================================================================
# 9. SORTING WITH key= (a function applied to each element to get its sort value)
# =============================================================================================
def sorting_demo():
    words = ["pear", "fig", "banana", "kiwi"]
    assert sorted(words) == ["banana", "fig", "kiwi", "pear"]
    assert sorted(words, key=len) == ["fig", "pear", "kiwi", "banana"]        # stable: pear before kiwi
    assert sorted(words, key=len, reverse=True)[0] == "banana"
    pairs = [("a", 3), ("b", 1), ("c", 2)]
    assert sorted(pairs, key=lambda p: p[1]) == [("b", 1), ("c", 2), ("a", 3)]
    people = [{"n": "A", "age": 30}, {"n": "B", "age": 25}]
    assert [p["n"] for p in sorted(people, key=lambda p: p["age"])] == ["B", "A"]
    assert sorted([(2, "b"), (1, "z"), (2, "a")]) == [(1, "z"), (2, "a"), (2, "b")]   # tuples: lexicographic
    assert max(words, key=len) == "banana" and min(words, key=len) == "fig"
    assert sum([1, 2, 3]) == 6 and max([1, 9, 3]) == 9 and abs(-3) == 3 and round(2.567, 1) == 2.6


# =============================================================================================
# 10. NUMBERS
# =============================================================================================
def numbers_demo():
    assert 7 // 2 == 3 and 7 % 2 == 1 and -7 // 2 == -4 and 7 / 2 == 3.5
    assert 2 ** 10 == 1024 and 10 ** -1 == 0.1
    assert int(3.9) == 3 and round(3.5) == 4 and round(2.5) == 2           # round: banker's rounding!
    assert 0.1 + 0.2 != 0.3 and abs(0.1 + 0.2 - 0.3) < 1e-9                 # never == on floats
    assert float("inf") > 10 ** 100                                         # handy initial value for a min search
    assert divmod(17, 5) == (3, 2)
    assert bool(0) is False and bool("") is False and bool([]) is False and bool(None) is False
    assert 5 == 5.0 and type(5) is int and type(5 / 1) is float
    a, b = 1, 2
    a, b = b, a                                                             # swap without temp variable
    assert (a, b) == (2, 1)


# =============================================================================================
# 11. FUNCTIONS
# =============================================================================================
def functions_demo():
    def apply(f, x):                           # a function can be an argument (first-class object)
        return f(x)

    assert apply(len, "abc") == 3 and apply(lambda x: x + 1, 1) == 2
    assert (lambda a, b: a * b)(3, 4) == 12

    def min_max(l):
        return min(l), max(l)                  # "returns two values" = returns ONE tuple

    lo, hi = min_max([3, 1, 2])                # unpacking
    assert (lo, hi) == (1, 3)

    def f(a, b=10, *args, **kwargs):
        return a, b, args, kwargs

    assert f(1) == (1, 10, (), {}) and f(1, 2, 3, z=4) == (1, 2, (3,), {"z": 4})
    assert f(b=5, a=1)[:2] == (1, 5)           # keyword arguments

    def no_return():
        x = 1

    assert no_return() is None                 # no return statement -> None

    def counter():
        total = 0

        def add(n):
            nonlocal total                     # needed to REASSIGN a variable of the enclosing function
            total += n
            return total
        return add

    c = counter()
    c(1)
    assert c(2) == 3


# =============================================================================================
# 12. EXCEPTIONS
# =============================================================================================
def safe_int(text, default=None):
    try:
        return int(text)
    except ValueError:                         # catch the PRECISE error
        return default


def exceptions_demo():
    assert safe_int("12") == 12 and safe_int("x") is None and safe_int("x", 0) == 0
    for bad, error in [(lambda: [][0], IndexError), (lambda: {}["k"], KeyError),
                       (lambda: int("a"), ValueError), (lambda: 1 / 0, ZeroDivisionError),
                       (lambda: None + 1, TypeError), (lambda: undefined_name, NameError)]:
        try:
            bad()
        except error:
            pass
        else:
            raise AssertionError("expected " + error.__name__)


# =============================================================================================
# 13. TEXT FILES
# =============================================================================================
def file_demo():
    path = os.path.join(tempfile.mkdtemp(), "t.txt")
    with open(path, "w") as f:                 # "w" erases, "a" appends, "r" reads (default)
        f.write("one\ntwo\nthree\n")
    with open(path) as f:
        text = f.read()                        # whole file as ONE string
    with open(path) as f:
        lines = [line.strip() for line in f]   # list of lines without the "\n"
    assert text == "one\ntwo\nthree\n" and lines == ["one", "two", "three"]
    with open(path) as f:
        assert f.readlines() == ["one\n", "two\n", "three\n"]
    assert os.path.exists(path)


# =============================================================================================
# 14. MATRICES (list of lists)
# =============================================================================================
def transpose(m):
    return [[m[r][c] for r in range(len(m))] for c in range(len(m[0]))]


def matrix_mul(a, b):
    n, k, p = len(a), len(b), len(b[0])        # (n x k) * (k x p) -> (n x p)  time O(n*k*p)
    return [[sum(a[i][t] * b[t][j] for t in range(k)) for j in range(p)] for i in range(n)]


def diagonal(m):
    return [m[i][i] for i in range(len(m))]


def neighbours(grid, r, c):
    """Valid 4-neighbours of a cell: always test the bounds BEFORE indexing."""
    result = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            result.append((nr, nc))
    return result


# =============================================================================================
# 15. CLASSIC LIST ALGORITHMS
# =============================================================================================
def second_largest(numbers):
    largest = second = None
    for n in numbers:
        if largest is None or n > largest:
            largest, second = n, largest
        elif n != largest and (second is None or n > second):
            second = n
    return second


def running_sum(numbers):
    result, total = [], 0
    for n in numbers:
        total += n
        result.append(total)
    return result


def rotate_right(items, k):
    if not items:
        return []
    k %= len(items)
    return items[-k:] + items[:-k] if k else items[:]


def merge_sorted(a, b):
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result + a[i:] + b[j:]


def linear_search(l, target):
    for i, x in enumerate(l):
        if x == target:
            return i
    return -1                                  # AFTER the loop, never inside it


def two_sum(numbers, target):
    """Indices of two numbers adding to target. O(n) with a dict instead of O(n^2) with two loops."""
    seen = {}
    for i, x in enumerate(numbers):
        if target - x in seen:
            return seen[target - x], i
        seen[x] = i
    return None


def is_sorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:                          # only up to sqrt(n): O(sqrt n)
        if n % d == 0:
            return False
        d += 1
    return True


def sieve(n):
    """Primes <= n, O(n log log n)."""
    flags = [True] * (n + 1)
    flags[0:2] = [False, False]
    for p in range(2, int(n ** 0.5) + 1):
        if flags[p]:
            for multiple in range(p * p, n + 1, p):
                flags[multiple] = False
    return [i for i, f in enumerate(flags) if f]


def algorithms_demo():
    assert second_largest([3, 9, 5, 9]) == 5 and second_largest([1]) is None
    assert running_sum([1, 2, 3]) == [1, 3, 6]
    assert rotate_right([1, 2, 3, 4], 1) == [4, 1, 2, 3] and rotate_right([1, 2, 3], 3) == [1, 2, 3]
    assert merge_sorted([1, 4], [2, 3, 9]) == [1, 2, 3, 4, 9]
    assert linear_search([5, 6], 6) == 1 and linear_search([5, 6], 7) == -1
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert is_sorted([1, 2, 2]) and not is_sorted([2, 1])
    assert is_prime(97) and not is_prime(91) and sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert diagonal([[1, 2], [3, 4]]) == [1, 4]
    assert neighbours([[0] * 3 for _ in range(3)], 0, 0) == [(1, 0), (0, 1)]


# =============================================================================================
if __name__ == "__main__":
    return_values_demo()
    aliasing_demo()
    l = [1]
    modifies_argument(l)
    assert l == [1, 99]
    l2 = [1]
    assert does_not_modify(l2) == [1, 99] and l2 == [1]
    assert default_argument_trap(1) == [1] and default_argument_trap(2) == [1, 2]   # the bug
    assert default_argument_ok(1) == [1] and default_argument_ok(2) == [2]          # the fix
    slicing_demo()
    loops_demo()
    comprehensions_demo()
    dict_demo()
    sets_demo()
    assert remove_duplicates_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    strings_demo()
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert word_frequencies("The cat. The dog!") == {"the": 2, "cat": 1, "dog": 1}
    assert abs(sum(letter_frequencies("aab").values()) - 1) < 1e-12
    assert caesar("abc xyz", 3) == "def abc"
    sorting_demo()
    numbers_demo()
    functions_demo()
    exceptions_demo()
    file_demo()
    algorithms_demo()
    assert json.loads('{"a": [1, true, null]}') == {"a": [1, True, None]}
    print("python_recipes: all OK")
