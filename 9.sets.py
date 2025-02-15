# method-1: to initialized of set
fruits_set={"apple","mango","banana","orange","litchi"}
mixed_property={"Hamza",True,False,1,0,"Amir"} #consider as same (True,1) and (False,0)
length_of_fruits= len(fruits_set) #result= 5


# method-2: to initialized of set
birds_set= set(("megpie","kingfisher","pegoen")) # note the double round-brackets
# print(birds_set)

# how to access the property of set
newList=[]
for bird in birds_set:
    if "k" in bird:
        newList.append(bird)
# print(newList)

isExist= "banana"  in fruits_set # true
isExist= "banana" not in fruits_set # false

# how to add something in set
birds_set.add("Swan") #add swan in the birds_set using add method that to add one property
vegitable={"tomato","onion","potato"}
newVegitable={"bean","carrot","little finger"}
vegitable.update(newVegitable) #update allow to add multiple property

fruits = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

fruits.update(mylist)


# how to remove something from a set
movies= {"KGF","Salar","Pathan","Pushpa","King"}
movies.remove("King") #if property exist then it work either throw an error
movies.discard("KGF") #if property exist then it work either not work (no error)
names=set(("Amir","Hamza","Ismail","Saim","Shanto","Anamul"))
names.pop() #it remove random property from a set. we never now which will be remove


# how to join multiple set together
letter = {"a", "b", "c"}
letNum = {1, "a", 3}
setUnion1= letter.union(letNum) #method 1 to concanate sets that allow to concanete multiple set
setUnion2= letter | letNum #method 2 to concanate sets that allow to concanete one set only

intersectionMethod1 = letter.intersection(letNum) #method 1 to intersected with each other
intersectionMethod2 = letter & letNum  #method 2 to intersected with each other

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple","blueberry"}
set1.intersection_update(set2) #this method chnage the original set
setDifference=set1.difference(set2) #method 1 to knowing about difference between two set
setDifference=set1 - set2 #method 2 to knowing about difference between two set
set3= set1.symmetric_difference(set2)
print(set3)


# <------- all method are below -------->

# add()	                	Adds an element to the set
# clear()	 	            Removes all the elements from the set
# copy()	            	Returns a copy of the set
# difference()  	        Returns a set containing the difference between two or more sets
# difference_update()   	Removes the items in this set that are also included in another, specified set
# discard()	               	Remove the specified item
# intersection()	    	Returns a set, that is the intersection of two other sets
# intersection_update() 	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	        Returns whether two sets have a intersection or not
# issubset()	            Returns whether another set contains this set or not
#  	<	                    Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	        Returns whether this set contains another set or not
#  	>	                    Returns whether all items in other, specified set(s) is present in this set
# pop()	 	                Removes an element from the set
# remove()	 	            Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
