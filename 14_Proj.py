#Input a string and determine whether it is a palindrome or not; convert the
#case of characters in a string.

a=input("Enter a string here:")
r=a[::-1]

if r==a:
    print("Its a palindrome.")
else:
    print("Not a palindrome")

b=a.swapcase()
print("The string with changed casing is is: ", b)
