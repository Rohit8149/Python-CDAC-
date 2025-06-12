# 2) first create list empty. accept numbers till user enters 0 and store them inside the list.
# Print the list and its length.

list=[]

while 1:
    print("Enter The numbers want ot add in list")
    print("Enter 0 to Stop")
    num = input("num : ")
    if num=='0':
        break
    else:
        list.append(num)
print(list)
print("length of list : ",len(list))
