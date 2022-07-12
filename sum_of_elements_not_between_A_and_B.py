n=int(input())
a=list(map(int,input().split()))
x,y=map(int,input().split())
sum=0
for i in a:
    if i<x or i>y:
        sum+=i
print(sum)