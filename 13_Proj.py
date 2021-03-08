#Count and display the number of vowels, consonants, uppercase, lowercase characters in string.

a=input("Enter a string here: ")
l=len(a)
d=0
s=l
c=0
uc=0
lc=0
sc="!@#$%^&*()_"
for i in a:
    if i.isdigit():
        d+=1
    elif i in sc:
        c+=1
    elif i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
s=s-(d+c)
print("Special characters- ",c)
print("Alphabets- ",s)
print("Numbers- ",d)
print("Upper case letters- ",uc)
print("Lower case letters- ",lc)

        

