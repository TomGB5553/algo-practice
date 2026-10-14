# Mock exam A (same format as exam 2025)

**Time: 1 hour.** Rules: act as in the real exam. Use ONLY your projects, your notebooks and one A4 sheet.
No internet, no AI. Do not open `../solutions/` before you have finished (or the hour is over).

Run the tests from THIS folder (`exam_A`):

```bash
python -m pytest tests/test_vector.py        # exercise 1
python -m pytest tests/test_catalan.py       # exercise 2
python -m pytest tests/test_observatory.py   # exercise 3
python -m pytest                             # everything
```

> **Warning** (as in the real exam): passing the tests is not enough. Follow the
> instructions precisely (names, return types) and make the logic correct.

Suggested timing: quiz (`../quiz/quiz_practice.md`, 10 min) - ex. 1 (12 min) - ex. 2 (18 min) - ex. 3 (20 min).
If you are stuck for more than 5 minutes, skip the question and come back.

---

## 1. 2D vectors

A vector of the plane is a pair `(x, y)` of numbers.

### Q1. Create the `Vector2D` class
In `src/vector.py`, create a class `Vector2D` with two attributes `x` and `y`.
The constructor takes two parameters, in this order: `x` and `y`.

### Q2. Addition
Implement `__add__` so that `v1 + v2` works. It **must** return a NEW `Vector2D` (the two
operands must not be modified):
`(x1, y1) + (x2, y2) = (x1 + x2, y1 + y2)`.

### Q3. String representation
Implement `__repr__`. It returns the string `Vector2D(x, y)`, with ONE space after the comma.
Example: `Vector2D(3, -1)`.

### Q4. Squared norm and comparison
- Implement the method `norm_squared(self)` that returns `x*x + y*y`.
- Implement `__lt__` so that `v1 < v2` is `True` when `v1` is SHORTER than `v2`
  (compare the squared norms). It must return a boolean.

### Q5. Scalar multiplication
Implement `__mul__` so that `v * k`, with `k` a number, returns a NEW vector `(k*x, k*y)`.

### Q6. Test in `main_vector.py`
In `main_vector.py`:
- create `Vector2D(3, 4)` and `Vector2D(-1, 2)`;
- print their sum;
- print the LONGER of the two (use `<`);
- print the first vector multiplied by 3.

---

## 2. Catalan numbers

The Catalan numbers `C_0, C_1, C_2, ...` count many things (ways to place brackets, binary trees...).
They are defined by:

```
C_0 = 1
C_n = C_0*C_(n-1) + C_1*C_(n-2) + ... + C_(n-1)*C_0     for n >= 1
    = sum, for i from 0 to n-1, of  C_i * C_(n-1-i)
```

First values: 1, 1, 2, 5, 14, 42, 132, 429...
Check by hand: `C_3 = C_0*C_2 + C_1*C_1 + C_2*C_0 = 2 + 1 + 2 = 5`.

### Q1. Recursive version
In `src/catalan.py`, write `catalan(n: int) -> int` that follows the formula with recursion.

### Q2. Memoization
Write `catalan_memo(n: int, cache=None) -> int`. It must be recursive and use a dictionary so that
each `C_k` is computed only once. `n` is the only mandatory parameter.
It must work if it is called several times in a row (be careful with the default value of `cache`).

### Q3. Iterative version
Write `catalan_iter(n: int) -> int` WITHOUT recursion: build a list `values` where `values[k]` is `C_k`,
from `k = 0` up to `n`.

### Q4. Complexity (write it in a comment above each function)
Give the time complexity of `catalan_memo` and of `catalan_iter` as a function of `n`
(count the multiplications). Explain in one sentence why `catalan` is much slower.

### Q5. Test in `main_catalan.py`
Compute `C_30` with `catalan_memo` and print it as `C_30 = VALUE`.

---

## 3. JSON data manipulation: an observatory

An amateur observatory records one JSON entry per night. The file `data/observatory.json`
becomes a nested dictionary once loaded. The keys are the **night numbers, as strings**
(`"101"`, `"102"`...). Some nights are missing from the file.

```json
"101": {
    "SEEING": {"av": 2.958, "ct": 530, "mn": 2.046, "mx": 4.108},
    "CLOUD":  {"av": 29.454, "ct": 886, "mn": 28.249, "mx": 30.227},
    "TARGETS": {
        "M57": {"type": "nebula", "minutes": 105},
        "M42": {"type": "nebula", "minutes": 110},
        "longest": {"name": "M42", "minutes": 110}
    },
    "Moon_phase": "new",
    "Observer": "Ada"
}
```

- `SEEING` is the quality of the air (lower = better). `av` = average, `ct` = count,
  `mn` = minimum, `mx` = maximum.
- `TARGETS` maps the name of each observed target to its `type` and the observation time in `minutes`.
  The key `"longest"` is NOT a target: it is a summary, you must skip it.

All the functions take `data` (the loaded dictionary) as first parameter.
Write them in `src/observatory.py`. Try them in `main_observatory.py`.

1. `load_data(file_path)` : read the JSON file and return the dictionary.
   (If you cannot, `from src.observatory_data import OBSERVATORY_DATA` gives you the dictionary.)
2. `count_nights(data)` : return the number of nights (int).
3. `get_avg_seeing(data, nights)` : `nights` is a list of integers. Return the average of the
   `SEEING` `av` values over these nights (float). A night that is not in the data is ignored.
   If no night is valid, return `None`.
4. `get_extreme_seeing(data)` : return `((night_min, mn), (night_max, mx))`: the night (as an
   **integer**) with the lowest `SEEING` `mn`, with that value, and the night with the highest
   `SEEING` `mx`, with that value.
5. `count_by_moon_phase(data)` : return a dictionary `{phase: number of nights with that phase}`.
6. `get_top_targets(data, top_n=3)` : return a dictionary `{night (str): [(target name, minutes), ...]}`
   where each list holds the `top_n` targets with the most minutes, sorted by minutes in descending
   order. Skip the key `"longest"`.
7. `get_hours_by_type(data)` : return a dictionary `{type: total hours}` (total minutes of all the
   targets of that type, over ALL the nights, divided by 60). Skip the key `"longest"`.

---

## Upload your work (in the real exam)

```bash
git add .
git commit -m "..."
git push origin main
```
