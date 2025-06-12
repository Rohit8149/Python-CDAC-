# 1) accept a string and display whether it is palindrome or not.

string = input("Enter a String to check palindrome")

rev_string=string[::-1]

if(string==rev_string):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
