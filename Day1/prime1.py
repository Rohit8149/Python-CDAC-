#11) accept a number and display whether it is prime or not

num=int(input("Enter a number"))
isprime=True
for i in range(2,num):
    if num%i==0:
        isprime=False
        break
if isprime:
    print('it is prime number')
else:
    print('it is not prime number')