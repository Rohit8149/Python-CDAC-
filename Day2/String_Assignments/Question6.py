"""
6) accept a sentence and reverse it.
	e.g.  hello world
		world hello
"""
string=input("Enter a String")
print(string)
mylist=string.split(' ')
# print(mylist)

mylist.reverse()
# print(mylist)
for i in mylist:
    print(i,end=' ')