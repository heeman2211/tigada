#  Program to check whether the given string is PALINDROME

def pal(a):
    b = a[::-1]
    if a == b:
        return a+" is Palindrome!"
    else:
        return a+" is not a Palindrome."

ms = input("Enter the string to check whether it is Palindrome or not:")

print(pal(ms))
print("END")
