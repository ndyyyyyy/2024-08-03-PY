# How to create a set.
myset = {1, 2, 3}
print(myset)

# !A set does not allow duplicates, and it is unordered!
print("\n")
myset1 = {2, 2, 3, 5, 5,}
myset01 = set("Hello")
print(myset1)
print(myset01)

# How to create a set differently(it is more preferable to create a set like this).
print("\n")
myset2 = set([9, 8, 7])

# How to add elements to a set.
print("\n")
myset2.add(1)
myset2.add(2)
myset2.add(3)
print(myset2)

# How to remove elements from a set.
print("\n")
myset2.remove(2)
print(myset2)

print("\n")
myset2.discard(8)
print(myset2)

print("\n")
print(myset2.pop())
print(myset2)

# How to remove everything from a set.
myset01.clear()

# How to iterate over a set.
print("\n")
for i in myset:
    print(i)

# How to check what is inside of a set.
print("\n")
if 9 in myset2:
    print("Yes")
else:
    print("No")

# How to calculate the union and intersection of two sets.
print("\n")
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

print(odds.union(evens))
print(odds.intersection(evens))
print(odds.intersection(primes))

# How to calculate the differences of two sets.
print("\n")
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

print(setA.difference(setB))
print(setA.symmetric_difference(setB))


# How to update a set.
setC = {1, 2, 3, 4, 5, 6}
setD = {5, 6, 7, 8, 9, 10, 11, 12}

setE = {5, 6, 11, 13, 14, 15, 16}
setF = {1, 2, 3, 14, 15, 17}

setG = {18, 19, 20, 10, 6, 7, 8}
setH = {7, 9, 19, 20, 21, 6}

print("\n")
myset2.update(myset)
print(myset2)

print("\n")
setC.intersection_update(setD)
print(setC)

print("\n")
setE.difference_update(setF)
print(setE)

print("\n")
setG.symmetric_difference_update(setH)
print(setG)

# Subsets(all the elements of our first set are in our second set).
print("\n")
setJ = {1, 2, 3, 4, 5, 6}
setK = {1, 2, 3}
setL = {7, 8}

print(setJ.issubset(setK))
print(setK.issubset(setJ))

# Supersets(all the elements of our first set contain all the elements from the second set).
print("\n")
print(setJ.issuperset(setK))
print(setK.issuperset(setJ))

# Isdisjoints(it returns True if there are no same elements in the sets).
print("\n")
print(setJ.isdisjoint(setK))
print(setJ.isdisjoint(setL))

# How to copy a set.
setM = {66, 77, 88, 99}
setN = setM.copy()

# Frozenset(cannot change it after it's creation).
print("\n")
print(frozenset([1, 2, 3, 4]))