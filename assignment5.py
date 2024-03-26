#the packages and the modules so here packages are the ones we refer to folders
# and the modules are files of code inside to be reused
# when creating amodule you start by the two undrscore(__) and init then two underscore then .py 
#then create amodule(__init__.py)
# we looked at calling  amodule in another module that is you write astatement in acertain module  and then call it or print it  from another module
# we looked at  turtles when you first import it to amodule
# where we use the first call the turtle , detemine the pensize,its color,we do penup to cammand it start writing,we give it the digits tonrefer to
# then call the shape and after calling the assign it to avalue

#we learnt  about Object orientated programming which is the idea that advocates for developing software based on real world object
# the principles of object orientated programming that is polymophism,Inheritance,Abstraction and encapsulation
# aclass and its attributes like  an animal is the class and its attributes refer to the object of it
# like joan is the object and agirl is the class 
# the abstraction the ability to ignore all other items and concetrate on the highest levelthat is names of classes are always in singular class like river,house
# inheritance foristance sumsung is achild to asmartphone
#polymophism having the ability to take on adifferent form
# enpsulation  the ability to have what to share and what not to share
 # we've looked at  defining an object in python
 # we use the word class starting with the capital letter and ending with afullcolon
#afunction in the class is called amethod
# the objects in the class is called the behaviour
class Animal:
    color = ""
    size = ""
    sex = ""
    name = ""
    sound = ""
    species = ""
dog = Animal()
dog.name = "marks"
dog.size = "medium"
dog.color = "gold"
dog.sex = "male"
dog.species = "junkie"
dog.sound = "barks"
dog.age = 17
#accessing objects by printing them
print(f"{dog.name} is {dog.age} years old")
print(dog.name + " does " + dog.sound)
print(f" {dog.name} is {dog.size} size")
print (dog.name  +  " is " + " color " + dog.color)


 