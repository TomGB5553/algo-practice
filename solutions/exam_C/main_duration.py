# Exercise 1, Q7
from src.duration import Duration

a = Duration(1, 45)
b = Duration(0, 50)
print(a + b)
print(a if a < b else b)      # the SHORTER one: a < b is True when a is shorter
print(a * 3)
