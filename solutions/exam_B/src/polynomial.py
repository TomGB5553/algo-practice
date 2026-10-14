class Polynomial:
    """A polynomial stored as a list of coefficients, lowest degree first."""

    # Q1 : list(coeffs) makes a COPY. With `self.coeffs = coeffs` both names
    # would point to the same list and a later change of the original list
    # would silently change the polynomial.
    def __init__(self, coeffs):
        self.coeffs = list(coeffs)

    # Q2 : must RETURN the string (self.coeffs is printed like a list by the f-string)
    def __repr__(self):
        return f"Polynomial({self.coeffs})"

    # Q3 : look for the last non-zero coefficient, starting from the END.
    # range(a, b, -1) counts down: here len-1, len-2, ..., 0.
    def degree(self):
        for i in range(len(self.coeffs) - 1, -1, -1):
            if self.coeffs[i] != 0:
                return i
        return -1  # empty list or only zeros

    # Q4 : sum of coeff * x**i. enumerate(list) gives (index, element) pairs.
    def evaluate(self, x):
        total = 0
        for i, coeff in enumerate(self.coeffs):
            total += coeff * x ** i
        return total

    # Q5 : the result is as long as the LONGEST list. For each index i, take
    # the coefficient if the list is long enough, 0 otherwise.
    def __add__(self, other):
        length = max(len(self.coeffs), len(other.coeffs))
        result = []
        for i in range(length):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result.append(a + b)
        return Polynomial(result)

    # Q6 : term a_i x^i times term b_j x^j contributes a_i*b_j to the power i+j.
    # Start with a list of zeros and ACCUMULATE (+=) in it.
    def __mul__(self, other):
        if len(self.coeffs) == 0 or len(other.coeffs) == 0:
            return Polynomial([])

        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]
        return Polynomial(result)
