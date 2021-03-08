#Input a list/tuple of elements, search for a given element in the list/tuple.

n=int(input("Enter number of characters in tuple: "))
t=(tuple())
for i in range(0,n):
    a=input("Enter value for tuple: ")
    t+=(a,)

f=input("Which element do you want to find?")
if f in t:
    print("The index of ",f," is ",t.index(f))
else:
    print("The number is not in the tuple.")
