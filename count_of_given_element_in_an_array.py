n=int(input())
a=list(map(int,input().split()))
x=int(input())
count=0
for i in a:
    if x==i:
        count+=1
print(count)