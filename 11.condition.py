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
