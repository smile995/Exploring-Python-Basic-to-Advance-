# how to write tuple
tuple1 = ("apple", "banana", "cherry")
tuple3 = (True, False, False)


# how to access tuple
banana= tuple1[1]
cherry= tuple1[-1]
cherry= tuple1[2]

# update tuple items by following few step
# step -1: convert tuple to list
tuple2 = (1, 5, 7, 9, 3) #main tuple
convertToList=list(tuple2) #[1, 5, 7, 9, 3]
# step -2: append or remove something in list
convertToList.append(32)
convertToList.remove(1)
# again convert the list into tuple
AgainTuple2=tuple(convertToList)


# unpacked tuple : similer to destructure in javascript
fruits = ("apple", "banana", "cherry")
(red, *yellow) = fruits
print(red)
print(yellow)


# looping on tuple--> method-1: access the element by index
for fav in range(len(fruits)):
    print(fruits[fav])
# looping on tuple--> method-2: access the element list property
for fruit in fruits:
    print(fruit)
    
# how to join tuple
letter = ("a", "b" , "c")
number = (1, 2, 3)

tupleJoin = letter + number #('a', 'b', 'c', 1, 2, 3)
print(fruits*3)