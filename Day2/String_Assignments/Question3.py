# 3) accept a string and display how many vowel characters are there inside it.


string = input("Enter a String :")
string=string.casefold()
# print(string)
count=0
for i in string:
    if i=='a' or i=='e' or i=='i' or i=='u'or i=='o':
        count+=1
print("Number of vowel characters in the string are ",count)