# How to create a tuple.
mytuple = ("stream", 99, "river", "lake", "ocean", 420)
print(mytuple)

# How to create a tuple from a iterable(exp.:list).
mytuple2 = tuple(["stream", 99, "river"])

# How can you recall what is inside the tuple.
print("\n")
print(mytuple[5])
print(mytuple[-4])

# How to iterate over the tuple.
print("\n")
for y in mytuple:
    print(y)

# How can you check what is inside the tuple.
print("\n")
if "lake" in mytuple:
    print("Yes")
else:
    print("No")

# How to check how long is the tuple.
len(mytuple)

# How to count things inside the tuple.
print("\n")
mytuple3 = ("a", "p", "p", "l", "e", "p", "i", "e")
print(mytuple3.count("p"))

# How can you chek the index of an item inside the tuple.
print("\n")
print(mytuple3.index("p"))
print(mytuple3.index("i"))
print(mytuple3.index("e"))

# How to convert a tuple to a list and vice versa.
print("\n")
list_1 = list(mytuple)
print(list_1)
tuple_1 = tuple(list_1)
print(tuple_1)

# How to specify/slice a part of the tuple.
print("\n")
k = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(k[5:9])
print(k[:4])
print(k[8:])
print(k[::3])
print(k[::-2])

# How to unpack the elements from the tuple.
print("\n")
mytuple4 = ("Ricsi", 20, "Putnok")
name, age, city = mytuple4
print(name, age, city)

# How to unpack mutiple elements from the tuple.
print("\n")
yourtuple = (0, 1, 2, 3, 4)
q1, *q2, q3 = yourtuple
print(q1)
print(q2)
print(q3)

#* Tuples can be efficient when working with large data.
# A list is larger then a tuple even when it has the same elements.  
print("\n")
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# Working with tuple is faster than working with lists.
print("\n")
import timeit
print(timeit.timeit(stmt = "[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt = "(0, 1, 2, 3, 4, 5)", number=1000000))