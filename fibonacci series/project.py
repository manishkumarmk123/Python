a=0
b=1
c=0
n=int(input("Enter the number to make fibonacci series "))
print(a)
print(b)
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    print(c)