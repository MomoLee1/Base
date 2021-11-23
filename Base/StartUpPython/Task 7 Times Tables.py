#initialise variable
i = 1
#get user to input number between 1-10
number = float(input("Input a number between 1-10"))
if number > 0 and number < 11:
#output first 10 values of the times table of "number"
    while i < 11:
        print(number*i)
        i = i + 1 
    #endwhile
#endif

