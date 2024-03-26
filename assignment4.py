
def myinfo(name,age,email,gender):
    name =input("enter your name here:")
    age =int(input('enter your age here:'))
    email =input("enter your email here:")
    gender =input("enter your gender here:")
    print(name,age,email,gender)
myinfo("name","age","email","gender")



def payement1(jpaye,nssf,salary):
    paye = (jpaye/100) * salary
    mnssf = (nssf/100) * salary
    netpay = salary - (paye + mnssf)
    print("Your actual salary is:",netpay)

jpaye = int(input("please enter paye percentage:"))
nssf = int(input("please enter nssf percentage:"))
salary = int(input("please enter gross salary:"))

payement1(jpaye,nssf,salary)
