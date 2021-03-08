#Display the terms of a Fibonacci series.

n=int(input("How many numbers do you want to see from the series?"))

s=0
a=1
for i in range(0,n):
    print(s)
    s+=a
    a=s-a
    
    
