# Exercise 2 : stairs and Stirling numbers


# Q1 - time: exponential (about 1.84^n). Each call makes 3 calls and the same values are recomputed again and again.
def ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return ways(n - 1) + ways(n - 2) + ways(n - 3)


# Q2 - time: O(n). The values ways(0..n) are each computed once, with 2 additions.
def ways_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    result = ways_memo(n - 1, cache) + ways_memo(n - 2, cache) + ways_memo(n - 3, cache)
    cache[n] = result
    return result


# Q3 - time: O(n). One loop of n turns, 2 additions per turn.
def ways_iter(n):
    values = [1]
    for k in range(1, n + 1):
        total = values[k - 1]
        if k >= 2:
            total += values[k - 2]
        if k >= 3:
            total += values[k - 3]
        values.append(total)
    return values[n]


# Q4 - time: O(n * k). There are at most n*k different keys (n, k), each computed once with 1 multiplication
# and 1 addition.
def stirling2(n, k, cache=None):
    if cache is None:
        cache = {}
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    key = (n, k)
    if key in cache:
        return cache[key]
    result = k * stirling2(n - 1, k, cache) + stirling2(n - 1, k - 1, cache)
    cache[key] = result
    return result
