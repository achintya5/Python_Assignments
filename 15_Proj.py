#Find the largest/smallest number in a list/tuple
list1=[]
n=int(input("How many numbers due you want to print"))
for i in range(0, n): 
    b = int(input("Enter the number here:")) 
    list1.append(b)

print("The largest number in the list is: ", max(list1))
print("The smallest number in the list is: ", min(list1))
