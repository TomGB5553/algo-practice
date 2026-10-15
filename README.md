# Exam practice pack

Built from the **2025 exam** (structure and difficulty), the **2024 exam**, your 5 projects (and every
error that had to be fixed in them) and the `learn-python` notebooks.

The real 2025 exam had: a 10-question quiz, then 3 exercises in 1 hour:
a class with special methods (`Rational`), recursion + memoization (`Bernoulli`), and nested-JSON
manipulation (`insight`). Both mock exams below copy that format, with new subjects.

## What is inside

| Folder / file | What it is | Time |
|---------------|-----------|------|
| `HOW_TO_REASON.md` | The 7-step method, the 11 patterns, worked examples, the 10 mistakes that cost points. **Read first.** | 20 min |
| `CHEATSHEET.md` | Syntax + complexity table: print it, or copy it on your A4 sheet. | |
| `SNIPPET_MAP.md` | Which of YOUR project files to open for each kind of question (you can use your projects in the exam). | |
| `drills/find_the_bug.py` | 18 functions with ONE bug each (bugs seen in your projects + classic beginner traps). Fix them. | 40 min |
| `drills/write_from_scratch.py` | 18 functions to write, from easy to exam level (dicts, indices, recursion). | 2-3 h total |
| `drills/trace_by_hand.md` | 12 snippets: predict the output on paper (aliasing, slices, recursion order, traversals). | 30 min |
| `quiz/quiz_practice.md` | 20 questions in the exam format. | 15 min |
| `exam_A/` | Mock exam A: `Vector2D` class / Catalan numbers (recursion + memo) / observatory JSON. Like the 2025 exam. | 1 h |
| `exam_B/` | Mock exam B: `Polynomial` / grids + strings recursion / exoplanets CSV + your own sort / trees. A bit harder. | 1 h 15 |
| `WEAK_POINTS.md` | Diagnosis of your mistakes in mock exams A, B and the training exam, with a plan. **Read second.** | 10 min |
| `weak_points/` | 6 exercise files (68 functions) aimed at those mistakes. Check with `python3 weak_points/run_checks.py`. | 3-4 h |
| `snippets/` | Tested example code to reuse: recursion/memo/iteration, JSON, CSV, trees, classes, recipes, complexity. Index in `snippets/README.md`. | |
| `quiz/quiz_extra.md` | 36 more quiz questions (answers + explanations in `solutions/quiz_extra_answers.md`). | 35 min |
| `solutions/training_quiz_answers.md` | Answers of the training-exam quiz + summary of the real-exam instructions. | |
| `solutions/` | All the solutions, commented with the reasoning. **Do not open before trying.** | |

## Suggested plan (about 2 weeks, 1 h per day)

1. Day 1: read `HOW_TO_REASON.md` and `CHEATSHEET.md`. Do `quiz/quiz_practice.md`, check with `solutions/quiz_answers.md`.
2. Days 2-3: `drills/find_the_bug.py` (whole), then `drills/trace_by_hand.md`.
3. Days 4-7: `drills/write_from_scratch.py`, 3-4 functions per day. For each one, FIRST do the example by hand on paper.
4. Day 8: **mock exam A** under exam conditions (timer, only your projects/notebooks/A4).
5. Days 9-11: redo what failed. Rewrite from memory the functions you needed to look up.
6. Day 12: **mock exam B** under exam conditions.
7. Last days: re-read your own corrected project files and `SNIPPET_MAP.md`; redo the drills that you failed.

## How to run the tests

From `practice/` (drills):

```bash
python -m pytest drills/test_find_the_bug.py
python -m pytest drills/test_write_from_scratch.py -k running_sum      # one function
```

From `practice/exam_A` or `practice/exam_B` (mock exams):

```bash
python -m pytest
python -m pytest tests/test_vector.py
```

(You need `pytest`: `pip install pytest`, or with uv: `uv run --with pytest python -m pytest`.)

## Rules to get real value out of it

- Write on paper before you type. Trace by hand before you run.
- Read only the FIRST error of the tests. A `KeyError`, `IndexError`, `TypeError` message tells you the line and the cause.
- After each exercise, once the tests pass, ask: "which pattern was it?" and "what was my mistake?" Write the mistake
  on your A4 sheet if it is a syntax one.
- The tests only check part of the grading: the real exam also checks that names, return types, recursion/memo/iteration
  requirements are respected, and that you wrote the complexity comments. Do the same here.
- When you finish a mock exam, compare with `solutions/`, then **rewrite** (not copy) the parts you missed.

## For maintenance

`uv run --with pytest python solutions/check_all.py` checks that every solution still passes its tests.
