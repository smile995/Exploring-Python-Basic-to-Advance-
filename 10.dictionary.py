# how to initailized the dictionary in python
# Dictionaries are used to store data values in key:value pairs.(similar to object in javascripy)

car = { #method:1
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":"sky blue",
  "price":1200
}
phone=dict(name="iphone",price=347678,color="red") #method:2
# how to access dictionary property
brand=car.get("brand") #method:1
model=car["model"] #method:1
dicKey= car.keys() #keys() function give you all the keys of a dictionary
dicValue=car.values() #values() function give you all the valus of a dictionary
getKeyValue= car.items() #return key and value as tuple
# how change,add,remove,delete and update the value of property
car["color"]="red" #now  color change  sku-blue to red
car.update({"price":343545}) #now  price  update  1200 to 343545
car.update({"owner":"Amir Hamza Ismail"}) #added a new property and owner
removeWithPop= car.pop("year") #pop help to remove specific things
removeWithPopItem= car.popitem() #popitem() help to remove the last property
del car["brand"] #del function help to delete specific property and full dictionary
car.clear() #clear () make the dictionary empty


my_info = {
    "name": "Amir Hamza Ismail",
    "role": "MERN Stack Developer",
    "skills": ["React", "Node.js", "Express", "MongoDB", "Next.js"],
    "location": "Bangladesh",
    "experience": 2,
    "available_for_remote": True
}

# looping in the dictionary
for property in my_info:
    allKey=(property) #provide only keys
    allVlaie=(my_info[property]) #provide only values

# another way to get the value
for value in my_info.values():
    getValueHere=value
# another way to get the keys
for key in my_info.keys():
    getKeyHere=key
# how to get the key and value as pair by looping
for KV in my_info.items():
    keyValurPair= KV

# how to copy a dictionary
new_my_info1= my_info.copy() # method 1: here my_info and new_my_info is same
new_my_info2= dict(my_info) # method 2: here my_info and new_my_info is same


# how to make nasted dictionary
developer_profile = {
    "name": "Amir Hamza Ismail",
    "contact": {
        "email": "amirhamza@example.com",
        "linkedin": "linkedin.com/in/amir-hamza-ismail",
        "github": "github.com/amir-hamza-ismail"
    },
    "skills": {
        "frontend": ["React", "Next.js", "HTML", "CSS", "Tailwind CSS"],
        "backend": ["Node.js", "Express.js"],
        "database": ["MongoDB", "PostgreSQL"],
        "tools": ["Git", "Postman", "Figma"]
    },
    "projects": {
        "hospital_management_system": {
            "tech_stack": ["Next.js", "Tailwind CSS", "MongoDB"],
            "description": "A complete hospital management system with doctor and patient management features."
        },
        "restaurant_admin_panel": {
            "tech_stack": ["React", "Express.js", "MongoDB"],
            "description": "An admin panel to manage restaurant orders, reservations, and user communications."
        }
    },
    "availability": {
        "remote": True,
        "freelance": True,
        "full_time": True
    }
}

skilss=developer_profile["skills"]["frontend"]
email= developer_profile["contact"]["email"]


# clear()       	Removes all the elements from the dictionary
# copy()	        Returns a copy of the dictionary
# fromkeys()       	Returns a dictionary with the specified keys and value
# get()         	Returns the value of the specified key
# items()	        Returns a list containing a tuple for each key value pair
# keys()	        Returns a list containing the dictionary's keys
# pop()	            Removes the element with the specified key
# popitem()	        Removes the last inserted key-value pair
# update()	        Updates the dictionary with the specified key-value pairs
# values()	        Returns a list of all the values in the dictionary