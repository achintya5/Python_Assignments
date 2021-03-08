#Input two numbers and display the larger / smaller number.
num1=int(input("Enter an integral value here: "))
num2=int(input("Enter another integral value here: "))
if num1> num2:
    print(num1, " is greater than ",num2)
elif num2>num1:
    print(num2, " is greater than ",num1)
else:
    print("Both the numbers are equal")

