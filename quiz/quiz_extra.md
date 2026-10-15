# Extra quiz : 36 questions (same format as the real exam)

> Tick ONE answer per question by writing `[X]` (no space). Do not modify any other line.
> Answers: `solutions/quiz_extra_answers.md` (do not open before you finish).
> Suggested: 10 questions = 10 minutes. For code questions, answer on paper BEFORE running anything.

## Question 1

What does this print?

```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)
```

-   [ ] [4]
-   [ ] Error
-   [ ] [1, 2, 3, 4]
-   [ ] [1, 2, 3]

## Question 2

What does the last line print?

```python
def f(x, l=[]):
    l.append(x)
    return l

f(1)
print(f(2))
```

-   [ ] [1, 2]
-   [ ] [2]
-   [ ] [1]
-   [ ] Error

## Question 3

What does this print?

```python
l = [3, 1, 2]
r = l.sort()
print(r)
```

-   [ ] [3, 1, 2]
-   [ ] [1, 2, 3]
-   [ ] None
-   [ ] Error

## Question 4

What does this print?

```python
print("10" < "9")
```

-   [ ] Error
-   [ ] True
-   [ ] None
-   [ ] False

## Question 5

What does this print?

```python
for i in range(3):
    if i == 1:
        break
else:
    print("done")
print(i)
```

-   [ ] 2
-   [ ] 1
-   [ ] done
-   [ ] done 1

## Question 6

`t = (1, 2, 3)` then `t[0] = 9`. What happens?

-   [ ] IndexError
-   [ ] t becomes (9, 2, 3)
-   [ ] ValueError
-   [ ] TypeError

## Question 7

What is printed?

```python
print(7 // 2, -7 // 2)
```

-   [ ] 3 -4
-   [ ] 3 -3
-   [ ] 3.5 -3.5
-   [ ] 4 -4

## Question 8

What does this print?

```python
x = [[0] * 2] * 2
x[0][0] = 1
print(x)
```

-   [ ] [[0, 0], [0, 0]]
-   [ ] [[1, 0], [0, 0]]
-   [ ] Error
-   [ ] [[1, 0], [1, 0]]

## Question 9

What does `print(len({1, 2, 2, 3, 3, 3}))` print?

-   [ ] 6
-   [ ] Error
-   [ ] 3
-   [ ] 4

## Question 10

What does this print?

```python
def g(n):
    if n == 0:
        return
    print(n, end=" ")
    g(n - 1)
    print(n, end=" ")

g(2)
```

-   [ ] 2 1 1 2
-   [ ] 2 1
-   [ ] 2 2 1 1
-   [ ] 1 2 2 1

## Question 11

What does `f(4)` return?

```python
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)
```

-   [ ] 10
-   [ ] 4
-   [ ] 24
-   [ ] Infinite recursion

## Question 12

Why is `def fibo_memo(n, cache={})` dangerous?

-   [ ] A dictionary cannot be a default value (SyntaxError)
-   [ ] It is slower than `cache=None`
-   [ ] The dictionary is created once and shared between ALL the calls
-   [ ] It makes the function iterative

## Question 13

Time complexity of the naive recursive `fibo(n)` (two calls: n-1 and n-2)?

-   [ ] O(n^2)
-   [ ] O(log n)
-   [ ] O(2^n)
-   [ ] O(n)

## Question 14

Time complexity of `fibo_memo(n)` (with a cache dictionary)?

-   [ ] O(log n)
-   [ ] O(2^n)
-   [ ] O(n^2)
-   [ ] O(n)

## Question 15

Time complexity of this code?

```python
for i in range(n):
    for j in range(i):
        count += 1
```

-   [ ] O(n^2)
-   [ ] O(2^n)
-   [ ] O(log n)
-   [ ] O(n)

## Question 16

Time complexity of this code?

```python
while n > 1:
    n = n // 2
```

-   [ ] O(n)
-   [ ] O(n log n)
-   [ ] O(1)
-   [ ] O(log n)

## Question 17

Computing `catalan_memo(n)` by filling `values[0..n]`, how many multiplications are made?

-   [ ] About n
-   [ ] About n log n
-   [ ] About n(n+1)/2, so O(n^2)
-   [ ] About 2^n

## Question 18

Which sort takes O(n) time on an ALREADY SORTED list?

-   [ ] All of them
-   [ ] Selection sort
-   [ ] Merge sort
-   [ ] Insertion sort

