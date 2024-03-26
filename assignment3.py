#looping refers to the process of executing ablock of repeatedly
# there are different types of loops that is the 
#the for loop

numbers = [2,4,6,8,10]
for i in numbers:
    print(i)  
#the while loop repeatedly executes ablock of code as long as specified condition is true

count = 1
while count < 5:
    print(count)
    count += 1

#if loop is for writing programs that make decisions based on different conditions
x = 10
if x > 5:
    print("x is greater than 5")
    

# the functions are blocks of reusable code that performs aspecific task
# to define afunction in python you use the 'def'followed by the function name and the parentheses 
# there two types of functions that is static and dynamic function
# static function these are parentheses without the parameter

def static():
    num1,num2 = 20,40
    print(num1+num2)
static()

# dynamic function these are parentheses with parameters
def add(num1,num2):
    sum = num1+num2
    print(sum)
add(30,40)
#the packages and the modules so here packages are the ones we refer to folders
# and the modules are files within code inside to be reused
# when creating amodule you start by the two undrscore(__) and init then two underscore then .py 
#then create amodule(__init__.py)


  














 # is ablock of code that performs aspecific task and can be reused through the programme
 #To define afunction in python you use 'def' and followed by the function name