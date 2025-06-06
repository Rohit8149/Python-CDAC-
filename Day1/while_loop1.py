# 4)	Display numbers from 3 to 30 except number 24  using while loop.

i=3
while i<31:
    if i==24:
        i+=1
        continue
    print(i)
    i += 1