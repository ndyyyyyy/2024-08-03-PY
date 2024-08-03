# How to create a string(""" """ for mutiple lines).
stri = "I'm a programmer"
print(stri)

# How to acces characters of a string.
print("\n")
mystring = "Hello World"
print(mystring[6])
print(mystring[-2])

# How to acces a substring of a string.
print("\n")
print(mystring[0:5])
print(mystring[:7])
print(mystring[3:])
print(mystring[::3])
print(mystring[::-1])

# How to add two strings together.
print("\n")
greet = "Hello"
name = "Johán"
sen = greet + " " + name + "!"
print(sen)

# How to loop through a string.
print("\n")
for i in mystring:
    print(i)

# How to check a character/substring is inside of a string.
print("\n")
if 'e' in greet:
    print("Yes")
else:
    print("No") 

print("\n")
if "johé" in name:
    print("Yes")
else:
    print("No")

# Strip
print("\n")
mystring2 = "     Hello World     "
print(mystring2)
print(mystring2.strip())

# Uppercase and Lowercase.
print("\n")
mystring3 = "UpPeR lOwEr"
print(mystring3.upper())
print(mystring3.lower())

# How to check what a string starts or ends with.
print("\n")
mystring4 = "start and and end"
print(mystring4.startswith("s"))
print(mystring4.startswith("start und"))
print(mystring4.endswith("end"))


# How to find an index or a substring.
print("\n")
print(mystring4.find("n"))
print(mystring4.find("art"))

# How to count characters in a string.
print("\n")
print(mystring4.count("t"))
print(mystring4.count("a"))

# How to repalce an idex or a subtring.
print("\n")
strA = "Goodbye World Goodbye World"
print(strA.replace("World", "Universe"))
print(strA.replace("Goodbye", "Hello", 1))

# How to convert a string to a list and vice versa.
print("\n")
strB = "how are you doing"
my_list = strB.split(" ")
print(my_list)

print("\n")
new_string = " ".join(my_list)
print(new_string)

# The "%" formating method(oldest).
print("\n")
var = "Tom"
strC = "The variable is %s" %var
print(strC)

print("\n")
var1 = 45
strD = "The variable is %d" %var1
print(strD)

print("\n")
var2 = 2.7688675
strE = "The variable is %f" %var2
strF = "The varibale is %.3f" %var2
print(strE)
print(strF)

# The ".format()" formating method(older).
print("\n")
var3 = "Yoda"
str1 = "Not {} I am".format(var3)
print(str1)

print("\n")
var4 = 3.14159265358
str2 = "The variable was {}".format(var4)
str3 = "The variable was {:.4f}".format(var4)
print(str2)
print(str3)

print("\n")
var5 = "PI"
str4 = "The {} is the star of the infamous {}".format(var4, var5)
print(str4)

# The "f-string" formating method(best and most modern method).
print("\n")
variable1 = 4
variable2 = 5.899
string1 = f"The variable is {variable1*4} and {variable2}"
print(string1)