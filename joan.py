#The result is that the string 'python is fun' is assigned to the  variable some_string. However, if you want to see the output, you need to  print the variable some_string
some_string = 'Python is fun' 
# This code assigns values 5, 3.2, and 'Hello' respectively to variables a, b,andc. Then it prints out the values of these variable: 

a, b, c = 5, 3.2, 'Hello'

print(a)  #  displays 5
print(b)  #  displays 3.2
print(c)  # displays Hello

#It means that you are assigning the value'5' to avariale named 'num1'
num1 = 5
#here it will display the value of num1  followed by the string 'is of atype' and then the type of the variable eg 5 is of type <class 'int' >
print(num1, 'is of type', type(num1))
#the variable 'num2' will hold the value'2.0' which is a floating-point number
num2 = 2.0
#This line prints information about the variable'num2'which consist  of three parts ie 'num2'this is a variable ,'is of type' this indicates what follows is a type of avariable,'type(num2) this determines the type of the variable using type()
print(num2, 'is of type', type(num2))
#It means that num3 holds the value of the complex number 1+2j where 1 is the real number 2j indicates that the imaginary part is 2 times the imaginary unit which is donated by j
num3 = 1+2j
#This indicates that num3 holds a complex number with a real part of 1 and an imaginary part of 2 and its <class 'complex'> as returned by the type() function
print(num3, 'is of type', type(num3))
#languages is a variable that holds a list of strings representing programming languages and you can access elements of these lists by indexing suchas language[0]
languages = ["Swift", "Java", "Python"]

# is a python statement that prints the first element of the languages lists to console
print(languages[0])   # Swift

# is a python statement that prints the third element of the languages list to console
print(languages[2])   # Python

# this statament that creates a tuple named product with two strings and one floating-point number
product = ('Microsoft', 'Xbox', 499.99)

# Is a python statement that displays the first element of the product tuple to the console which is microsoft
print(product[0])   # Microsoft

# is a python statement that displays the second element of the product tuple to console which is xbox
print(product[1])   # Xbox


#is a python statement that creates a dictionary named capital_city with curly braces
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
#Is a python statement that  prints the entire capital_city dictionary to console
print(capital_city)


# Is a python statement that creates a  set named 'student_id' using the curly braces
student_id = {112, 114, 116, 118, 115}

# Is a python statement that displays the entire student_id set to the console containing unique features
print(student_id)

#Is a python statement that displays the type of the variable student_id to the console which is aset acollection of unique eements 
print(type(student_id))

# Is a python statement that creates a list named fruits that holds a list with three elements
fruits = ["apple", "mango", "orange"] 
#Is a python statement that displays the entire fruits list to the console
print(fruits)

# is a python statement that creates atuple named numbers
numbers = (1, 2, 3) 
#tuple is straight forward you can use it to print() function to display the content ie(1,2,3)
print(numbers)

# Is apython statement that creates a dictionary named alphabets
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
#it displays the key-values pairs of the dictionary.
print(alphabets)

#these are the elements of the set
vowels = {'a', 'e', 'i' , 'o', 'u'} 
#It displays the elements of the set enclosed withinthe curly brackets
print(vowels) 


# it creates a set in python containing unique elements of the set
student_id = {112, 114, 116, 118, 115}

# Displays the elements of the set enclosed within curly braces separated by commas
print(student_id)

# its used to determine the data type of a given variable which is aset
print(type(student_id))
# creates a tuple representing information about the product
product = ('Microsoft', 'Xbox', 499.99)

#here it will output the first element of the tuple
print(product[0])   # Microsoft

#here it outputs the second element of the tuple 
print(product[1])   # Xbox




#here its assigning values to variables respectively
a = 7
b = 2

# displays the sum of the variables 'a' and 'b' along with the text 'sum'
print ('Sum: ', a + b)  

#displays the result of subtracting the value of variable 'b' from the value of the variable 'a' 
print ('Subtraction: ', a - b)   

# here displays the result of multiplying the value of the variable a by the value of te varible b
print ('Multiplication: ', a * b)  

# here it displays the result of dividing the value of the variable a by the value of the variable b along with the text division
print ('Division: ', a / b) 

# displays the result of the performing floor division     on the value of the variable a divided by the value of the varable b along with the text 'floor division"anwers is 3"
print ('Floor Division: ', a // b)

# the modulo operation returns the remainder of the division of a by b in case 7 divided by 2 results in 3 with remainder of 1 so the modulo operation returns 1
print ('Modulo: ', a % b)  

# In python the ** operator is used for exponentiation. it raises the left operand to the power of the  power of the right operand so 7** 2 is equal to 49
print ('Power: ', a ** b)   


# Here you've assigned the value 10 to the variable a with the statement a = 10
a = 10

# here you've assigned the value of 5 to avariable b
b = 5 

# this can equivalent to a=a+b this atatement adds the value of b to the current value of a
a += b      #15
print(a)
# Output: 15


# The == operator is a comparison used to check if two values are equal . in  this case a is 15 and b is 5 so a==b avaluates to false because 15 is not equal to 5
print('a == b =', a == b)

# The != operator is acomparison operator used to check if  two values are not equal in this case a is 15 and b is 5 so a !=b evaluates to True because 15 is not equal to 5
print('a != b =', a != b)

# The > operator os acomparison operator used to check if the value on the left side(in this case a) is greater than the value on the right side(in this case b ) since 15 is indeed greater than 5 the comparison a > b evaluates true
print('a > b =', a > b)

# Thats false
print('a < b =', a < b)

# This true because a is greater than b
print('a >= b =', a >= b)

# Thats false
print('a <= b =', a <= b)
#Its false for and all operators must be true
print((a > 2) and (b >= 6)) 

#   This code evaluates the logical expression True and True and prints the result which is True
print(True and True)     # True
print(True and False)    # False

# logical OR this code evaluates the logical expression True or False and prints the result True
print(True or False)     # True

# 
print(not True)          # False

#the variables x1, x2, x3, are equal to the variables y1,y2 and y3 respectively due to their assigned values and the rules of comparision in python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# this code evaluates the expression x1 is not y1 and displays the result false
print(x1 is not y1)  # false
#This code evaluates the expression x2 is y2 and displays the result which is True
print(x2 is y2)  # True
#In case x3 and y3 refer to different list object even though tey have the same content it evaluates false
print(x3 is y3)  # False
#python creates a string object to represent the value 'Hello world' and the variable message holds areference to that string object in memory
message = 'Hello world'
#dictionaries in python are unordered collections of items where each item consists of key-value pair. key-value pair. keys must be unique and immutable while values can be of datatype
dict1 = {1:'a', 2:'b'}
# this indicates that H is present in the string
print('H' in message)  # True

# looks whether hello is not present in the atring stored in the variable
print('hello' not in message)  # True

# checks whether 1 is present
print(1 in dict1)  # True 

# checks whether a is present in the dict
print('a' in dict1)  # False

