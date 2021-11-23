#get user to input integer
number = int(input("Input an integer between 100 and 999"))
hundreds = number//100
tens = (number - (number//100)*100)//10
units =(number - (number//100)*100) - ((number - (number//100)*100)//10)*10
#output results
print (hundreds, " hundreds", tens, " tens", units, " units" )


## ACS - You seem to be misisng some comments!