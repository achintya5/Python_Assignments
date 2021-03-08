#Input a list of elements, sort in ascending/descending order using
#Bubble/Insertion sort.

n=int(input("How many numbers due you want to print"))
list1=[]
for i in range(0, n): 
    b = int(input("Enter the number here:")) 
    list1.append(b)


for k in range(len(list1)-1,0,-1):
        for i in range(k):
            if list1[i]>list1[i+1]:
                a = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = a
        
print("The sorted list is: ",list1)
