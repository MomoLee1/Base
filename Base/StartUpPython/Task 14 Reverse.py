#get user to input string
word = input("Input any word")
#calculate the length of the string
stringlength = len(word)
#slice
reverseofword = word[stringlength::-1]
#output reverse of string
print(reverseofword)

#do it again in pseudocode
for count = stringlength-1 to 0 step -1
    reverse = reverse + word[count]
next
