# Q1 + Q5 : base case = one row or one column -> 1 path.
# Otherwise: paths arriving from above + paths arriving from the left.
# Complexity: the call tree has a node for each way of removing one row or
# one column, the same subproblems are recomputed again and again: the number
# of calls is about C(rows+cols-2, rows-1) (the answer itself, since the
# leaves each return 1) -> exponential in the size of the grid.
def grid_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1
    return grid_paths(rows - 1, cols) + grid_paths(rows, cols - 1)


# Q2 + Q5 : same recursion, but the cache key is the TUPLE (rows, cols)
# (a tuple can be a dict key, a list cannot).
# Complexity: there are rows*cols different subproblems, each solved once
# with O(1) work -> O(rows * cols).
def grid_paths_memo(rows, cols, cache=None):
    if cache is None:
        cache = {}

    if rows == 1 or cols == 1:
        return 1

    key = (rows, cols)
    if key in cache:
        return cache[key]

    result = grid_paths_memo(rows - 1, cols, cache) + grid_paths_memo(rows, cols - 1, cache)
    cache[key] = result
    return result


# Q3 + Q5 : the strings of length n are the strings of length n-1 with a "0"
# or a "1" put in front. Listing "0..." first keeps the increasing order.
# Complexity: the answer has 2^n strings of n characters, so O(n * 2^n)
# (O(2^n) strings): exponential, and it cannot be avoided because we must
# build all of them.
def binary_strings(n):
    if n == 0:
        return [""]

    shorter = binary_strings(n - 1)
    result = []
    for s in shorter:
        result.append("0" + s)
    for s in shorter:
        result.append("1" + s)
    return result


# Q4 : for each element, if it is a list flatten it recursively, otherwise keep it.
# Complexity: every element at every depth is looked at once: O(total number of elements).
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))  # extend adds all the elements of a list
        else:
            result.append(item)
    return result
