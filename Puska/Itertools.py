# The "product" itertool.
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

c = [1, 2]
d = [3]
prod1 = product(c, d, repeat=2)
print(list(prod1))

# The "permutations" itertool(returns all the posible order of an input).
print("\n")
from itertools import permutations
e = [7, 8, 9]
perm = permutations(e)
print(list(perm))
perm1 = permutations(e, 2)
print(list(perm1))

# The "combinations" itertool(make all possible combinations whith a !specified length!).
print("\n")
from itertools import combinations
f = [1, 2, 3, 4]
comb = combinations(f, 3)
print(list(comb))

print("\n")
from itertools import combinations_with_replacement
comb_wr = combinations_with_replacement(f, 2)
print(list(comb_wr))

# The "accumulate" itertool(returns a accumulated sum).
print("\n")
from itertools import accumulate
g = [1, 2, 3, 4]
acc = accumulate(g)
print(g)
print(list(acc))

print("\n")
import operator
acc_o = accumulate(g, func=operator.mul)
print(g)
print(list(acc_o))

print("\n")
h = [1, 2, 5, 3, 4, 8, 7]
acc_m = accumulate(h, func=max)
print(h)
print(list(acc_m))

# The "groupby" itertool(makes an iterator that returns keys and groups from another iterable).
print("\n")
from itertools import groupby
def smaller_than_3(x):
    return x < 3

j = [1, 2, 3, 4, 5]
group_obj = groupby(j, key=smaller_than_3)# group_obj = grouby(j, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))

print("\n")
persons = [{"name": "Tim", "age": 25}, {"name": "Jerry", "age": 25}, {"name": "Rick", "age": 27}, 
           {"name": "Summer", "age": 28},]

group_obj1 = groupby(persons, key=lambda y: y["age"])
for key, valuee in group_obj1:
    print(key, list(valuee))

# The "infinite iterator" itertools.
print("\n")
from itertools import count
for i in count(2):
    print(i)
    if i == 22:
        break

print("\n")
from itertools import cycle
ß = [4, 5, 6]
for q in cycle(ß):
    print(q)
    if q == 6:
        break

print("\n")
from itertools import repeat
ä = [1, 2, 3]
for p in repeat(2, 11):
    print(p)