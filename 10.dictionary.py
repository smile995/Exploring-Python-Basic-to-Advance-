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
print(dicValue)