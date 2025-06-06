# 7) accept numbers till user enters 0 and display the total of all the numbers entered.
total = 0

while 1:
    num =int(input("Enter A Number"))
    total=total + num
    if num==0:
        break
print(total)