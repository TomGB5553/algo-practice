"""
CLASSES AND SPECIAL ("dunder") METHODS   (the "Vector2D / Rational / Polynomial" exercise)

Run:  python3 snippets/classes_special_methods.py

=============================  RULES  =============================
 1. Every method has `self` as FIRST parameter. You never pass it when calling:   v.norm_squared()
 2. Attributes are read/written through self:   self.x = x   (without `self.` it is a local variable)
 3. Call another method with `self.method(...)`, and on the OTHER object with `other.method()`.
        WRONG  self.norm_squared(other)      RIGHT  self.norm_squared() < other.norm_squared()
 4. Operators that make a NEW object (+, *, -) must NOT modify self or other.
 5. __repr__ must RETURN a string (never print). Follow the format of the statement character by character.
 6. A constructor that receives a list should store a COPY if asked:   self.coeffs = list(coeffs)  or coeffs[:]
 7. Do not give a method a name close to the statement's name and hope: the tests call the EXACT name.

TABLE OF SPECIAL METHODS
    __init__(self, ...)   constructor                    V(1, 2)
    __repr__(self)        string shown by print / REPL   print(v)
    __add__(self, other)  v + w          __sub__  v - w          __mul__  v * k          __neg__  -v
    __eq__(self, other)   v == w         __lt__   v < w          __le__   v <= w
    __len__(self)         len(v)         __getitem__(self, i)    v[i]             __iter__  for x in v
    __contains__(self, x) x in v         __bool__ if v:          __hash__  (needed to use as dict key when __eq__ is defined)
    __radd__ / __rmul__   k * v  when k is an int (the left operand does not know the class)
"""
from math import gcd, sqrt


# ---------------------------------------------------------------------------------------------
# 1. Vector2D
# ---------------------------------------------------------------------------------------------
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"      # f-string: the `f` before the quotes enables {...}

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, k):                            # v * 3
        return Vector2D(self.x * k, self.y * k)

    def __rmul__(self, k):                           # 3 * v
        return self * k

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __eq__(self, other):
        return isinstance(other, Vector2D) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def norm_squared(self):
        return self.x * self.x + self.y * self.y

    def norm(self):
        return sqrt(self.norm_squared())

    def __lt__(self, other):                         # v < w  <=>  v is SHORTER than w
        return self.norm_squared() < other.norm_squared()

    def dot(self, other):
        return self.x * other.x + self.y * other.y


# ---------------------------------------------------------------------------------------------
# 2. Rational (the 2025 exam class): always stored in lowest terms, denominator > 0
# ---------------------------------------------------------------------------------------------
class Rational:
    def __init__(self, num, den=1):
        if den == 0:
            raise ValueError("denominator cannot be 0")
        if den < 0:                                  # the sign is carried by the numerator
            num, den = -num, -den
        g = gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        return Rational(self.num * other.den + other.num * self.den, self.den * other.den)

    def __mul__(self, other):
        return Rational(self.num * other.num, self.den * other.den)

    def __eq__(self, other):
        return self.num == other.num and self.den == other.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den   # cross-multiplication (denominators > 0)

    def __float__(self):
        return self.num / self.den


# ---------------------------------------------------------------------------------------------
# 3. Polynomial : coeffs = [a0, a1, a2, ...] from LOWEST to HIGHEST degree
# ---------------------------------------------------------------------------------------------
class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs)                   # a COPY

    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    def degree(self):
        """Index of the last non-zero coefficient, -1 for the zero polynomial."""
        for i in range(len(self.coeffs) - 1, -1, -1):    # from the END
            if self.coeffs[i] != 0:
                return i
        return -1

    def evaluate(self, x):
        total = 0
        for power, coeff in enumerate(self.coeffs):      # enumerate gives (index, value)
            total += coeff * x ** power                  # coefficient TIMES x^power
        return total

    def __add__(self, other):
        size = max(len(self.coeffs), len(other.coeffs))
        result = []
        for i in range(size):                            # range(size), NOT `for i in size`
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result.append(a + b)
        return Polynomial(result)

    def __mul__(self, other):
        if not self.coeffs or not other.coeffs:
            return Polynomial([])
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
                result[i + j] += a * b                   # a_i x^i * b_j x^j = a_i b_j x^(i+j)
        return Polynomial(result)

    def derivative(self):
        return Polynomial([i * c for i, c in enumerate(self.coeffs)][1:])


# ---------------------------------------------------------------------------------------------
# 4. A class that HOLDS a list and analyses it (NeoAnalyzer / Stack / BankAccount style)
# ---------------------------------------------------------------------------------------------
class Stack:
    """LIFO: last in, first out. All operations O(1)."""

    def __init__(self):
        self.items = []                              # attribute created in __init__, NOT shared (no class-level list!)

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


