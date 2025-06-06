"""
16) print the following pattern

*   *   *   *   *

  *   *   *   *

    *   *   *

      *   *

        *
"""

for i in range(1,6):
    for j in range(0,(6-i)):
        print('*',end ='   ')
    print()
    print()
    for k in range(0,i):
        print(" ",end=' ')