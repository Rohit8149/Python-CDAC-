"""
7) A pangram is a sentence that contains all the alphabets.
example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""
string= input("enter a String")
string=string.casefold()
print(string)
ispangram=True
for i in range(97,123):
    if not(chr(i) in string):
        ispangram=False
        break
if ispangram:
    print("It is a pangram")
else:
    print("It is not a pangram")