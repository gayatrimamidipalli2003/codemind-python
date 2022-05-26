n=int(input())
a=list(map(int,input().split()))
x=int(input())
first=-1
last=-1
for i in range(0,n):
    if a[i]==x and first==-1:
        first=i
    if a[i]==x:
        last=i
print(first,last)
        