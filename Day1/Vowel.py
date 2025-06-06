# 2)	using switch ….case   display whether accepted character is vowel or not.

char = input("Enter A Character : ")
char = char.lower()

match char:
    case 'a':
        print("It is a Vowel")
    case 'e':
        print("It is a Vowel")
    case 'i':
        print("It is a Vowel")
    case 'o':
        print("It is a Vowel")
    case 'u':
        print("It is a Vowel")
    case _:
        print("It is not a vowel")
