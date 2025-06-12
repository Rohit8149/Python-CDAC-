# 3) Write a Python program to find the repeated items of a tuple.

t = (1, 2, 3, 4, 2, 3, 5, 1, 3)
newt=tuple()
for i in t:
    if t.count(i)>1 :
        isavailable=False
        for j in newt:
            if i==j:
                isavailable = True
        if not(isavailable):
            # newt=newt+(i,)
            newt=newt+tuple([i])
print(newt)