class Queue:
    """FIFO: first in, first out. Use collections.deque for an O(1) popleft."""

    def __init__(self):
        from collections import deque
        self.items = deque()

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)


class Car:
    """The training-exam class."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.brand} {self.model}"

    def update_year(self, new_year):
        self.year = new_year                         # a method that MODIFIES self returns nothing


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []                            # mutable default created INSIDE __init__

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        self.history.append(("withdraw", amount))


class Analyzer:
    """Holds a list of dicts and answers questions about it."""

    def __init__(self, records):
        self.records = records

    def average(self, field):
        if not self.records:
            return None
        return sum(r[field] for r in self.records) / len(self.records)

    def filter(self, predicate):
        return [r for r in self.records if predicate(r)]     # a function passed as argument

    def best(self, field):
        return max(self.records, key=lambda r: r[field]) if self.records else None


# ---------------------------------------------------------------------------------------------
# 5. INHERITANCE
# ---------------------------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def __repr__(self):
        return f"{type(self).__name__}({self.name!r})"


class Dog(Animal):
    def __init__(self, name, tricks=0):
        super().__init__(name)                       # initialise the parent part
        self.tricks = tricks

    def speak(self):                                 # overrides the parent method
        return "Woof"


# ---------------------------------------------------------------------------------------------
# 6. SORTING OBJECTS : sorted() uses __lt__, or give a key
# ---------------------------------------------------------------------------------------------
def longest_first(vectors):
    return sorted(vectors, reverse=True)             # uses Vector2D.__lt__


# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    v1, v2 = Vector2D(3, 4), Vector2D(-1, 2)
    assert repr(v1 + v2) == "Vector2D(2, 6)" and (v1.x, v2.x) == (3, -1)     # operands unchanged
    assert str(v1 * 3) == "Vector2D(9, 12)" and str(3 * v1) == "Vector2D(9, 12)"
    assert v1.norm_squared() == 25 and v1.norm() == 5.0
    assert v2 < v1 and not v1 < v2
    assert (v1 if v2 < v1 else v2) == v1
    assert v1 == Vector2D(3, 4) and len({v1, Vector2D(3, 4)}) == 1
    assert longest_first([v2, v1]) == [v1, v2]
    assert -v1 == Vector2D(-3, -4) and v1.dot(v2) == 5

    a, b = Rational(1, 2), Rational(1, 3)
    assert repr(a + b) == "5/6" and repr(a * b) == "1/6" and repr(Rational(2, -4)) == "-1/2"
    assert Rational(2, 4) == Rational(1, 2) and b < a and abs(float(a) - 0.5) < 1e-12

    p, q = Polynomial([1, 2, 3]), Polynomial([4, 5])
    assert repr(p + q) == "Polynomial([5, 7, 3])"
    assert repr(p * q) == "Polynomial([4, 13, 22, 15])"
    assert p.degree() == 2 and Polynomial([1, 2, 0, 0]).degree() == 1 and Polynomial([]).degree() == -1
    assert Polynomial([3, 2, 5]).evaluate(2) == 27
    assert repr(Polynomial([1, 1]) * Polynomial([1, 1])) == "Polynomial([1, 2, 1])"
    assert repr(p.derivative()) == "Polynomial([2, 6])"
    original = [1, 2]
    poly = Polynomial(original)
    original.append(99)
    assert poly.coeffs == [1, 2]                     # it holds a copy

    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2 and s.peek() == 1 and len(s) == 1 and not s.is_empty()
    qu = Queue()
    qu.enqueue("a")
    qu.enqueue("b")
    assert qu.dequeue() == "a" and len(qu) == 1

    car = Car("Toyota", "Corolla", 2020)
    assert car.get_description() == "2020 Toyota Corolla"
    car.update_year(2022)
    assert car.get_description() == "2022 Toyota Corolla"

    acc = BankAccount("Ada")
    acc.deposit(50)
    acc.withdraw(20)
    assert acc.balance == 30 and acc.history == [("deposit", 50), ("withdraw", 20)]
    assert BankAccount("B").history is not acc.history

    an = Analyzer([{"v": 1}, {"v": 5}])
    assert an.average("v") == 3 and an.filter(lambda r: r["v"] > 2) == [{"v": 5}] and an.best("v") == {"v": 5}

    d = Dog("Rex")
    assert d.speak() == "Woof" and Animal("x").speak() == "..." and repr(d) == "Dog('Rex')"

    print("classes_special_methods: all OK")
