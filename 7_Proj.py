"""Write a program to input the value of x and n and print the sum of the
following series:

x + x^2/2 - x^3/3 + x^4/4 - .............x^n/n """

x=int(input("Enter an integral value here: "))
n=int(input("Enter the power here: "))

s=x

for i in range(2,n+1):
    s+=((x**i)/i)*((-1)**i)

print(s)

