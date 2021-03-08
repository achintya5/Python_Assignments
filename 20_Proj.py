#Create a dictionary with the roll number, name and marks of n students in a
#class and display the names of students who have marks above 75.

d1={}
for i in range(0,2):
    r=int(input("Enter your roll no. here:"))
    n=input("Enter your name here: ")
    m=int(input("Enter your marks here: "))
    d1[r]=[n,m]


for i in d1:
    if d1[i][1]>75:
        print(d1[i][0],"  got more than 75 marks.")
