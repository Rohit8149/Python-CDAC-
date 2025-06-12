# 2) accept a string and display it. now accept slicing positions from and to , slice the string and display it.

string = input("Enter a String : ")
print(string)
print("To slice the string give the from and to positions")
print()
_from=int(input("Enter the position from which you have to slice : "))
_to=int(input("Enter the position to which you have to slice : "))
print(string[_from:(_to+1)])