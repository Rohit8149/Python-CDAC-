# 4) accept a number,string,decimal,boolean value and a character from the user and store it inside the list. First print the list from the beginning and then from the end.

from decimal import Decimal

list=[]
x= int(input("Enter a number : "))
list.append(x)
x= input("Enter a string : ")
list.append(x)
x= Decimal(input("Enter a decimal : "))
list.append(x)
x= bool(input("Enter a boolean value : "))
list.append(x)
x= input("Enter a character : ")
list.append(x)

print(list)
print(list[::-1])