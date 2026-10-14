# How to reason when you write an algorithm

Your difficulty is not "Python", it is going from a sentence of the exam to the first line of code.
Use ALWAYS the same 7 steps. Write them on the exam paper, in the comments of your file, not in your head.

## The 7 steps

1. **Input / output.** Write the signature with the TYPES. What goes in? What must come out
   (a number? a list? a dict? a tuple? `None` in some case?). Read the "Returns" line twice:
   most lost points come from returning the wrong thing (a dict instead of its name, a string key
   instead of an int, a print instead of a return).
2. **One small example by hand.** Take the example of the statement (or invent a tiny one, 3 elements)
   and solve it with a pencil. Write down EVERY step you do. Your steps ARE the algorithm.
3. **Find the pattern** (table below). 90% of the exam functions are one of ~8 patterns.
4. **The special cases.** Empty input? One element? Key missing? All negative? Duplicates?
   Write the `if` that handles them FIRST.
5. **Write the skeleton** (loops and variables, no details), then fill it.
6. **Run it on your example** from step 2, and compare line by line with what you did by hand.
7. **Run the tests**, read the FIRST failing assertion only, fix, repeat.

## The patterns (learn to recognise them)

| The statement says...                         | Pattern            | Skeleton |
|-----------------------------------------------|--------------------|----------|
| "number of ...", "how many"                   | COUNT              | `count = 0` / `for x in l:` / `if cond: count += 1` / `return count` |
| "sum of", "total", "average"                  | ACCUMULATE         | `total = 0` / `for x in l: total += x` ; average = `total / count` (check `count == 0`) |
| "the largest / smallest / best / the one with the most" | FIND THE BEST | `best = None` / `for x in l: if best is None or x > best: best = x` (return the NAME or the VALUE as asked) |
| "only those which ...", "keep the ..."        | FILTER             | `result = []` / `for x in l: if cond: result.append(x)` |
| "for each ... give ..." (a new value per item)| TRANSFORM          | `result = []` / `for x in l: result.append(f(x))` or a comprehension |
| "how many of each", "frequency", "by type"    | COUNT IN A DICT    | `counts[k] = counts.get(k, 0) + 1` |
| "group the ... by ..."                        | GROUP IN A DICT    | `if k not in groups: groups[k] = []` then `groups[k].append(x)` |
| "sorted", "top n", "the n biggest"            | SORT + SLICE       | `sorted(l, key=lambda x: x[...], reverse=True)[:n]` |
| "does it contain", "is there", "exists"       | SEARCH             | `for x in l: if x == target: return True` / after the loop `return False` |
| defined with itself (F(n) from F(n-1))        | RECURSION          | 1. base case(s) 2. recursive case on a SMALLER input 3. (memo: a cache dict) |
| tree / nested structure                       | RECURSION on children | `if node is None: return <neutral>` then combine the results of left and right |

## Worked example 1 : "average temperature of a list of sols, ignoring the missing ones, None if none valid"

1. Input: `data` (dict, keys are STRINGS), `sols` (list of int). Output: float or `None`.
2. By hand: data has "10" (av 2.0) and "11" (av 4.0). sols = [10, 12, 11]. 10 -> take 2.0. 12 -> not in
   data, skip. 11 -> take 4.0. Sum 6.0, count 2 -> 3.0. If sols = [12] -> nothing taken -> None.
3. Pattern: ACCUMULATE with a FILTER (+ an average, so keep a count).
4. Special cases: key must be converted with `str(sol)`; no valid sol -> count == 0 -> return None.
5. Code:
   ```python
   total = 0
   count = 0
   for sol in sols:
       key = str(sol)
       if key in data:
           total += data[key]["AT"]["av"]
           count += 1
   if count == 0:
       return None
   return total / count
   ```

## Worked example 2 : "Pascal's triangle row n, iteratively" (a reasoning exercise)

By hand: row 0 = [1]; row 1 = [1, 1]; row 2 = [1, 2, 1]; row 3 = [1, 3, 3, 1].
Observation: each inner element of a row is the sum of the two elements above it
(row 3, index 1: 1 + 2). The first and last are 1.
Algorithm: start with `row = [1]`; repeat n times: build `new_row` = `[1]`, then for i from 1 to len(row)-1
append `row[i-1] + row[i]`, then append `1`; `row = new_row`. Return `row`.
=> You found the algorithm by LOOKING at the example, not by "knowing" it.

## Worked example 3 : recursion = "assume the smaller problem is solved"

`flatten([1, [2, [3]], 4])`. Do not follow the whole call tree in your head!
Ask only: "if I already had `flatten` working for every SMALLER list, what do I do with ONE element?"
- the element is an int: keep it;
- the element is a list: it is smaller, so `flatten(element)` gives me its flat version: add it.
Base case: the loop simply ends on an empty list. Write the code from these 2 sentences.

## The 10 mistakes that cost you the most (all seen in your projects / the drills)

| Mistake                                                        | How to avoid it |
|----------------------------------------------------------------|-----------------|
| `print` instead of `return`                                    | The signature says "Returns": use `return` |
| `return` indented inside the `for` loop                        | `return` for the final result is at the level of the `for` |
| Forgetting that CSV values / JSON keys are strings             | `int(...)`, `float(...)`, `str(sol)` at the entry of the function |
| `counts[k] += 1` on a new key (KeyError)                       | `counts.get(k, 0) + 1`, or `if k not in counts` first |
| Starting a "best" variable at `0` (negative numbers)           | Start with `None` or with the first element |
| Division by zero on an empty list                              | `if len(l) == 0: return None` first |
| Modifying the list you received (append, sort, remove)         | `result = list(l)` or build a new list |
| `names.sort()` assigned to a variable (it is `None`)           | `sorted(names)` returns the new list |
| Skipping the summary key (`"longest"`, `"most_common"`)        | `if key == "longest": continue` |
| Forgetting the base case, or the base case that never happens  | Write the base case FIRST; check the smallest input (0, 1, empty) |

## What to do when you are stuck (exam survival)

- Skip, and come back: each question is independent.
- Write the function signature and `return None` so the file still runs.
- Partial credit exists: a correct loop with one wrong detail is better than nothing.
- Use `print(...)` on the intermediate variables of the failing test to see where it differs from your hand example.
- Open the matching project file (see `SNIPPET_MAP.md`): you are allowed to reuse your own code.
