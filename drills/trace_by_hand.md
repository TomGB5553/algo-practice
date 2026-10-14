# DRILL 3 : PREDICT THE OUTPUT (trace by hand)

For each snippet, WRITE on paper what it prints, step by step (a small table of the variables
after each loop turn is the best tool). Only then run it to check, and read the answer in
`../solutions/drills/trace_answers.md`. This is the skill that lets you find your own bugs
without a test: executing the code in your head.

## 1. Loop and accumulator

```python
total = 0
for i in range(1, 5):
    total += i * 2
print(total)
```

Prints:  

## 2. Aliasing: two names, one list

```python
a = [1, 2, 3]
b = a
b.append(4)
c = list(a)
c.append(5)
print(a, b, c)
```

Prints:  

## 3. Slices and negative indices

```python
s = [10, 20, 30, 40, 50]
print(s[1:3], s[:2], s[-2:], s[::-1], s[-1])
```

Prints:  

## 4. Dictionary counting

```python
counts = {}
for ch in "abracadabra":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)
print(sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:2])
```

Prints:  

## 5. Return inside or after the loop

```python
def f(numbers):
    for n in numbers:
        if n > 2:
            return n
    return -1

print(f([1, 2, 3, 4]), f([1, 2]), f([]))
```

Prints:  

## 6. Function that modifies its argument

```python
def add_one(l):
    l.append(1)
    return l

def add_one_copy(l):
    l = l + [1]
    return l

x = [0]
y = add_one(x)
z = add_one_copy(x)
print(x, y, z)
```

Prints:  

## 7. sort() vs sorted()

```python
names = ["bob", "al", "cy"]
r1 = sorted(names)
r2 = names.sort()
print(r1, r2, names)
```

Prints:  

## 8. Recursion: the call order

```python
def show(n):
    if n == 0:
        return
    print("down", n)
    show(n - 1)
    print("up", n)

show(3)
```

Prints:  

## 9. Recursion: count the calls

```python
calls = 0
def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(5), calls)
```

Prints:  

## 10. Class with __add__ and __repr__

```python
class V:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return V(self.x + other.x)
    def __repr__(self):
        return f"V({self.x})"

a = V(1)
b = V(2)
c = a + b
print(a, b, c, a is c)
```

Prints:  

## 11. Traversal orders

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

def prefix(n):
    return [] if n is None else [n.value] + prefix(n.left) + prefix(n.right)
def infix(n):
    return [] if n is None else infix(n.left) + [n.value] + infix(n.right)
def postfix(n):
    return [] if n is None else postfix(n.left) + postfix(n.right) + [n.value]

t = Node(4, Node(2, Node(1), Node(3)), Node(6, None, Node(7)))
print(prefix(t)); print(infix(t)); print(postfix(t))
```

Prints:  

## 12. Nested loops and complexity

```python
count = 0
n = 6
for i in range(n):
    for j in range(i, n):
        count += 1
print(count)
```

Prints:  
