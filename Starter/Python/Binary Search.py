a=[]
flag=0
n=int(input("enter how many number of elements"))
for i in range(n):
    a.append(int(input()))
print("List is:\n")
print(a)
key=int(input("enter key"))
l=0
h=n-1
while l<=h:
    mid=(l+h)//2
    if key==a[mid]:
        flag=1
        break
    elif key>a[mid]:
        l=mid+1
    else:
        h=mid-1
if flag==1:
    print("%d found at %d position" %(key,mid))
else:
    print("%d not found" %key)
