"""
9) define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]

"""
def func(*vars):
    sum = 0
    for i in vars:
        sum+=i
    print("Sum = ",sum)
func(2,3,4,4)
func(1)
func(50,47)