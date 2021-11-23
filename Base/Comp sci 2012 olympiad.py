#distinct prime factorisation
number = int(input("Input a single integer"))
factor = []
for count in range (1, 1000001):
    if number%count == 0:
        factor[count] = count
#next count 
#can the number be divided by a square number?
#while i is smaller than the square root of the number


