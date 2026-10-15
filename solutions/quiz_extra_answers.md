# Answer key of the extra quiz

1. **D** - [1, 2, 3]  
   _`a[:]` makes a COPY, so appending to `b` does not change `a`. (With `b = a` both names would point to the same list.)_
2. **A** - [1, 2]  
   _The default list `[]` is created ONCE when the function is defined and shared by all the calls. Fix: `l=None`, then `if l is None: l = []`._
3. **C** - None  
   _`sort()` sorts in place and returns `None`. `sorted(l)` would return the new list. Never write `return l.sort()`._
4. **B** - True  
   _Strings are compared character by character: "1" < "9". Convert with `int()` before comparing numbers._
5. **B** - 1  
   _The `else` of a loop runs only if the loop ended WITHOUT `break`. Here `break` happens at i == 1, so only `print(i)` runs: 1._
6. **D** - TypeError  
   _Tuples (and strings) are immutable: item assignment raises `TypeError`._
7. **A** - 3 -4  
   _`//` is the FLOOR division: it rounds toward minus infinity, so -7 // 2 = -4._
8. **D** - [[1, 0], [1, 0]]  
   _`[[0]*2]*2` repeats the SAME inner list twice. Write `[[0]*2 for _ in range(2)]` to get independent rows._
9. **C** - 3  
   _Curly braces without `:` make a SET: duplicates disappear. `{1, 2, 3}` has 3 elements._
10. **A** - 2 1 1 2  
   _The first `print(n)` runs BEFORE the recursive call (going down: 2, 1), the second one AFTER it returns (coming back: 1, 2)._
11. **A** - 10  
   _f(4) = 4 + 3 + 2 + 1 + 0 = 10._
12. **C** - The dictionary is created once and shared between ALL the calls  
   _A default value is evaluated once, at the definition. Use `cache=None` and `if cache is None: cache = {}` inside the function._
13. **C** - O(2^n)  
   _Each call makes two calls and the same values are recomputed again and again: exponential._
14. **D** - O(n)  
   _Each value F(0)..F(n) is computed once, with a single addition each: O(n)._
15. **A** - O(n^2)  
   _The inner loop runs 0 + 1 + ... + (n-1) = n(n-1)/2 times: O(n^2)._
16. **D** - O(log n)  
   _n is divided by 2 at each turn: about log2(n) turns._
17. **C** - About n(n+1)/2, so O(n^2)  
   _C_k needs k products, so 1 + 2 + ... + n = n(n+1)/2: O(n^2)._
18. **D** - Insertion sort  
   _Insertion sort only compares each item with its left neighbour when the list is sorted. Selection sort always does n^2/2 comparisons, merge sort n log n._
19. **B** - items with equal keys keep their original relative order  
   _With a stable sort, sorting by Grade after sorting by Name keeps the names alphabetical inside each grade. For the insertion sort, use a STRICT `>` when shifting._
20. **D** - return self.norm_squared() < other.norm_squared()  
   _A method is called on an object: `object.method()`. `self` is passed automatically, so `norm_squared()` takes NO argument. `self < other` inside `__lt__` would call itself forever._
21. **B** - return a string  
   _`__repr__` RETURNS a string (the exact format of the statement). `print` is done by the caller._
22. **C** - v1.__add__(v2)  
   _Python calls the method `__add__` of the LEFT operand with the right one as argument. It must return a NEW object and not modify v1 or v2._
23. **B** - self.coeffs = list(coeffs)  
   _`self.coeffs = coeffs` only gives a second name to the same list: a later change by the caller would change the object. `list(coeffs)` or `coeffs[:]` copies._
24. **C** - data["101"]["SEEING"]["av"]  
   _JSON keys are ALWAYS strings: `"101"`, not `101`. A dict is read with `[...]`, not with a dot._
25. **A** - a key (a string here)  
   _Looping over a dict gives the KEYS. Use `data[night]` for the value, or `for night, info in data.items():` for both._
26. **B** - str  
   _Everything read from a CSV file is a string: convert with `int(...)` / `float(...)`._
27. **C** - return sorted(names)  
   _`sorted(names)` returns the new list. `names.sort()` returns None._
28. **D** - 1 3 2 8 5  
   _Postfix = left subtree, right subtree, then the node: (1 3 2) (8) 5. Prefix would be 5 2 1 3 8, infix 1 2 3 5 8, BFS 5 2 8 1 3._
29. **A** - 3  
   _root -> child -> leaf: 3 nodes. In the recursion: height(None) = 0, height(node) = 1 + max(height(left), height(right))._
30. **B** - if node is None:  
   _`is None` is the right test (`=` is an assignment: SyntaxError; `node.value` would crash on None)._
31. **C** - [1, 2, 3, 4]  
   _`m` rebinds its local `l` to a NEW list (`l + [4]`), so the caller's list is unchanged after `m(s)`. `m2` calls `append`, which modifies the caller's list._
32. **A** - TypeError: 'int' object is not callable  
   _Your variable `sum` hides the built-in function. Do not name variables `sum`, `list`, `min`, `max`, `dict`, `str`, `len`..._
33. **D** - ['fig', 'pear', 'kiwi']  
   _Sorted by length; "pear" and "kiwi" both have 4 letters and `sorted` is stable, so they keep their original order (pear first)._
34. **B** - 2 3  
   _The right-hand side `(b, a + b) = (2, 3)` is computed first with the OLD values, then assigned._
35. **B** - 2 4  
   _Python rounds .5 to the nearest EVEN number: round(2.5) = 2, round(3.5) = 4._
36. **A** - abs(a - b) < 1e-9  
   _Floats carry rounding errors: 0.1 + 0.2 == 0.3 is False. Compare with a small tolerance._

Count of correct letters: A=9, B=9, C=9, D=9
