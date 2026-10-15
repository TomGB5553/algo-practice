# Mock exam C (same format as exam 2025, built on YOUR weak points)

**Time: 1 hour.** Rules: act as in the real exam. Use ONLY your projects, your notebooks, `snippets/` and one A4 sheet.
No internet, no AI. Do not open `../solutions/` before you have finished (or the hour is over).

Run the tests from THIS folder (`exam_C`):

```bash
python -m pytest tests/test_duration.py      # exercise 1
python -m pytest tests/test_stairs.py        # exercise 2
python -m pytest tests/test_greenhouse.py    # exercise 3
python -m pytest                             # everything
```

> **Warning** (as in the real exam): passing the tests is not enough. Follow the
> instructions precisely (names, return types) and make the logic correct. Write the complexity comments.

Suggested timing: quiz (`quiz.md`, 10 min) - ex. 1 (12 min) - ex. 2 (18 min) - ex. 3 (20 min).
If you are stuck for more than 5 minutes, skip the question and come back. Write the `main_*.py` lines as soon
as the function exists.

What this exam trains (from `WEAK_POINTS.md`): copy in a constructor, calling methods on `self`/`other`,
operators returning NEW objects, memoization with a `None` cache and a TUPLE key, iterative versions,
nested JSON (keys / values / indices, accumulators, skipping a summary key), return values of `sort`.

---

## 1. Durations

A duration is a number of hours and minutes, for instance 2 h 15.

### Q1. Create the `Duration` class
In `src/duration.py`, create a class `Duration`. The constructor takes `hours` and `minutes` (in this order)
and stores them in the attributes `hours` and `minutes`. It **normalises** them so that `0 <= minutes < 60`:
`Duration(1, 75)` has `hours == 2` and `minutes == 15`.

### Q2. Total minutes
Method `total_minutes(self)` returns the whole duration in minutes (an int): `Duration(2, 30)` gives `150`.

### Q3. String representation
`__repr__` returns `<hours>h<minutes on 2 digits>`: `Duration(2, 15)` is `2h15`, `Duration(0, 5)` is `0h05`.

### Q4. Addition and comparison
- `__add__` so that `d1 + d2` works. It **must** return a NEW `Duration` (the operands are not modified).
- `__lt__` so that `d1 < d2` is `True` when `d1` is STRICTLY shorter than `d2`. It must return a boolean.

### Q5. Multiplication
`__mul__` so that `d * k`, with `k` an integer, returns a NEW `Duration` lasting `k` times as long.

### Q6. The `Playlist` class
In the same file, create the class `Playlist`. Its constructor takes `durations` (a list of `Duration`) and stores a
**COPY** of the list in the attribute `durations` (adding an element to the original list later must not change
the playlist).
- `total(self)` returns the total duration as a NEW `Duration` (an empty playlist gives `Duration(0, 0)`);
- `longest(self)` returns the longest `Duration` of the playlist, or `None` if it is empty.

### Q7. Test in `main_duration.py`
In `main_duration.py`:
- create `Duration(1, 45)` and `Duration(0, 50)`;
- print their sum;
- print the SHORTER of the two (use `<`);
- print the first one multiplied by 3.

---

## 2. Climbing stairs

A child climbs a staircase of `n` steps. At each move, they climb **1, 2 or 3 steps**.
`ways(n)` is the number of different sequences of moves to climb exactly `n` steps:

```
ways(0) = 1
ways(n) = 0                                         if n < 0
ways(n) = ways(n-1) + ways(n-2) + ways(n-3)         for n >= 1
```

First values: 1, 1, 2, 4, 7, 13, 24, 44...
Check by hand: `ways(3) = ways(2) + ways(1) + ways(0) = 2 + 1 + 1 = 4`.

### Q1. Recursive version
In `src/stairs.py`, write `ways(n: int) -> int` that follows the formula with recursion.

### Q2. Memoization
Write `ways_memo(n: int, cache=None) -> int`. It must be recursive and use a dictionary so that each value is
computed only once. `n` is the only mandatory parameter. It must work if it is called several times in a row
(be careful with the default value of `cache`).

