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