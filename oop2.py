#defining an object in python.
# we use the word class starting with the capital letter and ending with afullcolon

class Animal:
    color = ""
    size = ""
    sex = ""
    name = ""
    sound = ""
    species = ""
    age = 0
    def feed(self):
        print("the animal feeds by chewing")
       return "by chewing"
 # creating objects of the class Animal
 # afunction in the class is called amethod
 # the objects in the class is called the behaviour
cat = Animal()
cat.name = "hugo"
cat.size = "medium"
cat.color = "gold"
cat.sex = "male"
cat.species = "felime"
cat.sound = "meow"
cat.age = 17
#accessing objects by printing them
print(f"{cat.name} is {cat.age} years old")
print(cat.name + " does " + cat.sound)
print(f" {cat.name} is {cat.size} size")
print (cat.name  +  " is " + " color " + cat.color)
print(f"{cat.feed()}")