# 1)	accept a number and display its table.

n=int(input("Enter Table number you want: "))
for i in range(1,11):
    print(f"{n} X {i} = {i*n}")