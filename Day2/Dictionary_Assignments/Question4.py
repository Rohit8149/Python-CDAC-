"""

4)  Given a dictionary of students and their favourite colours:
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
1. Find out how many students are in the list
2. Change Lisa’s favourite colour
3. Remove 'Jenny' and her favourite color
4. Sort and print students and their favourite colours alphabetically by name
"""

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
#1 Find out how many students are in the list
print(len(people))
#2 Change Lisa’s favourite colour
print(people['Lisa'])
people['Lisa']='White'
print(people['Lisa'])

# 3. Remove 'Jenny' and her favourite color
print(people)
people.pop('Jenny')
print(people)

# 4. Sort and print students and their favourite colours alphabetically by name

for name in sorted(people):
    print(name," \t ",people[name])
