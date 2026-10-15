"""
RECURSION CLASSICS : each problem in 3 versions
    1. recursive            (direct translation of the formula)
    2. recursive + memo     (a dict `cache` so each value is computed ONCE)
    3. iterative            (a loop that fills a list/variables from the smallest case up)

Run this file:  python3 snippets/recursion_classics.py   -> prints "all OK" if every check passes.

THE RECIPE (always the same)
    a) find the BASE CASE(S)      : the input so small that you know the answer
    b) find the RECURSIVE CASE    : answer(n) written with answer of SMALLER inputs
    c) memo   : `if n in cache: return cache[n]` ... compute ... `cache[n] = result` ... `return result`
    d) iter   : `values = [base cases]` then `for k in range(...): values.append(formula using values)`

THE MEMO TRAP (lost points in mock exam A and B)
    def f(n, cache=None):
        if cache is None:      # NEVER write `cache={}` in the signature: the same dict is reused
            cache = {}         # between calls
        ...
        f(n - 1, cache)        # and ALWAYS pass `cache` in the recursive calls
"""


# ---------------------------------------------------------------------------------------------
# 1. FACTORIAL            n! = n * (n-1)!        0! = 1
# ---------------------------------------------------------------------------------------------
# time O(n), recursion depth n
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


# time O(n)
def factorial_iter(n):
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


# (no memo needed: each call is made once. Memo only helps when the SAME value is asked many times.)


# ---------------------------------------------------------------------------------------------
# 2. FIBONACCI            F(0)=0  F(1)=1  F(n) = F(n-1) + F(n-2)
# ---------------------------------------------------------------------------------------------
# time O(2^n) (really O(phi^n)): two calls per call and the same F(k) is recomputed again and again
def fibo(n):
    if n < 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


# time O(n): each F(k) computed once -> n additions
def fibo_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    result = fibo_memo(n - 1, cache) + fibo_memo(n - 2, cache)
    cache[n] = result
    return result


# time O(n), memory O(n) with the list; (O(1) memory with two variables, see fibo_iter_2vars)
def fibo_iter(n):
    values = [0, 1]
    for k in range(2, n + 1):
        values.append(values[k - 1] + values[k - 2])
    return values[n]


def fibo_iter_2vars(n):
    a, b = 0, 1            # F(0), F(1)
    for _ in range(n):
        a, b = b, a + b    # tuple assignment: both right-hand sides are computed BEFORE assigning
    return a


# ---------------------------------------------------------------------------------------------
# 3. CATALAN NUMBERS      C_0 = 1     C_n = sum for i in 0..n-1 of C_i * C_(n-1-i)
# ---------------------------------------------------------------------------------------------
# time O(4^n / n^1.5) roughly exponential: the same C_k are recomputed many times
def catalan(n):
    if n == 0:
        return 1
    total = 0
    for i in range(n):
        total += catalan(i) * catalan(n - 1 - i)
    return total


# time O(n^2): C_0..C_n each computed once, C_k needs k multiplications -> 1+2+...+n = n(n+1)/2
def catalan_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n == 0:
        return 1
    if n in cache:
        return cache[n]
    total = 0
    for i in range(n):
        total += catalan_memo(i, cache) * catalan_memo(n - 1 - i, cache)
    cache[n] = total
    return total


# time O(n^2) multiplications (same count), no recursion
def catalan_iter(n):
    values = [1]                                   # values[k] = C_k
    for k in range(1, n + 1):
        total = 0
        for i in range(k):                         # range(k) NOT range(n)
            total += values[i] * values[k - 1 - i]  # a PRODUCT, not a sum
        values.append(total)
    return values[n]


# ---------------------------------------------------------------------------------------------
# 4. GRID PATHS (2 arguments -> the cache KEY is a tuple)
#    robot goes right/down from top-left to bottom-right of a rows x cols grid
# ---------------------------------------------------------------------------------------------
# time O(2^(rows+cols)) exponential
def grid_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return grid_paths(rows - 1, cols) + grid_paths(rows, cols - 1)


