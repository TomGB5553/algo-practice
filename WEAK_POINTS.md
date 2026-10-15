# My weak points : diagnosis from mock exam A, mock exam B and the training exam

Written from the files pushed on GitHub (`exam_A`, `exam_B`) and `training-exam`.
The good news first: your **ideas are mostly right** (the structure of `get_hours_by_type`, `grid_paths`, `height`,
`count_leaves`, `contains`, `count_by_moon_phase` are correct). The lost points come from a small number of
repeated habits. Fix these 8 habits and most of the failures disappear.

## The 8 habits to fix (with the evidence in your files)

| # | Habit | Where it happened | Rule to apply | Exercise |
|---|-------|-------------------|---------------|----------|
| 1 | **Mixing up key / value / index** in loops | `for i in self.coeffs: self.coeffs[i]`; `for night in data: night["SEEING"]`; `target["type"]` where `target` is a string key; `for i in n:` (n is an int) | Before each `[...]` ask "what TYPE is this variable?". `for x in d` gives keys; `.items()` gives (key, inner dict); `range(len(l))` gives indices; `for i in n` needs `range(n)`. | `weak_points/ex1` |
| 2 | **Accumulators badly initialised or not updated** | `min, max = None`; `count` never incremented in `get_avg_seeing`; `biggest = []` then `biggest["Mass_earth"]`; `list = []` created INSIDE the loop; `counts[method] = sum.get(...)`; `out[planet] += 1` (key is the whole dict, not `planet["Method"]`) | Write the 5 questions: start value? created where (BEFORE the loop)? what changes per turn? empty input? what do I return? | `weak_points/ex2` |
| 3 | **Return value vs side effect** | `return out.sort()` returns `None`; `list.append(a, b)` takes ONE argument; `out.append(collect_infix(...))` nests lists; `planets_between` returns `None` instead of `[]` | `sort/append/extend/insert/remove/reverse` return `None`. `sorted()` and `+` give new lists. `append` one element, `extend`/`+` several. | `weak_points/ex3` |
| 4 | **Memoization written but not working** | `catalan(n, cache=None)` then `n in cache` crashes; cache never filled; `grid_paths_memo` calls the NON-memo `grid_paths`; no `catalan_memo` at all | The template: `if cache is None: cache = {}` / base case / `if n in cache: return cache[n]` / compute with recursive calls that pass `cache` / `cache[n] = result` / `return result`. Key = tuple for 2 arguments. | `weak_points/ex4` + `snippets/recursion_classics.py` |
| 5 | **Formula typos in iterative versions** | `catalan_iter`: `values[i] + values[k-1-i]` (should be `*`) and `range(n)` (should be `range(k)`); `evaluate`: `x**i` without the coefficient | Do ONE tiny case by hand (here C_3) and compare with the code line by line. | `weak_points/ex4`, `snippets/recursion_classics.py` |
| 6 | **Wrong names / signature** | `count_by_methods` instead of `count_by_method`; `degrees` instead of `degree`; `planets.apend`; `catalan` given a cache parameter | Copy the names from the statement. The grader calls the exact names. After writing, run the tests and read the FIRST error. | `weak_points/ex5` |
| 7 | **Built-in names reused as variables** | `sum = {}`, `list = []`, `min, max = ...` | Never call a variable `sum`, `list`, `min`, `max`, `dict`, `str`, `len`, `input`. Use `total`, `result`, `lowest`, `highest`. | `weak_points/ex2` |
| 8 | **Time management: functions left empty** | `__mul__`, `insertion_sort`, `binary_strings`, `flatten`, `is_bst`, `catalan_memo`, `main_*.py` files | 1) Do the easy questions of EVERY exercise first. 2) Never spend more than 5 min stuck: write `pass`, move on, come back. 3) Write the `main_*.py` lines as soon as the function exists (they are free points). | all |

## Smaller points

* **Trees** (very good!) : only `collect_infix` was wrong. Write `return infix(left) + [node.value] + infix(right)`;
  `[node.value]` is a LIST, and never call the function on `node.value`.
* **Stray `print(...)` at module level** (`print(catalan(3))`, `print(load_data("data/observatory.json"))`)
  runs at import and can crash the tests. Test in `main_*.py` instead, inside `if __name__ == "__main__":`.
* **Docstring template left empty** (`"""_summary_ ... _description_"""`): either fill it in one line or delete it.
* **Complexity comments** (asked in Q4 / Q5): not written yet. Template: `# O(n^2) multiplications: C_k needs k products, 1+2+...+n`.
* **Training exam**: quiz Q1 wrong (aliasing: `y = x` does not copy), Q2-Q4 empty; `update_year(2035)` instead of `2022`.
  Answers: `solutions/training_quiz_answers.md`.
* `list_slicing.py` is a good start. The full version is in `snippets/python_recipes.py` (section 3).

## The plan (about 6 hours spread over a week)

| Step | What | Time |
|------|------|------|
| 1 | Re-read the 8 habits above. Fix `exam_A` and `exam_B` yourself with `python -m pytest` until green (compare with `solutions/` only AFTER). | 1 h 30 |
| 2 | `python3 weak_points/run_checks.py ex1`, then `ex2`, `ex3` (one per day, 20-30 min each). | 1 h 30 |
| 3 | `ex4` (recursion/memo/trees) + read `snippets/recursion_classics.py` and `trees.py`. | 1 h |
| 4 | `ex5` (classes) then `ex6` (full JSON + CSV mini exam, 25 min timed). | 1 h |
| 5 | Quiz: `quiz/quiz_extra.md` in 3 sessions of 12 questions; the answers explain each trap. | 45 min |
| 6 | Last day: redo exam A under real conditions (1 h, snippets allowed, no AI) and push. | 1 h |

Run the exercises with:

```bash
cd practice
python3 weak_points/run_checks.py          # all files: TODO / FAIL / OK per function
python3 weak_points/run_checks.py ex2 -v   # one file, with the full traceback
```
