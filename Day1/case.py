# 8) accept a character and display whether it is upper case or lower case or not an alphabet.
char = input('Enter A Character')
UpperCase = char.upper()
LowerCase = char.lower()

if char==UpperCase:
    print("It is a Upper Case")
elif char==LowerCase:
    print("It is a Lower Case")
