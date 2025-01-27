# Mission is complete basic python in a day
# name= input("Enter your name here: ")
# age= input("Enter your age: ")
# message= f"Mr.{name} you are {age} year old now"
# print(message)

weight= input("Weight: ")
weight_in_num= float(weight)
wish= input("Gram (g) or pound(p): ")
wish_in_lower= wish.lower()
if wish_in_lower=="g":
    print("Weight in gram: ",weight_in_num*1000)
elif wish_in_lower=="p":
    print("Weight in pound: ", weight_in_num*2.20462)
else:
    print("you are a cowboy")
