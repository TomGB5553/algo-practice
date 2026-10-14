# Answers of the trace drill

## 1. Loop and accumulator

```
20
```

## 2. Aliasing: two names, one list

```
[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4, 5]
```

## 3. Slices and negative indices

```
[20, 30] [10, 20] [40, 50] [50, 40, 30, 20, 10] 50
```

## 4. Dictionary counting

```
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
[('a', 5), ('b', 2)]
```

## 5. Return inside or after the loop

```
3 -1 -1
```

## 6. Function that modifies its argument

```
[0, 1] [0, 1] [0, 1, 1]
```

## 7. sort() vs sorted()

```
['al', 'bob', 'cy'] None ['al', 'bob', 'cy']
```

## 8. Recursion: the call order

```
down 3
down 2
down 1
up 1
up 2
up 3
```

## 9. Recursion: count the calls

```
5 15
```

## 10. Class with __add__ and __repr__

```
V(1) V(2) V(3) False
```

## 11. Traversal orders

```
[4, 2, 1, 3, 6, 7]
[1, 2, 3, 4, 6, 7]
[1, 3, 2, 7, 6, 4]
```

## 12. Nested loops and complexity

```
21
```
