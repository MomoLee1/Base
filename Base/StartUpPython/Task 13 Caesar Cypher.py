#user inputs string
sentence = input("Type in a sentence").upper()
#user inputs shift
shift = int(input("What is your shift?"))
#initialise empty list
cipheredmessage=""
#loop for every character in string
for ch in sentence:
    #cipher
    if ch == " ":
         cipheredmessage+= ch
    else:
        cipheredmessage+= chr(ord(ch) + shift) 
#end for
#output ciphered message
print(cipheredmessage.lower())
