"""
8) Note: use List comprehension
 create a list with the numbers from 1 to 20
 create one more list which should contain only odd numbers from the first list.
"""
list=[i for i in range(1,21)]
print(list)
list2=[i for i in list if i%2!=0]
print(list2)