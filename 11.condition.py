# just single condition example below
x = 10
if x > 5:
    print("x is greater than 5")

# Two condition example below
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# two or more condition example like below
z = 10
if z > 15:
    print("z is greater than 15")
elif z > 5:
    print("z is greater than 5 but less than or equal to 15")
else:
    print("z is less than or equal to 5")
    
# nasted conditional below
a = 10
b = 5
if a > 5:
    if b < 10:
        print("a is greater than 5 and b is less than 10")
# use all logical conditions like below
# Equals
a = 10
b = 20
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Not Equals
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# Less than
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# Less than or equal to
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is greater than b")

# Greater than
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Greater than or equal to
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is less than b")



age=25
# Ternary operators examples
name= "Amir Hamza ISmail" if age<30 else "Omar Faruk"
isEvenOrFalse= "Even" if age%2==0 else "Odd"
isAdult="Adult" if age>18 else "You are not Adult"
print(isAdult)