class Vector2D:
    """A vector of the plane: (x, y)."""

    # Q1 : the constructor stores the two parameters in attributes (self.x / self.y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Q2 : called by `v1 + v2`. `self` is v1, `other` is v2.
    # We build and return a NEW vector: we never modify self or other.
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    # Q3 : called by print(v). It must RETURN a string (not print it).
    # f"...{expr}..." : the expression between braces is replaced by its value.
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    # Q4 : squared length. No square root needed to compare lengths.
    def norm_squared(self):
        return self.x * self.x + self.y * self.y

    # Q4 : called by `v1 < v2`. True if v1 is shorter than v2.
    def __lt__(self, other):
        return self.norm_squared() < other.norm_squared()

    # Q5 : called by `v * k`. k is a number, not a vector.
    def __mul__(self, k):
        return Vector2D(self.x * k, self.y * k)
