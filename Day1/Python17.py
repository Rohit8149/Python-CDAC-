"""17) print the following

     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
"""

for i in range(1,6):
    for k in range(1,(6-i)):
        print('', end=' ')
    for j in range(0,i):
        print('*',end =' ')

    print()

for i in range(1,5):
    print('', end=' ')
    for k in range(5 - i):
        print('*', end=' ')
    print()
    for j in range(0,i):
        print('',end=' ')