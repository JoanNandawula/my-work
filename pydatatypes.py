#datatypes in python
#numeric
#string
#sequence
#mapping
#boolean
#set
#Numeric: we have integers(int),float(float) and complex numbers(complex)
#examples:
num1=10+3
print(num1, "is of atype", type( num1))

#strings
# astring is agroup of characters
name="joan" #or name='joan'
print(name,  "is of atype",type(name))
#semantics is the meanings of what you've written
#typecasting
numx="20"
print(numx,"is of atype", type(numx))
#example of typecasting
numy=int(numx)#conversion of the value of the numx into an integer and store it in numy
print(numy,"is of atype", type(numy))
numy=float(numx)
print(numy,"is of atype", type(numy))
numy=str(numx)
print(numy,"is of atype", type(numy))
#sequence data type
#under sequensce, we have lists, tuples, and range
#list is avariable that can store more more than one value.
#however we can have  an empty variable list and we can store values later on
mylist=[]
mylist.append("joan")
print(mylist)
mylist.append(15)
print(mylist)
#appennd is aspecilised command in python used to add value to alist

languages=["python","javascript","c","c++","swift","julia","ruby","cobol"]
print(languages[5])
print(languages[0])
print(languages[7])
print(languages[-1])

country=["uganda","kenya","tanzania",["egypt","somalia",["sudan"]]]
print(country[3][2][0])
print(country[-1][-1][-1])
person ={ "name":"joan", "age":6, "coutry":"uk"}
print(name)
student_id ={100, 200, 300, 400,500}

print(student_id)
print(student_id)