# time O(rows * cols): there are rows*cols different keys, each computed once with 1 addition
def grid_paths_memo(rows, cols, cache=None):
    if cache is None:
        cache = {}
    if rows == 1 or cols == 1:
        return 1
    key = (rows, cols)                              # tuple = hashable = usable as a dict key
    if key in cache:
        return cache[key]
    result = grid_paths_memo(rows - 1, cols, cache) + grid_paths_memo(rows, cols - 1, cache)
    cache[key] = result
    return result


# time O(rows * cols), a 2D table filled line by line
def grid_paths_iter(rows, cols):
    table = [[1] * cols for _ in range(rows)]       # first row and first column are all 1
    for r in range(1, rows):
        for c in range(1, cols):
            table[r][c] = table[r - 1][c] + table[r][c - 1]
    return table[rows - 1][cols - 1]


# ---------------------------------------------------------------------------------------------
# 5. BINOMIAL COEFFICIENT / PASCAL'S TRIANGLE   C(n,k) = C(n-1,k-1) + C(n-1,k)
# ---------------------------------------------------------------------------------------------
# time O(2^n)
def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return binomial(n - 1, k - 1) + binomial(n - 1, k)


# time O(n*k)
def binomial_memo(n, k, cache=None):
    if cache is None:
        cache = {}
    if k == 0 or k == n:
        return 1
    if (n, k) in cache:
        return cache[(n, k)]
    cache[(n, k)] = binomial_memo(n - 1, k - 1, cache) + binomial_memo(n - 1, k, cache)
    return cache[(n, k)]


# the n-th row of Pascal's triangle, built line by line. time O(n^2)
def pascal_row(n):
    row = [1]
    for _ in range(n):
        # each new value = sum of the two values above it (missing ones count as 0)
        row = [a + b for a, b in zip([0] + row, row + [0])]
    return row


# ---------------------------------------------------------------------------------------------
# 6. POWER AND FAST EXPONENTIATION (halving the problem -> O(log n))
# ---------------------------------------------------------------------------------------------
# time O(n)
def power_slow(x, n):
    if n == 0:
        return 1
    return x * power_slow(x, n - 1)


