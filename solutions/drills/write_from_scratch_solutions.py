"""
Solutions of drills/write_from_scratch.py, each with the REASONING that leads to the code.
Read the reasoning, close the file, and try to rewrite the function yourself.
"""


def count_even(numbers):
    # Pattern "COUNT": a counter at 0, +1 when the condition is true.
    count = 0
    for n in numbers:
        if n % 2 == 0:  # % gives the remainder of the division; even <=> remainder 0
            count += 1
    return count


def running_sum(numbers):
    # Pattern "ACCUMULATE + BUILD A LIST": keep the total so far, append it at each step.
    # By hand: [1, 2, 3] -> total 1, 3, 6.
    result = []
    total = 0
    for n in numbers:
        total += n
        result.append(total)
    return result


def second_largest(numbers):
    # Pattern "FIND THE BEST", with TWO variables: the best and the second best so far.
    # None means "nothing seen yet" (no value can be smaller than "nothing").
    # By hand on [4, 9, 9, 7]: 4 -> first=4 | 9 -> second=4, first=9 | 9 -> same as first: ignore
    #                          | 7 -> 7 > second -> second=7.
    first = None
    second = None
    for n in numbers:
        if first is None or n > first:
            second = first   # the old best becomes the second (do this BEFORE changing first)
            first = n
        elif n != first and (second is None or n > second):
            second = n
    return second


def is_palindrome(text):
    # Clean the text first (lowercase, no spaces), then compare with its reverse.
    # text[::-1] is the slice "from the end to the start, step -1" = the reversed text.
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def word_frequencies(text):
    # Pattern "COUNT IN A DICT": dict.get(key, 0) avoids the KeyError of the first time.
    counts = {}
    for word in text.lower().split():  # .split() cuts at the spaces
        counts[word] = counts.get(word, 0) + 1
    return counts


def invert_dict(d):
    result = {}
    for key in d:
        result[d[key]] = key
    return result


def group_by_length(words):
    # Pattern "GROUP": the value is a list; create it the first time the key is seen.
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups


def nested_get(data, keys, default=None):
    # Go down one key at a time. At each step the current value must be a dict
    # that contains the key; if not, the path does not exist.
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


def top_n_by(items, field, n):
    # sorted(..., key=function, reverse=True) returns a NEW list (items is not modified);
    # [:n] keeps the n first elements (a slice never fails when n is too big).
    ordered = sorted(items, key=lambda item: item[field], reverse=True)
    return ordered[:n]


def remove_duplicates(items):
    # Pattern "FILTER with a memory": keep the elements already seen in a list (or a set).
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def transpose(matrix):
    # The new matrix has as many rows as the old one has columns.
    # new[j][i] = old[i][j].  By hand: [[1,2,3],[4,5,6]] -> column 0 = [1,4] is the new row 0...
    if len(matrix) == 0:
        return []
    result = []
    for j in range(len(matrix[0])):      # for each column j of the old matrix
        new_row = []
        for i in range(len(matrix)):     # go down the column
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def rotate_right(items, k):
    # Rotating by the length changes nothing, so k can be reduced with %.
    # The last k elements go in front: [1,2,3,4,5], k=2 -> [4,5] + [1,2,3].
    if len(items) == 0:
        return []
    k = k % len(items)
    if k == 0:
        return list(items)  # careful: items[-0:] would be the WHOLE list, so handle k = 0 apart
    return items[-k:] + items[:-k]


def merge_sorted(a, b):
    # Two "cursors" i and j: at each step take the smaller of a[i] and b[j] and move that cursor.
    # When one list is finished, copy what is left of the other one.
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


def index_of(sorted_numbers, target):
    # The interval [left, right] still to explore (both included). Look at the middle:
    # equal -> found; too small -> go right (left = mid + 1); too big -> go left (right = mid - 1).
    left = 0
    right = len(sorted_numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_numbers[mid] == target:
            return mid
        elif sorted_numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def balanced(text):
    # A STACK (last in, first out): push each opening bracket; on a closing bracket the
    # last opened one must match. At the end the stack must be empty.
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if len(stack) == 0 or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0


def digit_sum(n):
    # Base case: a single digit (n < 10) is its own sum.
    # Recursive case: last digit + digit_sum of the rest.  1234 -> 4 + digit_sum(123)
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def power(x, n):
    # x**0 = 1.  Even n: (x**(n/2))**2.  Odd n: x * x**(n-1).  n is halved every 2 calls -> O(log n).
    if n == 0:
        return 1
    if n % 2 == 1:
        return x * power(x, n - 1)
    half = power(x, n // 2)
    return half * half


def count_change(amount, coins):
    # Base cases: amount 0 -> exactly one way (pay nothing); amount < 0 or no coin left -> 0 ways.
    # Recursive case: ways WITHOUT the first coin + ways USING it at least once
    # (pay it, and the remaining amount can still use all the coins).
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    first = coins[0]
    return count_change(amount, coins[1:]) + count_change(amount - first, coins)
