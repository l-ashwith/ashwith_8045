a=int(input("Enter the length of list"))
l=[]
for i in range(a):
    l=l+[int(input("Enter any number"))]
print(l)
key=int(input("Enter a element to search"))
flag=0
for i in range(a):
    if l[i]==key:
        print("Element is found at :",i)
        flag=1
        break
if flag==0:
    print("Element not found in list")    