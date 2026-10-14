# Mock exam B (harder on reasoning: lists of different lengths, 2-argument memoization, CSV, sorting, trees)

**Time: 1 hour 15** (a bit longer than the real one: there are 4 exercises).
Same rules as the real exam: your projects + notebooks + one A4 sheet. No internet, no AI.
Do not open `../solutions/` before you have finished.

Run the tests from THIS folder (`exam_B`):

```bash
python -m pytest tests/test_polynomial.py
python -m pytest tests/test_paths.py
python -m pytest tests/test_planets.py
python -m pytest tests/test_trees.py
python -m pytest
```

> **Warning**: passing the tests is not enough. Follow the instructions precisely and keep the logic correct.
> Function and class names are checked.

---

## 1. Polynomials

A polynomial `a0 + a1*x + a2*x^2 + ...` is stored as the list of its coefficients **from the lowest
degree to the highest**: `[a0, a1, a2, ...]`.
Example: `3 + 2x + 5x^2` is `[3, 2, 5]`.

### Q1. The constructor
In `src/polynomial.py`, create the class `Polynomial`. Its constructor takes `coeffs` (a list of numbers)
and stores a **COPY** of it in the attribute `coeffs` (so that changing the original list later does not
change the polynomial).

### Q2. String representation
`__repr__` returns `Polynomial([3, 2, 5])` (the word `Polynomial`, then the list, in parentheses).

### Q3. Degree
Method `degree(self)`: the degree of the polynomial, i.e. the index of its LAST NON-ZERO coefficient.
Trailing zeros are ignored: `[1, 2, 0, 0]` has degree 1. The zero polynomial (empty list or only zeros)
has degree `-1`.

### Q4. Evaluation
Method `evaluate(self, x)`: the value of the polynomial at `x`.
Example: `[3, 2, 5]` at `x = 2` gives `3 + 2*2 + 5*4 = 27`.

### Q5. Addition
`__add__`: `p + q` returns a NEW `Polynomial`, whose coefficient `i` is the sum of the coefficients `i`
of `p` and `q`. **The two lists may have different lengths**: a missing coefficient counts as 0.
Example: `[1, 2] + [10, 20, 30] = [11, 22, 30]`. Neither `p` nor `q` may be modified.

### Q6. Multiplication
`__mul__`: `p * q` returns a NEW `Polynomial`. Reminder: `(a_i x^i) * (b_j x^j) = a_i b_j x^(i+j)`,
and all the terms with the same power are added.
Example: `(1 + x) * (1 + x) = 1 + 2x + x^2`, i.e. `[1, 1] * [1, 1] = [1, 2, 1]`.
(The result list has `len(p) + len(q) - 1` coefficients. Empty lists: return `Polynomial([])`.)

### Q7. Test in `main_polynomial.py`
Create `p = [1, 2, 3]` and `q = [4, 5]` as polynomials. Print `p + q`, `p * q`, the degree of `p` and
`p` evaluated at 2.

---

## 2. Recursion on grids and strings

### Q1. Paths in a grid
A robot is at the top-left corner of a grid and can only move one step **right** or one step **down**.
Write in `src/paths.py` the recursive function `grid_paths(rows, cols)` that returns the number of
different paths from the top-left cell to the bottom-right cell of a grid of `rows` x `cols` cells.
- a grid with only one row, or only one column, has exactly 1 path;
- otherwise, the last move was either a step down (coming from the grid with one row less) or a step
  right (coming from the grid with one column less).
Check: `grid_paths(2, 2) = 2`, `grid_paths(3, 3) = 6`, `grid_paths(3, 7) = 28`.

### Q2. Memoization with two arguments
Write `grid_paths_memo(rows, cols, cache=None)`, recursive with a dictionary. The key of the dictionary
must hold BOTH arguments (hint: a tuple `(rows, cols)` can be a key).

### Q3. All the binary strings
Write the recursive function `binary_strings(n)` that returns the LIST of all the strings of `n`
characters `"0"` or `"1"`, in increasing order. `binary_strings(0)` is `[""]`,
`binary_strings(2)` is `["00", "01", "10", "11"]`.

### Q4. Flatten
Write the recursive function `flatten(nested)` that takes a list which may contain integers or other
lists (at any depth) and returns a flat list of the integers, in order.
`flatten([1, [2, [3, 4]], 5])` is `[1, 2, 3, 4, 5]`. Hint: `isinstance(x, list)` tests if `x` is a list.

### Q5. Complexities
In a comment above each function, give the time complexity of `grid_paths`, `grid_paths_memo` and
`binary_strings` (in terms of `rows`, `cols` or `n`; for `grid_paths` it is enough to say if it is
polynomial or exponential, and why).

---

## 3. CSV data: exoplanets

The file `data/exoplanets.csv` has the columns `Name`, `Year`, `Distance_ly`, `Mass_earth`, `Method`.
Remember: **everything is read as a string** from a CSV file.
Write your functions in `src/planets.py`.

1. `load_planets(path)`: return a list of dictionaries, one per row, where `Year` is an `int`,
   `Distance_ly` and `Mass_earth` are `float`s, and `Name` and `Method` stay strings.
2. `count_by_method(planets)`: return `{method: number of planets}`.
3. `heaviest_planet(planets)`: return the NAME (a string, not a dictionary) of the planet with the
   biggest `Mass_earth`, or `None` if the list is empty.
4. `average_distance_by_method(planets)`: return `{method: average Distance_ly of its planets}`.
5. `planets_between(planets, first_year, last_year)`: return the sorted list (alphabetical order) of the
   NAMES of the planets discovered between the two years, both included.
6. `insertion_sort(planets, key)`: **write your own sort** (you cannot use `sorted` or `.sort` here).
   It returns a NEW list sorted in ascending order of `key(planet)` and does not modify the input list.
   When two planets have the same key, they must stay in their original order (stable sort).
   Hint, insertion sort: build the result by taking the items one by one and inserting each one at the
   right place in the already sorted result. Give its worst-case time complexity in a comment.

---

## 4. Trees

`src/trees.py` already contains the class `Node` (a binary tree node: `value`, `left`, `right`;
a missing child is `None`; an empty tree is `None` itself). Write the recursive functions:

1. `height(node)`: number of nodes on the longest path from `node` down to a leaf. `height(None) = 0`,
   and a single node has height 1.
2. `count_leaves(node)`: number of leaves (nodes with NO child). `count_leaves(None) = 0`.
3. `tree_sum(node)`: sum of all the values.
4. `contains(node, value)`: `True` if `value` is somewhere in the tree (the tree is NOT necessarily a
   binary search tree, so you may have to look in both children).
5. `collect_infix(node)`: the list of the values in infix order (left, node, right).
6. **Challenge** `is_bst(node)`: `True` if the tree is a binary search tree (every value of the left
   subtree is smaller than the node, every value of the right subtree is bigger, at ALL depths, not only
   for the direct children). Hint: pass down the interval `(low, high)` in which the values must be.

In a comment above each function, give its time complexity.
