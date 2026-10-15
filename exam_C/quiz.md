# Quiz (mock exam C)

> [!warning]
>
> **Please only write `[X]` without spaces for the answers you want to
>  select, do not add/modify other lines!**
>
> Each question has only one correct answer.

## Question 1

What does this print?

```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```

-   [ ] [4]
-   [ ] [1, 2, 3]
-   [X] [1, 2, 3, 4]
-   [ ] Error

## Question 2

A function must return a sorted copy of its list parameter `l` and leave `l` unchanged. Which body is right?

-   [ ] return l.sorted()
-   [ ] l.sort()
return l
-   [X] return sorted(l)
-   [ ] return l.sort()

## Question 3

`data` is a dict loaded from JSON: `{"7": {"v": 1}, "8": {"v": 2}}`. What is `x` in `for x in data:`?

-   [X] "7"
-   [ ] 0
-   [ ] {"v": 1}
-   [ ] ("7", {"v": 1})

## Question 4

In a class, `__lt__(self, other)` must compare the lengths given by the method `length()`. Which line is right?

-   [ ] return self.length(other) < self.length()
-   [X] return self.length() < other.length()
-   [ ] return self < other
-   [ ] return length(self) < length(other)

## Question 5

Which constructor stores a COPY of the list `items`?

-   [X] self.items = items
-   [ ] self.items = list(items)
-   [ ] items = self.items
-   [ ] self.items == items

## Question 6

What does this print?

```python
def f(n, cache=None):
    if n in cache:
        return cache[n]
    return 0

print(f(0))
```

-   [ ] Error
-   [ ] [0]
-   [X] 0
-   [ ] 1

## Question 7

Time complexity of `stirling2(n, k)` with a cache whose keys are `(n, k)` (one addition and one multiplication per key)?

-   [ ] O(2^n)
-   [X] O(n + k)
-   [ ] O(log n)
-   [ ] O(n * k)

## Question 8

What does `print(ways_iter(3))` print, with this code?

```python
def ways_iter(n):
    values = [1]
    for k in range(1, n + 1):
        values.append(values[k - 1] + values[k - 2] + values[k - 3])
    return values[n]
```

-   [ ] 3
-   [ ] IndexError
-   [ ] 4
-   [ ] 1

## Question 9

`planets_between` ends with `return names.sort()`. What does the caller receive?

-   [ ] None
-   [ ] A sorted copy
-   [ ] An empty list
-   [X] The sorted list

## Question 10

Which statement about this call is true?  `get_avg(data, [1, 2, 3])` where keys "1" and "2" exist in `data` but "3" does not, and the statement says "a day that is not in the data is ignored".

-   [ ] Raise a KeyError
-   [ ] Return None
-   [ ] Divide the total by 3
-   [X] Divide the total by 2
