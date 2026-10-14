from src.polynomial import Polynomial

p = Polynomial([1, 2, 3])
q = Polynomial([4, 5])
print(p + q)
print(p * q)
print(p.degree())
print(p.evaluate(2))
