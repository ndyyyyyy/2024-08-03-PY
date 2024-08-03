# How to create for loops.
a = "Okay"
for i in a:
    print(i)

for i in a:
    print(i, end=" ")

# How to loop through a list.
print("\n")
program = ["Java", "C++", "Python", "HTML", "Ruby"]
for i in program:
    print(i)

# It is better this way than in a for loop.
print("\n") 
list_num = [3, 56, 99, 21, 7, 103]
print(sum(list_num))
print(sum(list_num) / len(list_num))

# How to use "range()" in for loops.
print("\n")
for i in range(1, 11):
    print(i)

print("\n")
for i in range(1, 11, 2):
    print(i)

print("\n")
n = 6
for i in range(1, 11):
    mul = n*i
    print(n,"*",i,"=",mul)

print("\n")
for x in reversed(range(1, 11)):
    print(x)
print("Done!")        

print("\n")
list1 = ["Java", "C++", "Pearl", "Holy C", "Ruby"]
for i in range(len(list1)):
    print("Hello", list1[i])

# How to use nested for loops.
print("\n")
faang = ["Facebook", "Apple", "Amazon", "Netflix", "Google"]
for i in faang:
    print("Letters of",i,":")
    for letter in i:
        print(letter)

# For loops with else statement.
print("\n")
for i in range(1, 11, 3):
    print(i)
else:
    print("The loop has ended.")

# Break statement in for loops.
print("\n")  
for i in range(1, 11):
    if(i == 6):
        break
    print(i)

# Contunie statement in for loops.
print("\n")
for i in range(15, 21):
    if(i == 19):
        continue
    print(i)

# How to iterate over a dictionary.
print("\n")
ply_name = "Joshua"
goal = dict( Eddie = 9, Björn = 11, Joshua = 33)
for ply in goal:
    if ply == ply_name:
        print(goal[ply])
        break
else:
    print("No player available!")

# Better to use list comprehensions than for loops. 
print("\n")
num = [2, 5, 7, 4, 8, 6]
print([i**3 for i in num])

# How to create a pattern with for loops.
print("\n")
n = 9
for i in range(0, n):
    for j in range(0, i+1):
        print("*", end="")
    print()





#* While Loop
# How to create a while loop
print("\n")
b = 0
while b < 10:
    b = b + 1
    print(b, end="# ")

# How to use while loop.
print("\n")
count = 0
while count <= 5:
    print("True!!")
    count = count + 1
print("End!")

#* How to use the while loop with a not statement.
#print("\n")
#food = input("Enter a food(x to quit): ")
#while not food == "x":
#    print(f"You like {food}")
#    food = input("Enter another food(x to quit): ")
#print("Bye!")


#* How to use while loop with True.
#print("\n")
#while True:
#    print("Number: ")
#    num_ = int(input())
#    if num_ == 3:
#        break
#print("Correct!")


# How to find the LKKT with while loop.
print("\n")
x = 0
while True:
    x += 1
    if not(x % 4 or x % 7 or x % 9):
        break
print(x,"is the LKKT of 4, 7 and 9")

# The continue statement in while loops.
print("\n")
y = 0
while y < 5:
    y += 1
    if y == 3:
        continue
    print(y)

# While loops with else statement.
print("\n")
o = 1
while o < 5:
    print(o)
    o += 1
else:
    print("next number isn't less than 5")

# How to use pop function in while loops.
print("\n")
c = [1, 2, 3, 4, 5, 6]
while c:
    print(c.pop())
else:
    print("There are no elements left in the list.")

#* Calculating avarage of numbers with while loops.
#print("\n")
#num_1 = 0
#count_ = 0
#sum_ = 0
#amt = 0
#while num_1 >= 0 and amt != 3:
#    num_1 = int(input("Number: "))
#    amt += 1
#    if num_1 > 0:
#        count_ = count+1
#        sum_ = sum_ + num_1
#avg = sum_/count_
#print("The average is",avg)
       
       
#* While loops with random function.
#print("\n")
#import random
#r = random.randint(1, 100)
#print(r)
#guess = int(input("Number betwwen 1 and 100: "))
#while r != "guess":
#    if guess < r:
#        print("Too small number")
#        guess = int(input("Number betwwen 1 and 100: "))
#    elif guess > r:
#        print("Too big number")
#        guess = int(input("Number betwwen 1 and 100: "))
#    elif guess == r:
#        print("That's the number!")
#        break
#    else:
#       print("Ivalid input!")





#* Nested Loops.
# How to create a nested loop.
print("\n")
list_f = ["Apple", "Cherry", "Pear", "Blueberry", "Strawberry"]
for f in list_f:
    for i in f:
        print(i, end="_")
    print()

# How to pair all elements of a list with a nested loop.
print("\n")
list_c = ["Green", "White", "Black", "Red"]
list_i = ["Tree", "Snow", "Night", "Blood"]
for x in list_c:
    for y in list_i:
        print(x,y)

# How to draw a pattern with a nested loop. 
print("\n")
for i in range(18):
    for j in range(i):
        print("+", end=" ")
    print("")

print("\n")
v = 11
while(v > 0):
    h = 11
    while(h > v):
        print("-", end=" ")
        h = h - 1
    v = v - 1    
    print()

# How to append 2 lists with nested loops(also adds the elements together).
print("\n")
list2 = [10, 45, 30]
list3 = [90, 99, 88]
res = list()
for i in list2:
    for j in list3:
        res.append(i + j)
print(res)

# How to mutiply elements in 2 lists using nested loops.
print("\n")
list4 = [2, 4, 6, 10]
list5 = [3, 5, 7, 10]
for i in list4:
    for j in list5:
        if i == j:
            continue
        print(i, "*",j, "=",i*j)

# How to select specific elements using nested loops.
print("\n")
a_1 = 1
while a_1 <= 100:
    y_sum = 0

    for i in range(1, a_1):
        if a_1%i == 0:
            y_sum = y_sum + i
    if y_sum == a_1:
        print("Perfect number:",a_1)
    a_1 = a_1 + 1

# How to print elements mutiple times with nested loops.
print("\n")
fr = ["Niš", "Shköder"]
for h in fr:
    cout = 0
    while cout < 6:
        print(h, end=" ")
        cout = cout + 1       
    print()    