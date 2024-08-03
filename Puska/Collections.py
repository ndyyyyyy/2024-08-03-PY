# How to create a collection that stores it's values as a dictionary.
from collections import Counter
a = "aaaaaabbbbbccc"
print(Counter(a))
print(Counter(a).items())
print(Counter(a).keys())
print(Counter(a).values())
print(Counter(a).most_common(1)[0][0])# Mots common element.
print(list(Counter(a).elements()))# Can iterate over this.

# How to create a collection that stores it's values as tuple.
print("\n")
from collections import namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(3, -8)
print(pt)
print(pt.x, pt.y)

# How to create a ordered dictionary(same as a regular dictionary).
print("\n")
from collections import OrderedDict
ord_dict = OrderedDict()
ord_dict["b"] = 2
ord_dict["c"] = 3
ord_dict["d"] = 4
ord_dict["a"] = 1
print(ord_dict)

# How to create a defaultdictionary(it has a default value).
print("\n")
from collections import defaultdict
defa = defaultdict(int)# You can put float, string, list, boolen, tuple... values in it.
defa["a"] = 1
defa["b"] = 2
print(defa["a"])
print(defa["c"])

# How to create a deque(it is a double ended queue, can remove/add elements on both ends). 
print("\n")
from collections import deque
d = deque()

d.append("one")
d.append("two")
d.appendleft("three")
print(d)

d.pop()
print(d)

d.popleft()
print(d)

d.clear()
print(d)

d.extend([1, 2, 3])
print(d)

d.extendleft([5, 6, 7])
print(d)

d.rotate(1)
print(d)

d.rotate(-2)
print(d)