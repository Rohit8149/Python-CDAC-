# 6) define a function which accepts a character and return toggle of it.

def toggle(char):
    if char.lower()==char:
        return char.upper()
    else:
        return char.lower()
print((toggle('A')))