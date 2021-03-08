#Determine whether a number is a perfect number, an armstrong number or a palindrome.

x=int(input("Enter an integer here:"))

#Perfect_num
sum=0
for i in range(1,x):        #not including the number itself
    if x%i==0:
        sum+=i
if sum==x:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")

#Armstrong_num
s=0
x=str(x)
l=len(x)
for i in range(0,l):
    s+=(int(x[i]))**l
x=int(x)
if s==x:
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")

#Palindrome
string1=""
for i in range(l-1,-1,-1):
    string1+=(str(x)[i])

string1=int(string1)
if string1==x:
    print("The number is a palindrome number.")
else:
        print("The number is not a palindrome number.")
