n=int(input())
l=list(map(int,input().split()))
x=0
y=0
for i in range(0,n):
    if i%2==0:
        y+=l[i]
    else:
        x+=l[i]
d=abs(x-y)
if d%4==0:
    print("X")
else:
    print("Y")