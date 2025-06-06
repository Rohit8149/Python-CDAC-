#9) display fibonicii series of 10 numbers

n_minus_2=0
n_minus_1=1
n=0
print(n_minus_2,end=' ')
print(n_minus_1,end=' ')

for i in range(1,11):
    n=n_minus_2+n_minus_1
    print(n,end=' ')

    n_minus_2=n_minus_1
    n_minus_1=n