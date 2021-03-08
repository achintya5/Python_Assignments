"""Write a program to input the value of x and n and print the sum of the
following series:

x + x^2/2! - x^3/3! + x^4/4! - .............x^n/n! """

x=int(input("Enter an integral value here: "))
n=int(input("Enter the power here: "))

s=x
factorial=1

for i in range(2,n+1):
    for j in range(1,i+1):
        factorial*=j
    s+=((x**i)/factorial)*((-1)**i)
    factorial=1

print(s)
