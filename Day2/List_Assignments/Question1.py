"""
1) create a list , accept a number,name and a float value from user and store it inside the list.

now accept one more name from user and insert it at 2nd position.

accept a number and append it at the end of the list.
print the entire list.
"""

list=[]

number = int(input("Enter A Number"))
name = input("Enter A Name")
float = input("Enter A Float Value")

list.append(number)
list.append(name)
list.append(float)
print(list)

name2 = input("Enter a Name")
list.insert(2,name2)
print(list)

number2 = int(input("Enter a Number "))
list.append(number2)
print(list)