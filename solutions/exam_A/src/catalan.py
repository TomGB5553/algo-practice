# Q1 : recursive version, straight from the definition.
# Base case: C_0 = 1 (without it, the recursion never stops).
# Recursive case: sum of C_i * C_(n-1-i) for i = 0..n-1.
def catalan(n):
    if n == 0:
        return 1

    total = 0
    for i in range(n):  # i = 0, 1, ..., n-1
        total += catalan(i) * catalan(n - 1 - i)
    return total


# Q2 + Q4 : memoized version.
# Complexity: C_k for k = 0..n is computed ONCE each (afterwards it is read
# in the cache in O(1)). Computing C_k costs k multiplications, so the total
# is 0 + 1 + ... + n = n(n+1)/2 multiplications  ->  O(n^2).
# (The plain version is exponential: it recomputes the same C_k an enormous
# number of times, the call tree explodes like for the naive Fibonacci.)
def catalan_memo(n, cache=None):
    # `cache={}` as a default value would be shared by ALL the calls, so
    # we use None and create a fresh dict at the first call.
    if cache is None:
        cache = {}

    if n == 0:
        return 1
    if n in cache:  # already computed: just read it
        return cache[n]

    total = 0
    for i in range(n):
        # the SAME cache is passed down to every recursive call
        total += catalan_memo(i, cache) * catalan_memo(n - 1 - i, cache)

    cache[n] = total  # store before returning
    return total


# Q3 + Q4 : iterative version (bottom-up): we compute C_0, then C_1, ...
# each one from the list of the previous ones.
# Complexity: the outer loop runs n times, the inner one k times -> n(n+1)/2
# multiplications -> O(n^2) time, O(n) memory (the list).
def catalan_iter(n):
    values = [1]  # values[0] = C_0

    for k in range(1, n + 1):
        total = 0
        for i in range(k):
            total += values[i] * values[k - 1 - i]
        values.append(total)  # now values[k] = C_k

    return values[n]
