# Python syntax cheat sheet (for the A4 sheet)

## Lists
```python
l = [3, 1, 2]            l[0] -> 3     l[-1] -> 2 (last)      len(l) -> 3
l.append(4)              # add one element at the end (in place, returns None)
l.extend([5, 6])         # add several elements
l.insert(0, 9)           # insert 9 at index 0
l.pop() / l.pop(i)       # remove and return the last / the element at index i
l.remove(x)              # remove the first x (in place)
l[1:3]  l[:2]  l[2:]  l[::-1]   # slices: start included, end EXCLUDED; [::-1] = reversed copy
sorted(l)                # new sorted list     l.sort()  # sorts in place, returns None
sorted(l, key=lambda x: x[1], reverse=True)   # by the 2nd element, biggest first
sum(l) max(l) min(l)     # on a list of numbers
x in l                   # True/False (O(n) for a list)
copy = list(l)           # a COPY (copy = l is only a second name for the SAME list)
[x * 2 for x in l if x > 0]     # list comprehension : transform + filter
```

## Dictionaries
```python
d = {"a": 1, "b": 2}     d["a"] -> 1            d["c"] = 3   # add / replace
"a" in d                 # tests the KEYS
d.get("z", 0)            # value or 0 if missing (no error)
for k in d:  for v in d.values():  for k, v in d.items():
len(d)  d.keys()  del d["a"]
{k: v for k, v in d.items() if v > 1}     # dict comprehension
```

## Strings
```python
s.lower() s.upper() s.split() s.split(",") s.replace("a", "b") s.strip()
",".join(["a", "b"]) -> "a,b"       f"{x} and {y:.2f}"  # f-string, :.2f = 2 decimals
s[0] s[-1] s[1:3]  len(s)  s[::-1]  "ab" in "cabd" -> True
int("12") float("1.5") str(12)
```

## Loops and conditions
```python
for i in range(5):            # 0..4         range(a, b): a..b-1       range(n, -1, -1): n..0
for i, x in enumerate(l):     # index AND element
for a, b in zip(l1, l2):      # two lists side by side
while cond:   ...   break   continue
if a and b / a or b / not a      # NOT:  `if x == "a" or "b"`  (always True!)  -> `if x in ("a", "b")`
x is None    x is not None       # for None, use `is`
a if cond else b                 # one-line choice
a, b = b, a                      # swap
```

## Functions
```python
def f(a, b=10):           # b has a default value (never use [] or {} as a default: use None)
    """What it does."""
    return a + b          # without return -> None
f(1)  f(1, 2)  f(1, b=3)  f(b=3, a=1)
lambda x: x * 2           # small anonymous function
```

## Files
```python
with open(path, encoding="utf-8") as file:     # closes the file automatically
    text = file.read()                         # whole file as one string
import json
data = json.load(file)                          # JSON file -> dict/list (keys are STRINGS)
import csv
rows = list(csv.DictReader(file))               # CSV -> list of dicts (values are STRINGS)
# for csv, open with newline="" : open(path, newline="", encoding="utf-8")
```

## Classes
```python
class Rational:
    def __init__(self, num, den):         # constructor
        self.num = num                    # attributes are created with self.
        self.den = den
    def __add__(self, other):             # r1 + r2   -> return a NEW object
        return Rational(self.num * other.den + other.num * self.den, self.den * other.den)
    def __lt__(self, other):              # r1 < r2   -> return True/False
        return self.num * other.den < other.num * self.den
    def __repr__(self):                   # print(r)  -> RETURN a string
        return f"Rational({self.num}/{self.den})"
    def method(self, x):                  # called r.method(3): self is r
        return self.num * x
class Child(Parent):                      # inheritance
    def __init__(self, v):
        super().__init__(v)               # call the parent constructor
```

## Recursion and memoization
```python
def f(n, cache=None):
    if cache is None:
        cache = {}
    if n < 2:                    # base case
        return n
    if n in cache:               # already computed
        return cache[n]
    cache[n] = f(n - 1, cache) + f(n - 2, cache)   # pass the SAME cache down
    return cache[n]
# two arguments : key = (a, b)   (a tuple can be a dict key, a list cannot)
```

## Complexity quick table
| Code shape                                  | Complexity |
|---------------------------------------------|------------|
| one `for` over n elements                   | O(n) |
| `for` inside `for`, both over n             | O(n^2) |
| `while i < n: i *= 2` or halving the input  | O(log n) |
| loop of n with a `sorted` inside            | O(n * n log n) |
| `sorted(l)`                                 | O(n log n) |
| `x in list` / `x in dict`                   | O(n) / O(1) |
| recursion calling itself twice (no memo)    | O(2^n) |
| the same with a cache                       | O(number of distinct subproblems) |
| binary search / BST find (balanced)         | O(log n) ; BST worst case O(n) |
| bubble / selection / insertion sort         | O(n^2) |
| merge sort ; quick sort (average)           | O(n log n) ; quick sort worst O(n^2) |
| tree traversal (dfs, bfs)                   | O(n) |

## Traversals of a tree
prefix: node, left, right | infix: left, node, right (ascending on a BST) | postfix: left, right, node | bfs: level by level (queue)
