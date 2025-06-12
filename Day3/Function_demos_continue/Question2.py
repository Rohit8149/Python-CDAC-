# 2) define nested function and show how will you invoke it.

def fun1():
    def fun2():
        print("This is Function 2")
    print("This is Function 1")
    return fun2
x = fun1()
x()