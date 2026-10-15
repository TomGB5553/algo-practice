"""
COMPLEXITY : HOW TO COUNT, WHAT TO WRITE IN THE COMMENT, HOW TO MEASURE

Run:  python3 snippets/complexity_and_timing.py

=============================  HOW TO ANSWER "give the time complexity"  =============================
 1. Say WHAT you count (multiplications, comparisons, calls...) and with respect to WHAT (n = ...).
 2. Count how many times the innermost line runs, keep the dominant term, drop constants.
 3. One sentence of justification:  "one loop of n turns -> O(n)", "2 nested loops -> O(n^2)".

    # catalan_memo : O(n^2) multiplications : each C_k (k = 0..n) is computed once and needs k products,
    #                1 + 2 + ... + n = n(n+1)/2.
    # catalan      : exponential : the same C_k are recomputed an enormous number of times (no cache).

COMMON CASES
    single loop over n                                  O(n)
    loop inside a loop (both up to n)                   O(n^2)
    loop where the variable is DOUBLED/HALVED           O(log n)
    halving + a loop of n at each level (merge sort)    O(n log n)
    recursion with 2 calls on n-1 (fibo, no memo)       O(2^n)
    recursion with 1 call on n-1                        O(n)
    recursion with 1 call on n/2                        O(log n)
    memoized recursion                                  (number of distinct arguments) x (work per call)
    dict / set lookup, list append, list[i]             O(1)       list `in`, list.index, list.insert(0, x)   O(n)
    sorted() / list.sort()                              O(n log n)
    slicing l[a:b]                                      O(b - a)   (a COPY is made)
    string concatenation in a loop                      O(n^2) in theory (strings are copied); use "".join(list)

TABLE (n elements)
                   best         average        worst        stable   in place
    bubble sort    O(n)*        O(n^2)         O(n^2)       yes      yes        (*with the `swapped` flag)
    insertion sort O(n)         O(n^2)         O(n^2)       yes      yes
    selection sort O(n^2)       O(n^2)         O(n^2)       no       yes
    merge sort     O(n log n)   O(n log n)     O(n log n)   yes      no (O(n) extra)
    quick sort     O(n log n)   O(n log n)     O(n^2)       no       yes (in-place version)
    linear search  O(1)         O(n)           O(n)
    binary search  O(1)         O(log n)       O(log n)     needs a SORTED list
    BST find/insert O(1)        O(log n)       O(n)         worst case = tree is a chain (sorted inserts)
"""
import timeit


# ---------------------------------------------------------------------------------------------
# Functions with a KNOWN number of operations: count them, then compare with the formula
# ---------------------------------------------------------------------------------------------
def count_single_loop(n):
    ops = 0
    for i in range(n):
        ops += 1
    return ops                                   # n


def count_double_loop(n):
    ops = 0
    for i in range(n):
        for j in range(n):
            ops += 1
    return ops                                   # n^2


def count_triangle_loop(n):
    ops = 0
    for i in range(n):
        for j in range(i):
            ops += 1
    return ops                                   # 0 + 1 + ... + (n-1) = n(n-1)/2  -> still O(n^2)


def count_doubling_loop(n):
    ops, i = 0, 1
    while i < n:
        i *= 2
        ops += 1
    return ops                                   # about log2(n)


def count_fibo_calls(n):
    """Number of calls made by the naive fibo(n): grows like 1.6^n."""
    if n < 2:
        return 1
    return 1 + count_fibo_calls(n - 1) + count_fibo_calls(n - 2)


# ---------------------------------------------------------------------------------------------
# MEASURE the time of a function (course project: fibo_time.py, sorting_time.py)
# ---------------------------------------------------------------------------------------------
def measure(function, argument, repeat=3):
    """Best time in seconds over `repeat` runs."""
    return min(timeit.repeat(lambda: function(argument), number=1, repeat=repeat))


def measure_growth(function, sizes):
    """[(n, seconds), ...]. Plot it with matplotlib:  plt.plot(ns, ts); plt.xscale('log'); plt.yscale('log')"""
    return [(n, measure(function, n)) for n in sizes]


"""
MATPLOTLIB MINIMUM (copy-paste)
    import matplotlib.pyplot as plt
    ns, ts = zip(*measure_growth(f, [100, 200, 400]))
    plt.plot(ns, ts, marker="o", label="f")
    plt.xlabel("n"); plt.ylabel("time (s)"); plt.title("..."); plt.legend()
    plt.xscale("log"); plt.yscale("log")        # a straight line on log-log = a power law (slope = exponent)
    plt.savefig("fig.png")  # or plt.show()
"""

# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    assert count_single_loop(100) == 100
    assert count_double_loop(10) == 100
    assert count_triangle_loop(10) == 45
    assert count_doubling_loop(1024) == 10
    assert count_fibo_calls(10) == 177 and count_fibo_calls(20) == 21891      # explodes: no memo!

    def slow_sum(n):
        return sum(i * i for i in range(n))

    t_small = measure(slow_sum, 10_000)
    t_big = measure(slow_sum, 100_000)
    assert t_big > t_small                       # O(n): about 10 x slower for 10 x bigger
    print(f"time ratio for 10x bigger input: {t_big / t_small:.1f} (expected about 10 for O(n))")

    print("complexity_and_timing: all OK")
