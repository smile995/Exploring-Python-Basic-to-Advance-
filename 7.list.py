fruits=["Mango","Banana", "Apple", "Pine-apple","Orange","Kiwi","Grapes"]
# list property access by index
mango=fruits[0]
banana=fruits[1]
grape= fruits[-1] # Grapes ===> negetive value means start from last
mango_to_orange= fruits[:5]
apple_to_last= fruits[2:]
# print(apple_to_last)
# Changing list property
fruits[0]="tomato" #mango change tomato
# Append as child (push)
fruits.append("Black-berry") # append method add a item in an list at last index
fruits.insert(3, "Litchi") # insert method add a item in selected index


# Removing property from list
fruits.remove("Kiwi") #Kiwi is removed from list
fruits.pop(2) #remove by index. apple will be remove

# deleting property completely from list
thislist = ["apple", "banana", "cherry"]
print(thislist.clear()) #clear() make empty a list 

# for fruit in fruits:
#     print(fruit)

# for fruit in range(len(fruits)):
#     print(fruit)


movies= ["Vemon","Spiderman", "Ironman","Driver"]
newList=[]
for movie in movies:
    if "r" in movie:
        newList.append(movie)

# print(newList)
numbers=[3,43,534,545,435,34,5,45,5,345,4,54,5,5,4]
numbers.sort() #sorting in ascending order
# print("sorting in accending order",numbers)
numbers.sort(reverse=True)  #sorting in decending order
# print("sorting in decending order",numbers)
mainArray=["Shanto","Badaima", "Saim","Majnu","Anamul","Pera"]
copyArray= mainArray[:] #medhod-1: to copy an array
copyArray= mainArray[:]#method-2: to copy an array
# print(copyArray)

joinArray= movies+mainArray #Way to join array
print(joinArray)