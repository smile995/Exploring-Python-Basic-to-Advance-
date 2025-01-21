# single line string
movie='The Gangstar,The Police' #using single quatation
# Multi line string
about= """Myself Amir Hamza Ismail,
I'm student of CCNUST,
Department of CSE,
Loved to explore new technology""" #Triple double quates
# print(about)

hobby='''Loved to watch islamic revulation seris or something,
In leisure, like to train my boddy to make fit,
Playing cricket and football ''' #Triple single quates
# print(hobby)

# string slicing
name= "Amir Hamza Ismail" #using double quatation
print(name[:8]) # result--> Amir Ham
print(name[2:8]) # result--> ir Ham
print(name[5:]) # result--> Hamza Ismail
# Converting at Uppercase
Capital_letter= name.upper() # all charecter converted to uppercase
small_letter= name.lower() # all charecter converted to lowercase
capitalized_letter=name.capitalize() # first letter of the word converted to uppercase
# print(Capital_letter,small_letter,capitalized_letter)

# split by condition 
example= "You are just looking like a wow"
result= example.split(" ") #result --> ['You', 'are', 'just', 'looking', 'like', 'a', 'wow']
# print(result)

# replace method on string
example2="Hello World"
result2= example2.replace("H", "G") #result -->"Gello World"
print(result2)
