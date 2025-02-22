# In Python a function is defined using the def keyword:
# call the function that it's can executes
def my_function():
     print("amir hamza ismail")

# my_function()


# define function with argument
def printName(name):
     print("Your name is :",name)

# printName("amir hamza ismail")


# making a function that can add two numbers
def summation(x,y):
     sum= x+y
     print(sum)

# summation(3,5)
# summation function take two agruments. if you not pass the argument then you face error

# _____________________________________________________________________
# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def sum_calculator(*number):
     sum=0
     for x in number:
          sum=sum+x
     print(sum)

# sum_calculator(2,3,4,4,5,6,7,8,8)
# _____________________________________________
# Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print("calling itself")
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
# tri_recursion(6)


def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case

print(factorial(8))  # Output: 120