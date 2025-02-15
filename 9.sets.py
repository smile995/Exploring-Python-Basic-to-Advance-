# method-1: to initialized of set
fruits_set={"apple","mango","banana","orange","litchi"}
mixed_property={"Hamza",True,False,1,0,"Amir"} #consider as same (True,1) and (False,0)
length_of_fruits= len(fruits_set) #result= 5


# method-2: to initialized of set
birds_set= set(("megpie","kingfisher","pegoen")) # note the double round-brackets
print(birds_set)

# how to access the property of set
newList=[]
for bird in birds_set:
    print(bird)
    if "k" in bird:
        newList.append(bird)
print(newList)