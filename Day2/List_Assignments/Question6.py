# 6) accept 5 numbers, store them inside the list. now accept a position from user ,remove the element from that position and  after removing it, display the list.

list=[]
for i in range(1,6):
    print("Enter Number ", i, ": ",end='')
    num = int(input())
    list.append(num)
print(list)
pos = int(input("Enter the position of the number you want to delete : "))

list.remove(list[pos])
print(list)