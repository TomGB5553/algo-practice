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
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def mean(self):
        raise NotImplementedError

    def median(self):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def __mul__(self, k):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError


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
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def length(self):
        raise NotImplementedError

    def contains(self, x):
        raise NotImplementedError

    def overlaps(self, other):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def __lt__(self, other):
        raise NotImplementedError

    def shift(self, d):
        raise NotImplementedError


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
        raise NotImplementedError

    def add(self, name, qty):
        raise NotImplementedError

    def remove(self, name, qty):
        raise NotImplementedError

    def quantity(self, name):
        raise NotImplementedError

    def total(self):
        raise NotImplementedError

    def most_stocked(self):
        raise NotImplementedError

    def low_stock(self, threshold):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError
