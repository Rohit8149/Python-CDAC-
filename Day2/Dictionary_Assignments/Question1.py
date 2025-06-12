# 1) accept 5 students name and store them in the dictionary by providing keys from 1 to 5 respectively.

mydict={}

for i in range(1,6):
    name = input(f"Enter Name {i} : ")
    mydict.update({i:name})

print(mydict)
    