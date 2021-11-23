#Ask for input
x = input("time:")
#split
list = x.split(":")
#output number of seconds
print (int(list[0])*3600+int(list[1])*60 + int(list[2]), "seconds")