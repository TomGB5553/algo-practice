"""
EX 2 : ACCUMULATORS   (your mistakes: `min, max = None`, `count` never incremented, `list = []` INSIDE the loop,
                       `counts[method] = sum.get(...)` copy-paste, `out[planet]` instead of `out[planet["Method"]]`,
                       variables named `sum`, `list`, `min`, `max` that hide the Python functions)

The 5 questions to ask BEFORE writing the loop:
   1. What do I start from?  (0, [], {}, None)     2. Where is it created? (BEFORE the loop)
   3. What changes at each turn?                    4. What if the input is empty?   5. What do I return?
Do NOT use the built-ins sum / min / max / sorted unless the statement says you can.
"""


def average(numbers):
    """Mean of a list, None if the list is empty. average([1, 2, 6]) -> 3.0"""
    total = 0
    count = 0
    for x in numbers:
        total += x
        count += 1
    if count == 0:
        return None
    return total / count


def min_and_max(numbers):
    """(smallest, largest) with a loop, or None if the list is empty.  min_and_max([3, 9, 1]) -> (1, 9)"""
    if len(numbers) == 0:
        return None
    lowest = highest = numbers[0]
    for x in numbers:
        if x < lowest:
            lowest = x
        if x > highest:
            highest = x
    return lowest, highest


def index_of_max(numbers):
    """Index of the first occurrence of the largest value, -1 if empty. index_of_max([2, 9, 9, 1]) -> 1"""
    best = -1
    for i in range(len(numbers)):
        if best == -1 or numbers[i] > numbers[best]:
            best = i
    return best


def longest_word(words):
    """The longest word (the first one if there are ties), None if the list is empty."""
    best = None
    for w in words:
        if best is None or len(w) > len(best):
            best = w
    return best


def count_by_first_letter(words):
    """{first letter: number of words}   ["apple", "avocado", "kiwi"] -> {"a": 2, "k": 1}. Ignore empty strings."""
    counts = {}
    for w in words:
        if w == "":
            continue
        first = w[0]
        counts[first] = counts.get(first, 0) + 1
    return counts


def average_by_group(pairs):
    """pairs = [(group, value), ...]  ->  {group: average of its values}
    [("a", 1), ("b", 10), ("a", 3)] -> {"a": 2.0, "b": 10.0}
    You need TWO dictionaries (or one dict of lists): one for the totals, one for the counts.
    """
    totals = {}
    counts = {}
    for group, value in pairs:
        totals[group] = totals.get(group, 0) + value
        counts[group] = counts.get(group, 0) + 1
    return {group: totals[group] / counts[group] for group in totals}


def group_by_length(words):
    """{length: [words of that length, in original order]}   ["a", "bb", "c"] -> {1: ["a", "c"], 2: ["bb"]}"""
    groups = {}
    for w in words:
        n = len(w)
        if n not in groups:
            groups[n] = []                 # create the list ONLY the first time, never reset it
        groups[n].append(w)
    return groups


def best_per_group(records, group_field, value_field):
    """records = list of dicts. For each group return the NAME ("name" field) of the record with the biggest value.
    records = [{"name": "A", "g": 1, "v": 5}, {"name": "B", "g": 1, "v": 9}, {"name": "C", "g": 2, "v": 1}]
    best_per_group(records, "g", "v") -> {1: "B", 2: "C"}
    """
    best = {}
    for r in records:
        g = r[group_field]
        if g not in best or r[value_field] > best[g][value_field]:
            best[g] = r
    return {g: r["name"] for g, r in best.items()}


def second_largest(numbers):
    """Second largest DISTINCT value, None if there is none.  [3, 9, 5, 9] -> 5     [4, 4] -> None"""
    largest = None
    second = None
    for x in numbers:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x
    return second


def count_while(numbers, condition):
    """Number of elements at the BEGINNING of the list for which condition(x) is True, stopping at the first False.
    count_while([2, 4, 5, 6], lambda x: x % 2 == 0) -> 2
    """
    count = 0
    for x in numbers:
        if not condition(x):
            break
        count += 1
    return count
