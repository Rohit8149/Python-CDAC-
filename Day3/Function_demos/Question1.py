"""1) define 3 functions "add()","modify()" and "delete()" with just a print message.
now accept input from user as a number. if the number entered is 1, call "add()"
if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]
 """
def add():
    print("This is a Add Function")
def modify():
    print("This is a Modify Function")
def delete():
    print("This is a Delete Function")

print("Enter a Number\n1:add\n2:modify\n3:delete")
num = int(input())

match num:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()
    case _:
        print("Your Number Doesn't Match the option")