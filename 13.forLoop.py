# how initialized the for loop in an array
fruits=["mango","banana","litchi","apple","orange"]
for fruit in fruits:
    if fruit=="banana":
        print(fruit)
        if "a" in fruit:
            print("vowel")
        continue
    
# how to loop in a string
name="Amir Hamza Ismail"
for letter in name:
    if letter=="i":
        print("break")
        break
        
# how to use  range (initial value, end value, increment value)
for number in range(15):
    print(number)