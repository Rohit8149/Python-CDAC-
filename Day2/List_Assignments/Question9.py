# 9) accept 5 names and store them in list. Now sort the list in ascending order display and then in descending order.

list=[]

print("Enter 5 Names")
for i in range(1,6):
    name= input(f"Name {i} : ")
    list.append(name)
list.sort()
print(list)
list.sort(reverse=True)
print(list)