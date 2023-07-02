n=int(input("enter number "))
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s==n):
    print("It is a perfect number")
else:
    print("It is not a perfect number")