## Question 19

A sort is "stable" when...

-   [ ] it works on sorted lists only
-   [ ] items with equal keys keep their original relative order
-   [ ] it is faster than O(n log n)
-   [ ] it never uses extra memory

## Question 20

In `Vector2D`, which line is the correct body of `__lt__`?

-   [ ] return self < other
-   [ ] return norm_squared(self) < norm_squared(other)
-   [ ] return self.norm_squared(other)
-   [ ] return self.norm_squared() < other.norm_squared()

## Question 21

What must `__repr__` do?

-   [ ] return the attributes as a tuple
-   [ ] return a string
-   [ ] return None
-   [ ] print the object

## Question 22

`v1 + v2` is the same as...

-   [ ] v2.__add__(v1)
-   [ ] v1.add(v2)
-   [ ] v1.__add__(v2)
-   [ ] __add__(v1, v2) as a free function

## Question 23

A class constructor receives a list `coeffs`. The statement says "stores a COPY". Which line?

-   [ ] coeffs = self.coeffs
-   [ ] self.coeffs = list(coeffs)
-   [ ] self.coeffs = coeffs
-   [ ] self.coeffs == coeffs

## Question 24

`data = json.load(file)` gives `{"101": {"SEEING": {"av": 2.9}}}`. How do you read 2.9?

-   [ ] data[101]["SEEING"]["av"]
-   [ ] data.101.SEEING.av
-   [ ] data["101"]["SEEING"]["av"]
-   [ ] data["101"].SEEING["av"]

## Question 25

`data` is a dict. In `for night in data:`, what is `night`?

-   [ ] a key (a string here)
-   [ ] a value (the inner dict)
-   [ ] an index 0, 1, 2...
-   [ ] a (key, value) tuple

## Question 26

With `csv.DictReader`, what is the type of `row["Year"]`?

-   [ ] int
-   [ ] str
-   [ ] float
-   [ ] depends on the file

## Question 27

You want a function to return a sorted list of names. Which line is correct?

-   [ ] return names.sort()
-   [ ] return names.sorted()
-   [ ] return sorted(names)
-   [ ] names.sort(); return None

## Question 28

What is the postfix (left, right, node) traversal of this tree?  Root 5; left child 2 with children 1 and 3; right child 8.

-   [ ] 1 2 3 5 8
-   [ ] 5 2 8 1 3
-   [ ] 5 2 1 3 8
-   [ ] 1 3 2 8 5

## Question 29

Height (number of nodes on the longest path) of a tree whose root has ONE child, which has two leaf children?

-   [ ] 3
-   [ ] 2
-   [ ] 1
-   [ ] 4

## Question 30

Which test is correct for an empty subtree?

-   [ ] if node == 0:
-   [ ] if node is None:
-   [ ] if node = None:
-   [ ] if not node.value:

## Question 31

What does the last line print?

```python
s = [1, 2, 3]
def m(l):
    l = l + [4]
    return l
def m2(l):
    l.append(4)
m(s)
m2(s)
print(s)
```

-   [ ] None
-   [ ] [4]
-   [ ] [1, 2, 3, 4]
-   [ ] [1, 2, 3]

## Question 32

`sum = 0` is written at the top of a file, and later `sum([1, 2, 3])` is called. What happens?

-   [ ] TypeError: 'int' object is not callable
-   [ ] 6
-   [ ] NameError
-   [ ] 0

## Question 33

What does this print?

```python
print(sorted(["pear", "fig", "kiwi"], key=len))
```

-   [ ] fig pear kiwi
-   [ ] ['fig', 'kiwi', 'pear']
-   [ ] ['kiwi', 'fig', 'pear']
-   [ ] ['fig', 'pear', 'kiwi']

## Question 34

What does this print?

```python
a, b = 1, 2
a, b = b, a + b
print(a, b)
```

-   [ ] 1 2
-   [ ] 2 3
-   [ ] 2 2
-   [ ] 1 3

## Question 35

What does this print?

```python
print(round(2.5), round(3.5))
```

-   [ ] 3 3
-   [ ] 2 4
-   [ ] 2 3
-   [ ] 3 4

## Question 36

Which expression correctly tests if two floats are "equal"?

-   [ ] abs(a - b) < 1e-9
-   [ ] a.equals(b)
-   [ ] a == b
-   [ ] a is b
