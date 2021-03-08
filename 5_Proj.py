"""Write a program to input the value of x and n and print the sum of the
following series:
1+x+x^2+x^3+x^4+.............x^n
"""

x=int(input("Enter an integral value here: "))
n=int(input("Enter the power here: "))
s=0
for i in range(0,n+1):
    s+=x**i

print(s)
