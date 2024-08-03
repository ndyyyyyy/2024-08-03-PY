# How to create a list.
mylist = ["banana", "cherry", "cheese", "apple"]
print(mylist)

# How to create an empty list.
mylist2 = list()

# What can you put in the list.
mylist3 = [5, True, "apple", "apple", False, 248, "cherry"]

# How can you recall what is inside the list.
print("\n")
print(mylist[0])
print(mylist[2])
print(mylist[-1])

# How to iterate over the list.
print("\n")
for i in mylist:
    print(i)

print([i for i in mylist])
# How can you check what is inside the list.
print("\n")
if "cheese" in mylist:
    print("Yes")
else:
    print("No")

print("\n")
if "lemon" in mylist:
    print("yes")
else:
    print("No")

# How to check an idex of an element in a list.
print("\n")
print(mylist.index("cherry"))
print(mylist.index("apple"))    

# How to check how long is the list.
len(mylist)

# How to add items inside the list.
print("\n")
mylist.append("kiwi")
print(mylist)

# How to insert a specific item into the list.
print("\n")
mylist.insert(2, "blueberry")
print(mylist)

# How to remove an item from the list.
print("\n")
item4 = mylist.pop(3)
print(item4)
print(mylist)

print("\n")
item5 = mylist.remove("cherry")
print(mylist)

# How to remove everything from the list.
mylist3.clear()

# How to reverse the list.
print("\n")
mylist.reverse()
print(mylist)

# How to sort the list.
print("\n")
mylist4 = [1, 11, -5, -89, 35, 1111, -1, 0]
print(mylist4)
mylist4.sort()
print(mylist4)

print("\n")
newlist = sorted(mylist)
print(mylist)
print(newlist)

# How to add 2 lists together.
print("\n")
mylist5 = [1] * 5
print(mylist5)

mylist6 = [0, 2, 3, 4, 5]

print(mylist5 + mylist6)

# How to add different iretables together.
print("\n")
a = [1, 2, 3]# A list
b = (4, 5, 6)# A tuple

print([*a, *b])

# How to specify/slice a part of the list.
print("\n")
yourlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(yourlist[1:6])
print(yourlist[2:])
print(yourlist[:8])
print(yourlist[::2])
print(yourlist[::-1])      

# How to copy the list.
hislist = ["BMW", "Mercedes", "Toyota", "Honda"]
list_copy = hislist.copy()




 
#*List comprehensions(a better alternative than for loops).
# How to create a list comprehension.
print("\n")
nums = [1, 2, 3]
nums_c = [i*2 for i in nums]
print(nums_c)

# List comprehension with integer.
print("\n")
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [f*f for f in c]
print(c)
print(d)

# List comprehension with strings.
print("\n")
str_1 = ["intro", "to", "list", "comps"]
results = [i.upper() for i in str_1]
print(results)

# List comprehension with "def".
print("\n")
def timesFive(num):
    return num*5

result = [timesFive(i) for i in c]
print(result)

print("\n")
def timesSix(nom):
    return nom*6

result_1 = [timesSix(i) for i in c if i > 5]
print(result_1)

# List comprehension with dictionaries.
print("\n")
dicts = [{"name": "Jerry"}, {"name": "Rick"}]
result_2 = [i["name"] for i in dicts]
print(result_2)

# How to create list comprehensions with if/else statement.
print("\n")
list1 = [1, 2, 3]
list1_ = [i*5 if i==3 else i for i in list1]
print(list1_)

list1__ = [i*5 if i==3 else i for i in list1 if i > 1]# !Same!
print(list1__)

# List comprehension with lambda.
print("\n")
lmb = map(lambda x: x*5, list1)
print(list(lmb))

lmb_ = map(lambda x: x*5 if x==3 else x, list1)
print(list(lmb_))

lmb__ = map(lambda i: i*5 if i==3 else i, filter(lambda i: i > 1, list1))# !Same!
print(list(lmb__))

# List comprehensions with multiple if statements.
print("\n")
el = [1, 2, 3, 4]
fr = ["cherry", "apple", "watermelon", "pear"]
list2 = [i for i in el if i > 1 if i != 3]
print(list2)

list2_ = [(i,f) for i in el if i > 1 for f in fr]
print(list2_)

print("\n")
list3 = [(i,f) for i in el if i > 1 if i != 3 for f in fr]
print(list3)

print("\n")
list3_ = [(i,f) for i in el if i > 1 if i != 3 for f in fr if f != "watermelon"]
print(list3_)

print("\n")
list3__ = [(i,f) for i in el if i > 1 if i != 3 for f in fr if f != "watermelon" and f != "apple"]
print(list3__)