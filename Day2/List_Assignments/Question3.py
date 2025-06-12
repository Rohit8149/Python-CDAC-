# 3) accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at the end of the list using "extend" method.
list=[]
for i in range(1,6):
    print("Enter Number ", i, ": ",end='')
    num = input()
    list.append(num)
print(list)
list.extend([100,200,300])
print(list)