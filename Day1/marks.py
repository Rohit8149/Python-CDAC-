# 5)	accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.

eng = int(input("Enter Your English Marks : "))
mat = int(input("Enter Your Maths Marks : "))
sci = int(input("Enter Your Science Marks : "))

sum = eng + mat + sci
percent=sum/3
print("percent : ",percent)

if not(eng>=35 and mat>=35 and sci>=35):
    print("Fail")
elif 100>=percent>=75:
    print("Distinction")
elif 75>percent>=60:
    print("First Class")
elif 60>percent>=50:
    print("Second Class ")
else:
    print("Pass")