# Training exam : quiz answers + what to check before the real exam

Source: `training-exam/questions.md` (4 questions). Answers below; the file format rule is
**"only write `[X]` without spaces, do not add/modify other lines"**.

| Q | Correct answer | Why |
|---|----------------|-----|
| 1 | `[1, 2, 3, 4]` (2nd option) | `y = x` does NOT copy: `x` and `y` are two names for the SAME list, so `y.append(4)` also changes `x`. (You ticked `[1, 2, 3]`: that would be right with `y = x[:]` or `y = list(x)`.) |
| 2 | "Functions are first-class objects and can be passed as arguments" (3rd option) | A function can return several values (really one tuple), can be defined inside another function, and without `return` it returns `None`, so the other three statements are false. |
| 3 | `0 1 2 Done` (3rd option) | The `else` of a `for` runs when the loop ends normally (no `break`). The "only if a `break` is used" option is the opposite of the truth. |
| 4 | "A concise way to create a list using a loop inside square brackets" (3rd option) | `[x * x for x in range(5)]`. |

Your file currently has only Q1 ticked (wrongly) and Q2-Q4 empty. Tick exactly one option per question,
as `[X]`, for example `- [X] [1, 2, 3, 4]`.

## The rest of the training exam (the Car class) : review

Your `src/car.py` passes the test. Two things to fix in `main.py`:

* Q4 says "Update the `year` of the first one by setting to **2022**": you wrote `a.update_year(2035)`.
  Follow the numbers of the statement exactly.
* `src/car.py` still starts with the template comment; harmless, but clean files make a good impression.

## Instructions of the real exam, summarised (from `training-exam/README.md`)

Environment
* The exam is on **Linux** (ISAE computers), not on Windows.
* Fork the exam repository on GitLab: **do not change** the project name nor the slug, choose your own id as namespace,
  visibility **Private**. Add `j.detchart` as **Maintainer** (Manage > Members > Invite).
* Clone YOUR repository (HTTPS URL of the `Code` button), then in a terminal:
  ```bash
  module load anaconda3
  cd training-exam          # (the exam folder)
  code .                    # to open VS Code
  ```
* Run the tests: `pytest -v`. Run your code: `python main.py`.

Rules
* Forbidden: internet, any mobile device, any chat/email, any AI tool (Copilot, ChatGPT, Gemini...).
* Allowed: the course notes and website, your labs, your home directory, one A4 sheet with your own notes.

Upload (do it REGULARLY, not only at the end)
```bash
git add .
git commit -m "describe what you did"
git push origin main
```

Checklist for the last 5 minutes of the real exam
1. `pytest -v`: read the first failure of each file.
2. Every function has EXACTLY the name and parameters of the statement; classes too.
3. No `print(...)` left at the top level of the files in `src/` (it runs at import).
4. Complexity comments written where requested.
5. The quiz file: one `[X]` per question, no other line modified.
6. `git add . && git commit -m "..." && git push origin main`, then check on GitLab that the last commit is there.
