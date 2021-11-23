#initialise variable
n = 1
#get user to input an integer
x = int(input("Input an integer"))
#output the factors of the integer
print("The factors of ", x, "are: ")
while n <= x:
    #determine if counter is a factor of the integer
    if x%n == 0:
        print(n)
    #endif
    n=n+1
#endwhile



