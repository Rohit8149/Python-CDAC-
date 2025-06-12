# 4) accept a string and display the characters which are repeated in the string

string = input("Enter the string")
myset=set()
for i in string:
    if string.count(i)>1:
        myset.add(i)
print(myset)
