# Practice quiz (same format as the real exam)

> Tick ONE answer per question by writing `[X]` (no space). Do not modify any other line.

## Question 1

What does this print?

```python
l = [1, 2, 3]
l.append([4, 5])
print(len(l))
```

-   [ ] 5
-   [ ] 4
-   [ ] 3
-   [ ] 2

## Question 2

Which line creates a dictionary with the key "a" mapped to 1?

-   [ ] d = {"a", 1}
-   [ ] d = {"a": 1}
-   [ ] d = ("a": 1)
-   [ ] d = ["a": 1]

## Question 3

What is the value of `t[1:3]` for `t = [10, 20, 30, 40]`?

-   [ ] [10, 20, 30]
-   [ ] [20, 30, 40]
-   [ ] [20, 30]
-   [ ] [10, 20]

## Question 4

`d` is a dict that does not contain the key "x". What does `d.get("x", 0)` return?

-   [ ] KeyError
-   [ ] None
-   [ ] 0
-   [ ] "x"

## Question 5

What is the result of `7 // 2` and of `7 % 2` ?

-   [ ] 3.5 and 1
-   [ ] 3 and 1
-   [ ] 4 and 1
-   [ ] 3 and 0.5

## Question 6

A function ends without any `return`. What does a call to it give?

-   [ ] 0
-   [ ] an empty string
-   [ ] None
-   [ ] an error

## Question 7

What is the difference between `names.sort()` and `sorted(names)`?

-   [ ] no difference
-   [ ] sort() sorts in place and returns None; sorted() returns a new sorted list
-   [ ] sorted() sorts in place; sort() returns a new list
-   [ ] sort() only works on numbers

## Question 8

The CSV file gives the string "9" and the string "10". What is `"9" < "10"`?

-   [ ] True, because 9 < 10
-   [ ] False, because strings are compared character by character and "9" > "1"
-   [ ] an error
-   [ ] True, because Python converts the strings to numbers

## Question 9

In a class, why do we write `self.count = self.count + 1` and not `count = count + 1` in a method?

-   [ ] both are the same
-   [ ] without self, count is a local variable (or an error), the attribute is not changed
-   [ ] self is only a naming convention with no effect
-   [ ] count would be a global variable

## Question 10

Which method is called by `print(obj)` to get a text for the object?

-   [ ] __init__
-   [ ] __str__ if it exists, else __repr__
-   [ ] __add__
-   [ ] __lt__

## Question 11

What does `a + b` call, where a and b are instances of your class?

-   [ ] a.add(b)
-   [ ] a.__add__(b)
-   [ ] b.__add__(a)
-   [ ] add(a, b)

## Question 12

What is the time complexity of this function?

```python
def f(n):
    i = 1
    while i < n:
        i = i * 2
```

-   [ ] O(n)
-   [ ] O(n^2)
-   [ ] O(log n)
-   [ ] O(1)

## Question 13

What is the time complexity of this function?

```python
def g(l):
    for a in l:
        for b in l:
            if a == b:
                pass
    for a in l:
        pass
```

-   [ ] O(n)
-   [ ] O(n^2 + n) = O(n)
-   [ ] O(n^2)
-   [ ] O(2n)

## Question 14

The recursive Fibonacci without memoization has a time complexity of about:

-   [ ] O(n)
-   [ ] O(n^2)
-   [ ] O(log n)
-   [ ] O(2^n)

## Question 15

Which of these sorting algorithms has a worst case of O(n^2) AND an average case of O(n log n)?

-   [ ] merge sort
-   [ ] bubble sort
-   [ ] quick sort
-   [ ] selection sort

## Question 16

Why can binary search NOT be used on any list?

-   [ ] it needs the list to be sorted
-   [ ] it needs the list to have an even length
-   [ ] it only works on integers
-   [ ] it needs the list to be stored in a dict

## Question 17

What does this code print?

```python
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)
print(f(4))
```

-   [ ] 4
-   [ ] 24
-   [ ] 10
-   [ ] an infinite recursion

## Question 18

A tree is traversed and visits the nodes in the order: left subtree, right subtree, root. This is:

-   [ ] prefix (pre-order)
-   [ ] infix (in-order)
-   [ ] postfix (post-order)
-   [ ] breadth-first

## Question 19

Binary search tree built by inserting 5, 3, 8, 1, 4 in this order. What is its infix traversal?

-   [ ] 5 3 1 4 8
-   [ ] 1 3 4 5 8
-   [ ] 1 4 3 8 5
-   [ ] 5 3 8 1 4

## Question 20

What does a Python function receive when you pass it a list and it calls `.append` on it?

-   [ ] a copy: the caller's list is unchanged
-   [ ] the same list: the caller's list IS modified
-   [ ] an error, lists are immutable
-   [ ] a tuple
