# How to raise an exception.
#x = -5
#if x < 0:
#    raise Exception("x should be positive")


# How to make an assertion error.
#y = -6
#assert (y >= 0), "x is not positive"


# How to find errors.
try:
    a = 5 / 0
except:
    print("An error happened!")    

print("\n")
try:
    b = 7 / 0
except Exception as i:
    print(i)

print("\n")
try:
    c = 4 / 1
    d = 3 + "20"
except ZeroDivisionError as q:
    print(q)
except TypeError as r:
    print(r)    

print("\n")
try:
    e = 9 / 1
    f = 3 + 20
except ZeroDivisionError as p:
    print(p)
except TypeError as o:
    print(o)
else:
    print("Everything is fine.")
finally:
    print("Cleaning up...")# This clause is always running.         


# How to raise your own exceptions.
print("\n")
class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("The value is too high!")
    if x < 100:
        raise ValueTooLowError("The value is too low!", x)
    


try:
    test_value(5)
except ValueTooHighError as t:
    print(t)
except ValueTooLowError as k:
    print(k.message, k.value)            