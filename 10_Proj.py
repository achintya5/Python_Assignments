#Input a number and check if the number is a prime or composite number. 

num=int(input("Enter a positive integer here: "))
if num<=0:
    print("Please enter a positive number")
elif num==1:
    print("Its neither prime nor composite")
elif num==2:
    print("Its a prime number")    

for i in range(2,num):
    if num%i==0:
        print("Its a composite number")
        break
    else:
        print("Its a prime number")
        break
    
    