### Q3. Iterative version
Write `ways_iter(n: int) -> int` WITHOUT recursion: build a list `values` where `values[k]` is `ways(k)`,
from `k = 0` up to `n`. (Careful with the first values: `values[k-2]` and `values[k-3]` do not exist for small `k`.)

### Q4. Stirling numbers (two arguments)
`stirling2(n, k)` is the number of ways to split `n` different objects into exactly `k` non-empty groups.

```
S(0, 0) = 1
S(n, 0) = 0 for n >= 1        S(0, k) = 0 for k >= 1
S(n, k) = k * S(n-1, k) + S(n-1, k-1)       for n >= 1 and k >= 1
```

Check: `S(3, 2) = 2*S(2, 2) + S(2, 1) = 2*1 + 1 = 3`.
Write `stirling2(n: int, k: int, cache=None) -> int`: recursive, with a dictionary. The key of the dictionary must
hold BOTH `n` and `k`. It must work when called several times in a row.

### Q5. Complexity (write it in a comment above each function)
Give the time complexity of `ways_memo`, `ways_iter` and `stirling2` (count the additions or the multiplications).
Explain in one sentence why `ways` is much slower.

### Q6. Test in `main_stairs.py`
Compute `ways_memo(40)` and `stirling2(10, 3)` and print them as `ways(40) = VALUE` and `S(10, 3) = VALUE`.

---

## 3. JSON data manipulation: a greenhouse

A gardener records one JSON entry per day. The file `data/greenhouse.json` becomes a nested dictionary once loaded.
The keys are the **day numbers, as strings** (`"301"`, `"302"`...). Some days are missing from the file.

```json
"301": {
    "TEMP":     {"av": 13.67, "ct": 800, "mn": 11.1, "mx": 21.7},
    "HUMIDITY": {"av": 58.4,  "ct": 484, "mn": 30.5, "mx": 90.2},
    "PLANTS": {
        "mint":  {"family": "herb", "height_cm": 146},
        "thyme": {"family": "herb", "height_cm": 99},
        "tallest": {"name": "mint", "height_cm": 146}
    },
    "Weather": "windy",
    "Gardener": "Maya"
}
```

- `TEMP` is the temperature in degrees. `av` = average, `ct` = count, `mn` = minimum, `mx` = maximum.
- `PLANTS` maps the name of each plant to its `family` and its `height_cm`.
  The key `"tallest"` is NOT a plant: it is a summary, you must skip it.

All the functions take `data` (the loaded dictionary) as first parameter.
Write them in `src/greenhouse.py`. Try them in `main_greenhouse.py`.

1. `load_data(file_path)` : read the JSON file and return the dictionary.
   (If you cannot, `from src.greenhouse_data import GREENHOUSE_DATA` gives you the dictionary.)
2. `count_days(data)` : return the number of days (int).
3. `get_avg_temp(data, days)` : `days` is a list of integers. Return the average of the `TEMP` `av` values over
   these days (float). A day that is not in the data is ignored (and not counted). If no day is valid, return `None`.
4. `get_extreme_temp(data)` : return `((day_min, mn), (day_max, mx))`: the day (as an **integer**) with the lowest
   `TEMP` `mn`, with that value, and the day with the highest `TEMP` `mx`, with that value.
5. `count_by_weather(data)` : return a dictionary `{weather: number of days with that weather}`.
6. `get_tallest_plants(data, top_n=2)` : return a dictionary `{day (str): [(plant name, height_cm), ...]}` where each
   list holds the `top_n` plants with the biggest `height_cm`, sorted in descending order. Skip the key `"tallest"`.
7. `get_meters_by_family(data)` : return a dictionary `{family: total height in METERS}` (sum of the `height_cm` of
   all the plants of that family, over ALL the days, divided by 100). Skip the key `"tallest"`.
8. **Bonus** `days_with_plant(data, plant_name)` : return the SORTED list of the days (as integers) in which the
   plant appears.

---

## Upload your work (in the real exam)

```bash
git add .
git commit -m "..."
git push origin main
```
