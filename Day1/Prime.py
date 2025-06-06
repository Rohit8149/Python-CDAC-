from traceback import print_exc

for i in range(3,31):
    isprime=True
    for j in range(2,i):
        if((i%j)==0):
            isprime=False
            break
    if(isprime):
        print(i)

