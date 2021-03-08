"""
Input a list of numbers and test if a number is equal to the sum of the cubes of
its digits. Find the smallest and largest such number from the given list of
numbers. 
"""

n=int(input("How many numbers due you want to add to the list"))
list1=[]
for i in range(0, n): 
    a = int(input("Enter the number here:")) 
    list1.append(a)

count=0
list2=[]
for i in list1:
    i=str(i)
    s=0
    for j in range(0,len(i)):
        s+=(int(i[j]))**3
    
    if s==int(i):
        print(i," fulfills the given condition")
        list2.append(i)
        count+=1
if count>=1:
    print("The largest such number is: ",max(list2))
    print("The smallest such number is: ",min(list2))
else:
    print("There is no such number in the given list.")
