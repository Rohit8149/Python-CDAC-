# 5) accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove from the list and  after removing it, display the list.
list=[]
for i in range(1,6):
    print("Enter Number ", i, ": ",end='')
    num = int(input())
    list.append(num)
print(list)
num = int(input("Enter the number you want to delete : "))

list.remove(num)
print(list)