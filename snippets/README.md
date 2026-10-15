# Snippets library : "where is an example of ...?"

Every file is a **runnable, tested** collection of functions with the reasoning in comments.
Check one with `python3 snippets/<file>.py` (prints `all OK`). In the exam you may use your own files:
copy the structure, ADAPT the names / keys / return type to the statement. Never paste blindly.

| I need ... | File | Look for |
|------------|------|----------|
| recursion, memoization AND iteration of the same problem (factorial, **Fibonacci**, **Catalan**, grid paths, binomial, Pascal, stairs, power by squaring, gcd, count change, Collatz, LCS) | `recursion_classics.py` | sections 1-12 |
| recursion on lists / strings / halves; merge sort, quick sort, binary search; **flatten**, nested sum; **binary strings**, subsets, permutations, combinations, Tower of Hanoi, nested dicts | `recursion_on_structures.py` | sections A-F |
| **nested JSON**: load, count, average with missing keys, min/max with the key, top N, group by, filter, flatten to rows, safe path access, `continue` on odd keys | `json_nested.py` | sections 1-10 |
| **CSV**: DictReader + conversions, count/group/average by category, best, filter+sort, sort by 2 criteria, **insertion / selection / bubble sort**, mean/median, write a CSV | `csv_data.py` | sections 1-8 |
| **trees**: Node, height, leaves, sum, contains, 4 traversals, BFS, levels, paths, **BST** (find, min, max, insert, delete, `is_bst`), tree classes with inheritance, expression tree | `trees.py` | sections 1-5 |
| **classes**: `__init__`, `__repr__`, `__add__`, `__mul__`, `__lt__`, `__eq__`, `__len__`, `__contains__`, Vector2D, Rational, Polynomial, Stack, Queue, Car, BankAccount, inheritance | `classes_special_methods.py` | sections 1-6 |
| quick facts: slicing, aliasing and copies, what each method returns, loops (`enumerate`, `zip`, `for...else`), comprehensions, dict/set/string/sort recipes, exceptions, text files, matrices, prime sieve, two-sum | `python_recipes.py` | sections 1-15 |
| **complexity**: how to count, table of sorts, timing with `timeit`, matplotlib minimum | `complexity_and_timing.py` | docstring on top |

## Recognise the exercise, find the snippet

| The statement says... | Open |
|-----------------------|------|
| "recursive", "memoization", "cache dictionary", "iterative version", "values[k]" | `recursion_classics.py` (any triple: `x`, `x_memo`, `x_iter`) |
| "all the strings / lists / subsets / orderings of ..." | `recursion_on_structures.py` section E |
| "list that may contain lists at any depth" | `recursion_on_structures.py` `flatten` |
| "the keys are strings", "nested dictionary", "some nights are missing" | `json_nested.py` |
| "skip the key `longest`" | `json_nested.py` `get_top_targets`, `get_hours_by_type` (`continue`) |
| "everything is read as a string", "csv", "DictReader" | `csv_data.py` |
| "write your own sort", "stable", "you cannot use `sorted`" | `csv_data.py` `insertion_sort` |
| "sorted by ... then by ...", "descending" | `csv_data.py` `sort_by_two_criteria`, `python_recipes.py` section 9 |
| "binary tree", "left", "right", "None is an empty tree" | `trees.py` |
| "binary search tree", "at ALL depths" | `trees.py` `is_bst` |
| "special method", "`v1 + v2` must return a NEW", "`<`" | `classes_special_methods.py` |
| "complexity", "count the multiplications" | `complexity_and_timing.py` docstring + comments above each function |
| "stores a COPY" | `classes_special_methods.py` `Polynomial.__init__` |

## Coding conventions used in all the files

* A comment starting with `# time O(...)` above a function gives its complexity, in the style the exam asks for.
* `result`, `total`, `count`, `best`... as variable names: never `sum`, `list`, `min`, `max`.
* Each file ends with `if __name__ == "__main__":` and `assert`s: the examples are the specification.
