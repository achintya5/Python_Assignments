#Compute the greatest common divisor and least common multiple of two integers.

x=int(input("Enter an integral value here: "))
y=int(input("Enter an integral value here: "))

common=[]
for i in range(1,x+y):
    if x%i==0 and y%i==0:
        common.append(i)
hcf=max(common)
lcm=(x*y)//hcf

print("HCF is: ",hcf)
print("LCM is: ",lcm)
