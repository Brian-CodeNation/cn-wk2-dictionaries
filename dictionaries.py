# This is the work done on Python Dictionaries

animals = {
    "Lion" : "Cub",
    "Horse" : "Foal",
    "Cat" : "Kitten",
    "Dog" : "Puppy",
    "Cow" : "Calf",
}

#The get method returns the value of a key
print(animals.get("Dog"))

print(animals.get("TRex", "Nope - can't this one"))

