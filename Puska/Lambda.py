# How to create a lambda
add10 = lambda x: x + 10
print(add10(5))

# How to create a lambda with multiple argumnets.
print("\n")
mult = lambda x,y: x * y
print(mult(6, 3))

# How to sort iterates with lambda.
print("\n")
points2d = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2d_sotred = sorted(points2d)# Sorts by the "x".
print(points2d)
print(points2d_sotred)

print("\n")
points2d_sotred_ = sorted(points2d, key=lambda x: x[1])# Sorts by the "y".
print(points2d)
print(points2d_sotred_)

print("\n")
points2d_sotred_2 = sorted(points2d, key=lambda y: y[0] + y[1])# Sorts by the sum.
print(points2d)
print(points2d_sotred_2)

# The "map" function(transforms each elements with a function).
print("\n")
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
print(list(b))

# The "filter" function(filters each elements with a function, returns elements for which the function evaluates to True).
print("\n")
c = filter(lambda y: y%2 == 0, a)
print(list(c))

# The "reduce" function(repeatedly applies the function to the elements and returns a single value).
print("\n")
from functools import reduce
prod = reduce(lambda z,s: z*s, a)
print(prod)