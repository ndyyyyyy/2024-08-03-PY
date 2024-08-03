# How to create a dictionary.
mydict = {"continent": "Europe", "country": "Poland", "city": "Warsaw"}
print(mydict)

# How to create a dictionary differently.
mydict2 = dict(name = "Vladislav", age = 33, man = True, city = "Gdansk")

# How to access the elements in the dictionary.
print("\n")
print(mydict["country"])

print("\n")
print(mydict.get("city"))

# How to add/overwrite an element to the dictionary.
print("\n")
mydict2["drunkard"] = False
print(mydict2)
mydict2["drunkard"] = True
print(mydict2)

print("\n")
mydict.update({"region": "Central Poland"})
print(mydict)

# How to remove an element from the dictionary.
print("\n")
del mydict2["age"]
print(mydict2)

print("\n")
mydict2.pop("man")
print(mydict2)

print("\n")
mydict.popitem()
print(mydict)

# How to check if an element is in the dictionary.
print("\n")
if "name" in mydict2:
    print(mydict2["name"])
else:
    print("Error!")    

print("\n")
try:
    print(mydict["continent"])
except:
    print("Error!")

# How to loop through your dictionary.
print("\n")
for key in mydict2:
    print(key)

print("\n")
for keyy in mydict2.keys():
    print(keyy)

print("\n")
for value in mydict2.values():
    print(value)

print("\n")
for keys, values in mydict2.items():
    print(f"{keys}: {values}")

# How to copy your dictionary.
print("\n")
mydict_copy = mydict
print(mydict)
print(mydict_copy)

# !If you change the copy you also chnage the real dictionary itself beacuse of "mydict_copy = mydict"!
print("\n")
mydict_copy["email"] = "iamdrunkasfuck@ligma.com"
print(mydict)
print(mydict_copy)

# How to copy your dictionary like a pro(if you use this it will not change the original dictionary).
print("\n")
mydict3 = dict(name = "Jhon", age = 66, city = "London")
mydict_copy2 = mydict3.copy

# How to merge dictionaries.
yourdict = {"name":"Max", "age":18, "email":"max@xyz.com"}
yourdict2 = dict(name = "Conor", age = 26, city = "Detroid")
yourdict.update(yourdict2)
print(yourdict)

# This one merge two dictionaries but does not change the original ones.
print("\n")
x = {"a":1, "b":2}
y = {"b":8, "c":9}
z = x | y
print(z)
print(x)
print(y)

# Possible key types for dictionary.
print("\n")
hisdict = {3: 9, 4: 16, 8: 64}
print(hisdict)
print(hisdict[8])

# How to create a dictionary with tuples.
print("\n")
mytuple = ("8 + 7")
dictionary = {mytuple: 15}
print(dictionary)