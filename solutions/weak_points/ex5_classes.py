"""
EX 5 : CLASSES AND SPECIAL METHODS
   (your mistakes: `self.norm_squared(self) < self.norm_squared(other)`, missing COPY of the list in the constructor,
    method name different from the statement (`degrees` instead of `degree`), `__mul__` left empty)

Checklist for each class:  self first parameter / attributes through self / call methods with self.method()
/ operators return a NEW object / __repr__ RETURNS the exact format / names exactly as in the statement.
"""


class Stats:
    """A list of numbers with statistics.
    - Stats(values): stores a COPY of the list in the attribute `values`
    - repr(Stats([1, 2])) == "Stats([1, 2])"
    - len(s): number of values                                    (__len__)
    - mean(): average, or None if empty
    - median(): middle value (average of the 2 middle values if even count), None if empty
    - s1 + s2: NEW Stats containing the values of s1 then those of s2     (__add__)
    - s1 < s2: True when the mean of s1 is smaller than the mean of s2    (__lt__) (use self.mean(), other.mean())
    - s * k: NEW Stats with every value multiplied by k                  (__mul__)
    - add(x): append x to this Stats (modifies self, returns None)
    """

    def __init__(self, values):
        self.values = list(values)

    def __repr__(self):
        return f"Stats({self.values})"

    def __len__(self):
        return len(self.values)

    def mean(self):
        if len(self.values) == 0:
            return None
        return sum(self.values) / len(self.values)

    def median(self):
        if len(self.values) == 0:
            return None
        ordered = sorted(self.values)
        middle = len(ordered) // 2
        if len(ordered) % 2 == 1:
            return ordered[middle]
        return (ordered[middle - 1] + ordered[middle]) / 2

    def __add__(self, other):
        return Stats(self.values + other.values)

    def __lt__(self, other):
        return self.mean() < other.mean()

    def __mul__(self, k):
        return Stats([v * k for v in self.values])

    def add(self, x):
        self.values.append(x)


class Interval:
    """A closed interval [low, high] of numbers (low <= high is guaranteed).
    - Interval(low, high) with attributes `low` and `high`
    - repr -> "[1, 5]"                                          (__repr__)
    - length(): high - low
    - contains(x): True if low <= x <= high
    - overlaps(other): True if the two intervals share at least one point
    - __add__(other): the SMALLEST interval containing both (NEW object)
    - __eq__(other): same low and same high
    - __lt__(other): self is shorter than other (use self.length() and other.length())
    - shift(d): MODIFY self by adding d to both ends (returns None)
    """

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __repr__(self):
        return f"[{self.low}, {self.high}]"

    def length(self):
        return self.high - self.low

    def contains(self, x):
        return self.low <= x <= self.high

    def overlaps(self, other):
        return self.low <= other.high and other.low <= self.high

    def __add__(self, other):
        return Interval(min(self.low, other.low), max(self.high, other.high))

    def __eq__(self, other):
        return self.low == other.low and self.high == other.high

    def __lt__(self, other):
        return self.length() < other.length()

    def shift(self, d):
        self.low += d
        self.high += d


class Inventory:
    """A shop stock: a dict {item name: quantity}.
    - Inventory(): empty stock, attribute `stock` (a NEW dict for each object!)
    - add(name, qty): increase the quantity (create the item if needed)
    - remove(name, qty): decrease; raise ValueError("not enough") if the stock is too small or the item unknown
    - quantity(name): current quantity, 0 if unknown
    - total(): total number of items in stock
    - most_stocked(): NAME of the item with the biggest quantity, None if empty
    - low_stock(threshold): sorted list of the names whose quantity is STRICTLY below threshold
    - repr -> "Inventory(3 kinds, 12 items)"
    """

    def __init__(self):
        self.stock = {}

    def add(self, name, qty):
        self.stock[name] = self.stock.get(name, 0) + qty

    def remove(self, name, qty):
        if self.stock.get(name, 0) < qty:
            raise ValueError("not enough")
        self.stock[name] -= qty

    def quantity(self, name):
        return self.stock.get(name, 0)

    def total(self):
        total = 0
        for qty in self.stock.values():
            total += qty
        return total

    def most_stocked(self):
        best = None
        for name in self.stock:
            if best is None or self.stock[name] > self.stock[best]:
                best = name
        return best

    def low_stock(self, threshold):
        return sorted(name for name, qty in self.stock.items() if qty < threshold)

    def __repr__(self):
        return f"Inventory({len(self.stock)} kinds, {self.total()} items)"
