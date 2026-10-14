from src.vector import Vector2D

a = Vector2D(3, 4)
b = Vector2D(-1, 2)

print(a + b)
# a < b is True when a is shorter; so if b < a, a is the longer one
print(a if b < a else b)
print(a * 3)
