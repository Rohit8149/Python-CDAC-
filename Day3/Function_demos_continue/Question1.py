"""
1) create 3 functions "show1()","show2()" and "show3()"
now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.
"""
def show1():
    print("This is show1")
def show2():
    print("This is show2")
def show3():
    print("This is show3")

def caller(fun):
    fun()

caller(show1)
caller(show2)
caller(show3)