# time O(log n): n is halved at each call
def power_fast(x, n):
    if n == 0:
        return 1
    half = power_fast(x, n // 2)         # compute ONCE and reuse (calling it twice would be O(n) again)
    if n % 2 == 0:
        return half * half
    return half * half * x


# time O(log n), loop version (binary exponentiation)
def power_iter(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result


# ---------------------------------------------------------------------------------------------
# 7. GCD (Euclid)         gcd(a, 0) = a     gcd(a, b) = gcd(b, a % b)
# ---------------------------------------------------------------------------------------------
# time O(log(min(a,b)))
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_iter(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# ---------------------------------------------------------------------------------------------
# 8. SUM OF DIGITS / COUNT DIGITS / REVERSE A NUMBER  (n // 10 removes the last digit, n % 10 reads it)
# ---------------------------------------------------------------------------------------------
# time O(number of digits)
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def digit_sum_iter(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def to_binary(n):
    """to_binary(10) -> '1010'  (last bit = n % 2, the rest = to_binary(n // 2))"""
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# ---------------------------------------------------------------------------------------------
# 9. STAIRS : ways to climb n steps taking 1 or 2 steps at a time (it IS Fibonacci in disguise)
# ---------------------------------------------------------------------------------------------
# time O(2^n)
def stairs(n):
    if n <= 1:
        return 1
    return stairs(n - 1) + stairs(n - 2)


# time O(n)
def stairs_memo(n, cache=None):
    if cache is None:
        cache = {}
    if n <= 1:
        return 1
    if n not in cache:
        cache[n] = stairs_memo(n - 1, cache) + stairs_memo(n - 2, cache)
    return cache[n]


def stairs_iter(n):
    values = [1, 1]
    for k in range(2, n + 1):
        values.append(values[k - 1] + values[k - 2])
    return values[n]


# ---------------------------------------------------------------------------------------------
# 10. COUNT CHANGE : in how many ways can `amount` be paid with `coins` (order does not matter)?
#     ways(amount, coins) = ways(amount - coins[0], coins)   [use coins[0] at least once]
#                         + ways(amount, coins[1:])          [never use coins[0]]
# ---------------------------------------------------------------------------------------------
# time exponential
def count_change(amount, coins):
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    return count_change(amount - coins[0], coins) + count_change(amount, coins[1:])


# time O(amount * len(coins)): the key is (amount, number of coins still allowed)
def count_change_memo(amount, coins, cache=None):
    if cache is None:
        cache = {}
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    key = (amount, len(coins))          # coins[1:] is always the same list for a given len -> len is enough
    if key not in cache:
        cache[key] = (count_change_memo(amount - coins[0], coins, cache)
                      + count_change_memo(amount, coins[1:], cache))
    return cache[key]


# time O(amount * len(coins)): the classic "one coin at a time" table
def count_change_iter(amount, coins):
    ways = [1] + [0] * amount           # ways[a] = number of ways to pay a
    for coin in coins:
        for a in range(coin, amount + 1):
            ways[a] += ways[a - coin]
    return ways[amount]


# ---------------------------------------------------------------------------------------------
# 11. COLLATZ : number of steps to reach 1 (n even -> n/2, n odd -> 3n+1). A recursion WITHOUT a formula in n.
# ---------------------------------------------------------------------------------------------
def collatz_steps(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz_steps(n // 2)
    return 1 + collatz_steps(3 * n + 1)


def collatz_steps_iter(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


# ---------------------------------------------------------------------------------------------
# 12. LONGEST COMMON SUBSEQUENCE (2 strings -> cache key = (i, j) positions)
# ---------------------------------------------------------------------------------------------
# time O(len(a) * len(b)) with memo, exponential without
def lcs_length(a, b, i=0, j=0, cache=None):
    if cache is None:
        cache = {}
    if i == len(a) or j == len(b):
        return 0
    if (i, j) in cache:
        return cache[(i, j)]
    if a[i] == b[j]:
        result = 1 + lcs_length(a, b, i + 1, j + 1, cache)
    else:
        result = max(lcs_length(a, b, i + 1, j, cache), lcs_length(a, b, i, j + 1, cache))
    cache[(i, j)] = result
    return result


# ---------------------------------------------------------------------------------------------
# 13. TIMING comparison (what the course project did with timeit)
# ---------------------------------------------------------------------------------------------
def compare_times(n=25):
    import timeit
    t_rec = timeit.timeit(lambda: fibo(n), number=1)
    t_memo = timeit.timeit(lambda: fibo_memo(n), number=1)
    t_iter = timeit.timeit(lambda: fibo_iter(n), number=1)
    return t_rec, t_memo, t_iter


# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    assert [factorial(n) for n in range(6)] == [1, 1, 2, 6, 24, 120]
    assert factorial_iter(5) == 120

    assert [fibo(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fibo_memo(50) == fibo_iter(50) == fibo_iter_2vars(50) == 12586269025
    assert fibo_memo(10) == 55 and fibo_memo(10) == 55          # twice in a row: the cache bug would show

    assert [catalan(n) for n in range(8)] == [1, 1, 2, 5, 14, 42, 132, 429]
    assert catalan_memo(30) == catalan_iter(30) == 3814986502092304

    assert grid_paths(3, 7) == grid_paths_memo(3, 7) == grid_paths_iter(3, 7) == 28
    assert grid_paths_memo(18, 18) == grid_paths_iter(18, 18) == 2333606220

    assert binomial(5, 2) == binomial_memo(5, 2) == 10
    assert pascal_row(4) == [1, 4, 6, 4, 1]

    assert power_slow(2, 10) == power_fast(2, 10) == power_iter(2, 10) == 1024
    assert power_fast(3, 7) == power_iter(3, 7) == 2187

    assert gcd(48, 18) == gcd_iter(48, 18) == 6

    assert digit_sum(1234) == digit_sum_iter(1234) == 10
    assert to_binary(10) == "1010" and to_binary(0) == "0"

    assert stairs(10) == stairs_memo(10) == stairs_iter(10) == 89

    assert count_change(11, [1, 5, 10]) == count_change_memo(11, [1, 5, 10]) == count_change_iter(11, [1, 5, 10]) == 4

    assert collatz_steps(6) == collatz_steps_iter(6) == 8

    assert lcs_length("ABCBDAB", "BDCABA") == 4

    print("recursion_classics: all OK")
