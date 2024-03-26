def vat(rate,price):
    frate = ( rate / 100) * price
    return frate
 #   it gives us the answer that functions are self contained


def act_price():
    actvat = vat(18,20000)
    netprice = actvat +20000
    print(netprice)
act_price()


#afunction that wants to return avalue must return that value to any recuring function

#valuing when avoking afunction are the arguement
#return is the last statement they execute in afunctionreturn its  give back
# using parameter functions create three functions which share values. the last function should print out 
# the two should be dynamic
# the last on should receive value from function b which received 


#assignment "from then and now what are your learning takeaway with examples in code"


